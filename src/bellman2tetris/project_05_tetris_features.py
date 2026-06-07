"""Project 05: board features for Tetris-style evaluation.

This file is the board-analysis layer, not the game engine. Each helper takes a
board and extracts one numeric property that later policies or heuristics can
use.

Board conventions for this file:
- ``board`` is a rectangular 2D structure indexed as ``board[row][col]``.
- Row ``0`` is the top of the board.
- A zero cell is empty.
- A non-zero cell is occupied.

Tests for this file live in ``tests/05_tetris_math/``.
"""

from __future__ import annotations


def column_heights(board) -> list[int]:
    """Measure the occupied height of every column.

    Parameters
    ----------
    board:
        2D board where zero means empty and non-zero means occupied.

    Returns
    -------
    list[int]
        One height per column, measured from the bottom of the board up to the
        highest occupied cell in that column. An empty column has height ``0``.
    """
    raise NotImplementedError


def count_holes(board) -> int:
    """Count holes in the board.

    Parameters
    ----------
    board:
        2D occupancy grid.

    Returns
    -------
    int
        Number of empty cells that have at least one occupied cell somewhere
        above them in the same column.
    """
    raise NotImplementedError


def bumpiness(board) -> int:
    """Measure how uneven the surface of the board is.

    Parameters
    ----------
    board:
        2D occupancy grid.

    Returns
    -------
    int
        Sum of absolute differences between adjacent column heights.
    """
    raise NotImplementedError


def full_rows(board) -> list[int]:
    """Find all completely filled rows.

    Parameters
    ----------
    board:
        2D occupancy grid.

    Returns
    -------
    list[int]
        Row indices whose cells are all occupied.
    """
    raise NotImplementedError


def extract_features(board) -> dict:
    """Compute the core feature bundle for one board position.

    Parameters
    ----------
    board:
        2D occupancy grid.

    Returns
    -------
    dict
        Dictionary containing at least these keys:
        ``"column_heights"``, ``"holes"``, ``"bumpiness"``, and ``"full_rows"``.
    """
    raise NotImplementedError
