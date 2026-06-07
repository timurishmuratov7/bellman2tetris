from __future__ import annotations

from conftest import load_symbol


def test_rotate_clockwise():
    rotate_clockwise = load_symbol(
        "bellman2tetris.project_06_tetris_core", "rotate_clockwise"
    )

    piece = [[1, 0], [1, 1], [1, 0]]

    assert rotate_clockwise(piece) == [[1, 1, 1], [0, 1, 0]]

