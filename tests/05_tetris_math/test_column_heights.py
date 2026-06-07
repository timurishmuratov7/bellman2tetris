from __future__ import annotations

from conftest import load_symbol


BOARD = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
]


def test_column_heights():
    column_heights = load_symbol(
        "bellman2tetris.project_05_tetris_features", "column_heights"
    )
    assert column_heights(BOARD) == [2, 3, 0, 2]

