from __future__ import annotations

from conftest import load_symbol


def test_hard_drop_lands_on_the_floor():
    hard_drop_y = load_symbol("bellman2tetris.project_06_tetris_core", "hard_drop_y")

    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    piece = [[1, 1], [1, 1]]

    assert hard_drop_y(board, piece, x=1, start_y=0) == 2

