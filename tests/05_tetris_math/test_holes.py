from __future__ import annotations

from conftest import load_symbol


BOARD = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
]


def test_count_holes():
    count_holes = load_symbol(
        "bellman2tetris.project_05_tetris_features", "count_holes"
    )
    assert count_holes(BOARD) == 1

