from __future__ import annotations

from conftest import load_symbol


def test_full_rows():
    full_rows = load_symbol(
        "bellman2tetris.project_05_tetris_features", "full_rows"
    )

    board = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ]

    assert full_rows(board) == [1, 3]

