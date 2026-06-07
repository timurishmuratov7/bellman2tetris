from __future__ import annotations

from conftest import load_symbol


def test_line_world_reset_and_terminal_rewards():
    LineWorld = load_symbol("bellman2tetris.project_02_td_control", "LineWorld")

    env = LineWorld(length=5)
    state = env.reset()
    assert state == 2

    state, reward, terminated = env.step(0)
    assert (state, reward, terminated) == (1, 0.0, False)

    state, reward, terminated = env.step(0)
    assert (state, reward, terminated) == (0, -1.0, True)

