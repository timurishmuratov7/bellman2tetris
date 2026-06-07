# Visualizations

Every project should end with something you can watch, not just something that passes tests.

## Library Choice

Use the `raylib` Python package and its `pyray` module.

Why this choice:

- the official package supports Windows with an official Python build,
- it exposes a Pythonic `pyray` API,
- and it keeps the viewer code short.

Install it with:

```sh
python -m pip install -r requirements-visuals.txt
```

## Design Rule

The learning code remains yours.

The visualization code should stay tiny and reusable. That means:

- your RL functions return plain Python data,
- the shared viewer reads that data,
- and the viewer does not contain RL logic.

## Current Viewer Commands

### Bandits

```sh
python project_00.py avg-vis
python project_00.py argmax-vis
python project_00.py epsilon-vis
python project_00.py bandit-vis
```

Expected implementation hook:

- `bellman2tetris.project_00_bandits.incremental_average(...)`
- `bellman2tetris.project_00_bandits.argmax_tie_break(...)`
- `bellman2tetris.project_00_bandits.epsilon_greedy_action(...)`
- `bellman2tetris.project_00_bandits.simulate_bandit(...)`

What you should see:

- a step-by-step sample-average trace,
- a histogram showing random tie-breaking across equal maxima,
- a side-by-side epsilon-greedy action histogram,
- and then the full bandit learning trace.

All of these viewers are now debugger-style:

- click `Prev` and `Next` to move one step at a time,
- click `Reset` to go back to the start,
- click `Final` to jump to the last step,
- or use `Left/Right`, `A/D`, `Home`, and `End`.

### Dynamic Programming

```sh
python project_01.py dp-vis
```

Expected implementation hook:

- `bellman2tetris.project_01_bellman_dp.trace_value_iteration(...)`

What you should see:

- one line per state value,
- and each sweep moving toward convergence.

This viewer also uses the same step controls instead of autoplay.

## Future Visual Checkpoints

- `LineWorld`: animate state transitions under the learned policy.
- `GridWorld`: show the moving agent and goal.
- `Catch`: animate the falling fruit and paddle.
- `Tetris`: render the board, active piece, line clears, and game over.

## Philosophy

If a project has a core quantity that changes over time, it should have a trace.

If a project has a board, it should have a renderer.
