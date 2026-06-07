from __future__ import annotations

from conftest import load_symbol


def test_collides_with_walls_and_filled_cells():
    collides = load_symbol("bellman2tetris.project_06_tetris_core", "collides")

    board = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    piece = [[1, 1], [1, 1]]

    assert collides(board, piece, x=3, y=0) is True
    assert collides(board, piece, x=0, y=1) is True
    assert collides(board, piece, x=2, y=2) is False

