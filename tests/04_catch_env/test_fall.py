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


def test_catch_fruit_falls_one_row_per_step():
    CatchEnv = load_symbol("bellman2tetris.project_04_catch", "CatchEnv")

    env = CatchEnv(width=5, height=6)
    obs, _ = env.reset(seed=0)
    start_row, _ = locate(as_tuple_2d(obs), 1)

    obs, reward, terminated, truncated, _ = env.step(1)
    next_row, _ = locate(as_tuple_2d(obs), 1)

    assert next_row == start_row + 1
    assert reward == 0.0
    assert terminated is False
    assert truncated is False

