from __future__ import annotations

from conftest import load_symbol


def test_lock_piece_returns_new_board_with_piece_added():
    lock_piece = load_symbol("bellman2tetris.project_06_tetris_core", "lock_piece")

    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    original = [row[:] for row in board]
    piece = [[1, 1], [1, 1]]

    locked = lock_piece(board, piece, x=1, y=2)

    assert board == original
    assert locked == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
    ]

