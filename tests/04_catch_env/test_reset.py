from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")

from conftest import as_tuple_2d, load_symbol


def test_catch_reset_contains_one_fruit_and_one_paddle():
    CatchEnv = load_symbol("bellman2tetris.project_04_catch", "CatchEnv")

    env = CatchEnv(width=5, height=6)
    obs, info = env.reset(seed=0)
    board = as_tuple_2d(obs)

    fruit_count = sum(cell == 1 for row in board for cell in row)
    paddle_count = sum(cell == 2 for row in board for cell in row)

    assert len(board) == 6
    assert len(board[0]) == 5
    assert fruit_count == 1
    assert paddle_count == 1
    assert info == {}

