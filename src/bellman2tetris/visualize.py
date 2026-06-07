from __future__ import annotations

import argparse
import importlib
import random
from collections import Counter
from typing import Iterable


def _require_pyray():
    try:
        import pyray  # type: ignore
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Install the viewer dependency first: "
            "python -m pip install -r requirements-visuals.txt"
        ) from exc
    return pyray


def _load(module_name: str, symbol_name: str):
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        raise SystemExit(
            f"Create {module_name.replace('.', '/')}.py before running this viewer."
        ) from exc

    if not hasattr(module, symbol_name):
        raise SystemExit(f"{module_name} is missing {symbol_name}.")

    return getattr(module, symbol_name)


def _draw_axes(pyray, x: int, y: int, width: int, height: int):
    pyray.draw_line(x, y + height, x + width, y + height, pyray.DARKGRAY)
    pyray.draw_line(x, y, x, y + height, pyray.DARKGRAY)


def _value_range(values: Iterable[float]) -> tuple[float, float]:
    values = list(values)
    if not values:
        return 0.0, 1.0

    low = min(values)
    high = max(values)
    if high == low:
        padding = 1.0 if high == 0 else abs(high) * 0.1
        low -= padding
        high += padding
    return low, high


def _draw_labeled_axes(
    pyray,
    x: int,
    y: int,
    width: int,
    height: int,
    *,
    x_max: int,
    y_values: Iterable[float],
    x_label: str = "step",
    y_label: str = "value",
    y_ticks: int = 4,
):
    _draw_axes(pyray, x, y, width, height)
    label_x = max(4, x - 56)

    low, high = _value_range(y_values)
    tick_count = max(2, y_ticks)
    for tick in range(tick_count + 1):
        fraction = tick / tick_count
        tick_y = y + height - int(fraction * height)
        tick_value = low + fraction * (high - low)
        pyray.draw_line(x - 6, tick_y, x, tick_y, pyray.DARKGRAY)
        pyray.draw_text(f"{tick_value:.2f}", label_x, tick_y - 8, 16, pyray.DARKGRAY)
        if tick not in (0, tick_count):
            pyray.draw_line(x, tick_y, x + width, tick_y, pyray.LIGHTGRAY)

    x_ticks = min(max(1, x_max), 5)
    for tick in range(x_ticks + 1):
        fraction = tick / max(1, x_ticks)
        tick_x = x + int(fraction * width)
        tick_step = int(round(fraction * x_max))
        pyray.draw_line(tick_x, y + height, tick_x, y + height + 6, pyray.DARKGRAY)
        pyray.draw_text(str(tick_step), tick_x - 8, y + height + 6, 16, pyray.DARKGRAY)

    pyray.draw_text(x_label, x + width - 30, y + height + 20, 18, pyray.DARKGRAY)
    pyray.draw_text(y_label, label_x, y - 24, 18, pyray.DARKGRAY)


def _scale_points(values: Iterable[float], x: int, y: int, width: int, height: int):
    values = list(values)
    if not values:
        return []

    low, high = _value_range(values)

    last_index = max(1, len(values) - 1)
    points = []
    for index, value in enumerate(values):
        px = x + int(width * (index / last_index))
        normalized = (value - low) / (high - low)
        py = y + height - int(normalized * height)
        points.append((px, py))
    return points


def _draw_series(pyray, values, color, x, y, width, height):
    points = _scale_points(values, x, y, width, height)
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        pyray.draw_line(x1, y1, x2, y2, color)


def _draw_bar_chart(pyray, values, labels, x, y, width, height, colors):
    if not values:
        return

    max_value = max(values)
    if max_value <= 0:
        max_value = 1

    count = len(values)
    gap = 12
    bar_width = max(20, (width - gap * (count - 1)) // count)

    for index, value in enumerate(values):
        bar_height = int((value / max_value) * (height - 40))
        bar_x = x + index * (bar_width + gap)
        bar_y = y + height - bar_height - 24
        color = colors[index % len(colors)]
        pyray.draw_rectangle(bar_x, bar_y, bar_width, bar_height, color)
        pyray.draw_text(str(labels[index]), bar_x, y + height - 20, 18, pyray.BLACK)
        pyray.draw_text(f"{value}", bar_x, bar_y - 22, 18, pyray.DARKGRAY)


def _point_in_rect(mouse_x: int, mouse_y: int, rect: tuple[int, int, int, int]) -> bool:
    x, y, width, height = rect
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height


def _draw_button(
    pyray, rect: tuple[int, int, int, int], label: str, *, enabled: bool = True
) -> bool:
    x, y, width, height = rect
    mouse_x = pyray.get_mouse_x()
    mouse_y = pyray.get_mouse_y()
    hovered = enabled and _point_in_rect(mouse_x, mouse_y, rect)

    if not enabled:
        fill = pyray.LIGHTGRAY
        text_color = pyray.GRAY
    elif hovered:
        fill = pyray.SKYBLUE
        text_color = pyray.BLACK
    else:
        fill = pyray.GRAY
        text_color = pyray.RAYWHITE

    pyray.draw_rectangle(x, y, width, height, fill)
    pyray.draw_rectangle_lines(x, y, width, height, pyray.DARKGRAY)
    text_width = pyray.measure_text(label, 20)
    pyray.draw_text(
        label,
        x + (width - text_width) // 2,
        y + (height - 20) // 2,
        20,
        text_color,
    )

    return enabled and hovered and pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT)


def _step_controls(pyray, step: int, max_step: int) -> int:
    control_y = pyray.get_screen_height() - 60

    if pyray.is_key_pressed(pyray.KEY_LEFT) or pyray.is_key_pressed(pyray.KEY_A):
        step = max(0, step - 1)
    if pyray.is_key_pressed(pyray.KEY_RIGHT) or pyray.is_key_pressed(pyray.KEY_D):
        step = min(max_step, step + 1)
    if pyray.is_key_pressed(pyray.KEY_HOME):
        step = 0
    if pyray.is_key_pressed(pyray.KEY_END):
        step = max_step

    if _draw_button(pyray, (40, control_y, 100, 40), "Prev", enabled=step > 0):
        step = max(0, step - 1)
    if _draw_button(
        pyray, (155, control_y, 100, 40), "Next", enabled=step < max_step
    ):
        step = min(max_step, step + 1)
    if _draw_button(pyray, (270, control_y, 100, 40), "Reset", enabled=step != 0):
        step = 0
    if _draw_button(
        pyray, (385, control_y, 100, 40), "Final", enabled=step != max_step
    ):
        step = max_step

    pyray.draw_text("Left/Right or A/D: step", 520, control_y + 2, 18, pyray.DARKGRAY)
    pyray.draw_text("Home/End: jump   Esc: close", 520, control_y + 22, 18, pyray.DARKGRAY)
    return step


def _project_00():
    module_name = "bellman2tetris.project_00_bandits"
    return {
        "incremental_average": _load(module_name, "incremental_average"),
        "argmax_tie_break": _load(module_name, "argmax_tie_break"),
        "epsilon_greedy_action": _load(module_name, "epsilon_greedy_action"),
        "simulate_bandit": _load(module_name, "simulate_bandit"),
    }


def show_bandit_average():
    pyray = _require_pyray()
    incremental_average = _project_00()["incremental_average"]

    rewards = [2.0, 4.0, 8.0, 1.0, 5.0, 3.0, 6.0, 7.0]
    estimates = []
    sample_means = []
    estimate = 0.0
    running_total = 0.0

    try:
        for step, reward in enumerate(rewards, start=1):
            estimate = incremental_average(estimate, reward, step)
            estimates.append(estimate)
            running_total += reward
            sample_means.append(running_total / step)
    except NotImplementedError as exc:
        raise SystemExit("Implement incremental_average(...) before running avg-vis.") from exc

    pyray.init_window(1100, 680, "bellman2tetris - project 00 - incremental average")
    pyray.set_target_fps(60)
    step = 0

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        step = _step_controls(pyray, step, len(rewards))
        current_index = max(0, step - 1)

        pyray.draw_text("Project 00: incremental average", 40, 20, 28, pyray.BLACK)
        pyray.draw_text(
            f"step={step}/{len(rewards)}"
            + (
                ""
                if step == 0
                else f" reward={rewards[current_index]:.2f} estimate={estimates[current_index]:.2f}"
            ),
            40,
            56,
            22,
            pyray.DARKGRAY,
        )

        pyray.draw_text("Reward sequence", 40, 100, 24, pyray.BLACK)
        _draw_bar_chart(
            pyray,
            [abs(value) for value in rewards[:step]],
            [str(index + 1) for index in range(step)],
            40,
            140,
            480,
            220,
            [pyray.SKYBLUE],
        )

        pyray.draw_text("Estimate vs exact sample mean", 560, 100, 24, pyray.BLACK)
        _draw_labeled_axes(
            pyray,
            560,
            140,
            460,
            320,
            x_max=len(rewards),
            y_values=estimates[:step] + sample_means[:step],
            x_label="step",
            y_label="mean",
        )
        _draw_series(pyray, estimates[:step], pyray.MAROON, 560, 140, 460, 320)
        _draw_series(pyray, sample_means[:step], pyray.DARKGREEN, 560, 140, 460, 320)
        pyray.draw_text("estimate", 560, 472, 20, pyray.MAROON)
        pyray.draw_text("exact sample mean", 660, 472, 20, pyray.DARKGREEN)
        if step > 0:
            pyray.draw_text(
                f"estimate = {estimates[current_index]:.4f}",
                560,
                500,
                20,
                pyray.MAROON,
            )
            pyray.draw_text(
                f"sample mean = {sample_means[current_index]:.4f}",
                760,
                500,
                20,
                pyray.DARKGREEN,
            )
        pyray.draw_text(
            "Step through one reward at a time. If your function is correct, these lines should overlap.",
            40,
            560,
            22,
            pyray.DARKGRAY,
        )

        pyray.end_drawing()

    pyray.close_window()


def show_bandit_argmax():
    pyray = _require_pyray()
    argmax_tie_break = _project_00()["argmax_tie_break"]

    values = [1.0, 5.0, 5.0, 2.0]
    rng = random.Random(7)
    history = []

    try:
        for _ in range(180):
            history.append(argmax_tie_break(values, rng))
    except NotImplementedError as exc:
        raise SystemExit("Implement argmax_tie_break(...) before running argmax-vis.") from exc

    pyray.init_window(1100, 680, "bellman2tetris - project 00 - argmax tie break")
    pyray.set_target_fps(60)
    colors = [pyray.GRAY, pyray.RED, pyray.BLUE, pyray.GRAY]
    step = 0

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        step = _step_controls(pyray, step, len(history))
        counts = Counter(history[:step])
        pyray.draw_text("Project 00: argmax with random tie-breaking", 40, 20, 28, pyray.BLACK)
        pyray.draw_text(
            f"samples shown={step} tied max actions are 1 and 2",
            40,
            56,
            22,
            pyray.DARKGRAY,
        )

        pyray.draw_text("Input values", 40, 100, 24, pyray.BLACK)
        _draw_bar_chart(
            pyray,
            values,
            [str(index) for index in range(len(values))],
            40,
            140,
            480,
            260,
            colors,
        )

        pyray.draw_text("Chosen-action histogram", 560, 100, 24, pyray.BLACK)
        _draw_bar_chart(
            pyray,
            [counts.get(index, 0) for index in range(len(values))],
            [str(index) for index in range(len(values))],
            560,
            140,
            460,
            260,
            colors,
        )

        pyray.draw_text(
            "A correct tie-breaker should choose both max indices over time, not always the first one.",
            40,
            470,
            22,
            pyray.DARKGRAY,
        )

        pyray.end_drawing()

    pyray.close_window()


def show_bandit_epsilon():
    pyray = _require_pyray()
    epsilon_greedy_action = _project_00()["epsilon_greedy_action"]

    values = [0.2, 0.9, 0.4]
    rng_greedy = random.Random(11)
    rng_explore = random.Random(11)
    greedy_history = []
    explore_history = []

    try:
        for _ in range(180):
            greedy_history.append(epsilon_greedy_action(values, 0.0, rng_greedy))
            explore_history.append(epsilon_greedy_action(values, 0.3, rng_explore))
    except NotImplementedError as exc:
        raise SystemExit(
            "Implement epsilon_greedy_action(...) before running epsilon-vis."
        ) from exc

    pyray.init_window(1100, 720, "bellman2tetris - project 00 - epsilon greedy")
    pyray.set_target_fps(60)
    colors = [pyray.GRAY, pyray.RED, pyray.BLUE]
    step = 0

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        step = _step_controls(pyray, step, len(greedy_history))
        greedy_counts = Counter(greedy_history[:step])
        explore_counts = Counter(explore_history[:step])
        pyray.draw_text("Project 00: epsilon-greedy action choice", 40, 20, 28, pyray.BLACK)
        pyray.draw_text(
            f"samples shown={step} values={values}",
            40,
            56,
            22,
            pyray.DARKGRAY,
        )

        pyray.draw_text("epsilon = 0.0", 40, 110, 24, pyray.BLACK)
        _draw_bar_chart(
            pyray,
            [greedy_counts.get(index, 0) for index in range(len(values))],
            [str(index) for index in range(len(values))],
            40,
            150,
            460,
            250,
            colors,
        )

        pyray.draw_text("epsilon = 0.3", 580, 110, 24, pyray.BLACK)
        _draw_bar_chart(
            pyray,
            [explore_counts.get(index, 0) for index in range(len(values))],
            [str(index) for index in range(len(values))],
            580,
            150,
            460,
            250,
            colors,
        )

        pyray.draw_text(
            "With epsilon=0.0 almost everything should go to the greedy action. "
            "With epsilon=0.3 the non-greedy bars should wake up.",
            40,
            470,
            22,
            pyray.DARKGRAY,
        )

        pyray.end_drawing()

    pyray.close_window()


def show_bandit():
    pyray = _require_pyray()
    simulate_bandit = _project_00()["simulate_bandit"]

    try:
        trace = simulate_bandit([0.2, 0.5, -0.1], steps=200, epsilon=0.1, seed=0)
    except NotImplementedError as exc:
        raise SystemExit("Implement simulate_bandit(...) before running bandit-vis.") from exc

    estimates = trace["estimates"]
    cumulative_reward = trace["cumulative_reward"]
    optimal_action = trace["optimal_action"]
    colors = [pyray.RED, pyray.BLUE, pyray.GREEN, pyray.ORANGE, pyray.PURPLE]

    pyray.init_window(1100, 700, "bellman2tetris - project 00 - bandit trace")
    pyray.set_target_fps(60)
    step = 0

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        step = _step_controls(pyray, step, len(estimates))
        current_index = max(0, step - 1)

        pyray.draw_text("Project 00: full bandit trace", 40, 20, 28, pyray.BLACK)
        pyray.draw_text(
            f"step={step}/{len(estimates)} optimal_action={optimal_action}",
            40,
            56,
            22,
            pyray.DARKGRAY,
        )

        estimate_values = []
        for snapshot in estimates[:step]:
            estimate_values.extend(snapshot)
        _draw_labeled_axes(
            pyray,
            40,
            90,
            700,
            240,
            x_max=len(estimates),
            y_values=estimate_values,
            x_label="step",
            y_label="Q(a)",
        )
        for arm_index in range(len(estimates[0])):
            series = [snapshot[arm_index] for snapshot in estimates[:step]]
            _draw_series(
                pyray,
                series,
                colors[arm_index % len(colors)],
                40,
                90,
                700,
                240,
            )
            pyray.draw_text(
                f"arm {arm_index} true={trace['arm_means'][arm_index]:.2f}",
                770,
                100 + 28 * arm_index,
                20,
                colors[arm_index % len(colors)],
            )

        pyray.draw_text("Cumulative reward", 40, 370, 24, pyray.BLACK)
        _draw_labeled_axes(
            pyray,
            40,
            410,
            700,
            180,
            x_max=len(cumulative_reward),
            y_values=cumulative_reward[:step],
            x_label="step",
            y_label="sum r",
        )
        _draw_series(
            pyray,
            cumulative_reward[:step],
            pyray.MAROON,
            40,
            410,
            700,
            180,
        )

        if step > 0:
            pyray.draw_text(
                f"last action={trace['actions'][current_index]} reward={trace['rewards'][current_index]:.3f}",
                770,
                410,
                20,
                pyray.BLACK,
            )
            for arm_index, estimate_value in enumerate(estimates[current_index]):
                pyray.draw_text(
                    f"Q[{arm_index}]={estimate_value:.4f}",
                    770,
                    150 + 28 * arm_index,
                    20,
                    colors[arm_index % len(colors)],
                )
            pyray.draw_text(
                f"cum reward = {cumulative_reward[current_index]:.4f}",
                770,
                438,
                20,
                pyray.MAROON,
            )

        pyray.end_drawing()

    pyray.close_window()


def show_dp():
    pyray = _require_pyray()
    trace_value_iteration = _load(
        "bellman2tetris.project_01_bellman_dp", "trace_value_iteration"
    )

    states = ("A", "B", "T")
    actions = {"A": ("wait", "go"), "B": ("finish",), "T": ()}
    transitions = {
        ("A", "wait"): [(1.0, "A", 0.0)],
        ("A", "go"): [(1.0, "B", 1.0)],
        ("B", "finish"): [(1.0, "T", 2.0)],
    }
    sweeps = trace_value_iteration(
        states, actions, transitions, gamma=0.9, theta=1e-8
    )
    colors = {"A": pyray.RED, "B": pyray.BLUE, "T": pyray.GREEN}

    pyray.init_window(1100, 620, "bellman2tetris - value iteration trace")
    pyray.set_target_fps(60)
    step = 0

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        step = _step_controls(pyray, step, len(sweeps))
        current_index = max(0, step - 1)
        pyray.draw_text("Value iteration sweeps", 40, 20, 24, pyray.BLACK)
        pyray.draw_text(f"sweep={step}/{len(sweeps)}", 40, 52, 20, pyray.DARKGRAY)

        plot_values = []
        for sweep in sweeps[:step]:
            plot_values.extend(sweep.values())
        _draw_labeled_axes(
            pyray,
            40,
            90,
            760,
            380,
            x_max=len(sweeps),
            y_values=plot_values,
            x_label="sweep",
            y_label="V(s)",
        )
        for index, state in enumerate(states):
            series = [sweep.get(state, 0.0) for sweep in sweeps[:step]]
            _draw_series(pyray, series, colors[state], 40, 90, 760, 380)
            pyray.draw_text(
                f"{state} = {0.0 if step == 0 else sweeps[current_index].get(state, 0.0):.4f}",
                840,
                100 + 30 * index,
                22,
                colors[state],
            )

        pyray.end_drawing()

    pyray.close_window()


VIEWERS = {
    "bandit-average": show_bandit_average,
    "bandit-argmax": show_bandit_argmax,
    "bandit-epsilon": show_bandit_epsilon,
    "bandit": show_bandit,
    "dp": show_dp,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("viewer", choices=tuple(VIEWERS))
    args = parser.parse_args()
    VIEWERS[args.viewer]()


if __name__ == "__main__":
    main()
