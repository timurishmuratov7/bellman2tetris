from __future__ import annotations

from conftest import load_symbol


BOARD = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
]


def test_bumpiness():
    bumpiness = load_symbol(
        "bellman2tetris.project_05_tetris_features", "bumpiness"
    )
    assert bumpiness(BOARD) == 6

