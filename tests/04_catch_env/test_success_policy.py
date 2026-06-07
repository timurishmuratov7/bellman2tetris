from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")

from conftest import as_tuple_2d, load_symbol


def locate(board, value):
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == value:
                return row_index, col_index
    raise AssertionError(f"Value {value} not found in board.")


def test_catch_policy_can_force_a_success():
    CatchEnv = load_symbol("bellman2tetris.project_04_catch", "CatchEnv")

    env = CatchEnv(width=5, height=6)
    obs, _ = env.reset(seed=0)

    while True:
        board = as_tuple_2d(obs)
        _, fruit_x = locate(board, 1)
        _, paddle_x = locate(board, 2)

        if fruit_x < paddle_x:
            action = 0
        elif fruit_x > paddle_x:
            action = 2
        else:
            action = 1

        obs, reward, terminated, truncated, _ = env.step(action)
        if terminated or truncated:
            break

    assert reward == 1.0
    assert terminated is True
    assert truncated is False

