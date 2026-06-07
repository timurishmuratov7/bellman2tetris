from __future__ import annotations

from conftest import load_symbol


def test_clear_lines_removes_full_rows_and_counts_them():
    clear_lines = load_symbol("bellman2tetris.project_06_tetris_core", "clear_lines")

    board = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ]

    new_board, cleared = clear_lines(board)

    assert cleared == 2
    assert new_board == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
    ]

