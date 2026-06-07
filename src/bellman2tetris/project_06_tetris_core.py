"""Project 06: pure Tetris board mechanics.

This file is the deterministic rules layer underneath the environment. The goal
is to make the core board updates correct before adding Gymnasium or PufferLib
wrappers.

Board and piece conventions for this file:
- ``board`` is a 2D list indexed as ``board[row][col]`` with row ``0`` at the
  top.
- ``piece`` is a 2D list of ``0`` and ``1`` values where ``1`` means an
  occupied cell of the falling tetromino.
- Positions ``x`` and ``y`` refer to the top-left corner of the piece matrix on
  the board.
- These helpers should be pure: return new values instead of mutating inputs
  when practical.

Tests for this file live in ``tests/06_tetris_core/``.
"""

from __future__ import annotations


def rotate_clockwise(piece) -> list[list[int]]:
    """Rotate a piece matrix 90 degrees clockwise.

    Parameters
    ----------
    piece:
        2D list representing a tetromino footprint.

    Returns
    -------
    list[list[int]]
        A new rotated matrix. The input should not be mutated.
    """
    raise NotImplementedError


def collides(board, piece, x: int, y: int) -> bool:
    """Check whether placing a piece at ``(x, y)`` would collide.

    Parameters
    ----------
    board:
        Current board occupancy grid.
    piece:
        Piece matrix to test.
    x:
        Proposed left column of the piece.
    y:
        Proposed top row of the piece.

    Returns
    -------
    bool
        ``True`` if the piece would overlap a filled cell or leave the board,
        otherwise ``False``.
    """
    raise NotImplementedError


def lock_piece(board, piece, x: int, y: int) -> list[list[int]]:
    """Create a board with the piece merged into the occupied cells.

    Parameters
    ----------
    board:
        Current board occupancy grid.
    piece:
        Piece matrix to lock.
    x:
        Left column of the piece.
    y:
        Top row of the piece.

    Returns
    -------
    list[list[int]]
        A new board with the piece cells written into it.
    """
    raise NotImplementedError


def clear_lines(board) -> tuple[list[list[int]], int]:
    """Remove every full row and compact the board downward.

    Parameters
    ----------
    board:
        Current board occupancy grid.

    Returns
    -------
    tuple[list[list[int]], int]
        ``(new_board, cleared_count)`` where ``new_board`` has the same shape as
        the input board and ``cleared_count`` is the number of removed rows.
    """
    raise NotImplementedError


def hard_drop_y(board, piece, x: int, start_y: int = 0) -> int:
    """Compute the landing row for a hard drop.

    Parameters
    ----------
    board:
        Current board occupancy grid.
    piece:
        Piece matrix to drop.
    x:
        Left column at which the piece is dropped.
    start_y:
        Initial top row from which the drop begins.

    Returns
    -------
    int
        The final top-row position ``y`` where the piece comes to rest just
        before colliding.
    """
    raise NotImplementedError
