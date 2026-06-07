"""Project 08: environment constructors and PufferLib integration.

This file should stay thin. The heavy lifting belongs in earlier projects:
board rules in Project 06 and the Gymnasium environment in Project 07.

What belongs here:
- ``make_env(...)``: construct the plain project Tetris environment.
- ``make_puffer_env(...)``: construct the PufferLib-compatible wrapped version.

Tests for this file live in ``tests/08_puffer_tetris/``.
"""

from __future__ import annotations


def make_env(**kwargs):
    """Construct the plain project Tetris environment.

    Parameters
    ----------
    **kwargs:
        Keyword arguments forwarded to ``TetrisEnv`` such as ``width``,
        ``height``, or ``seed``.

    Returns
    -------
    object
        A plain ``TetrisEnv`` instance exposing at least ``reset``, ``step``,
        and ``action_space``.
    """
    raise NotImplementedError


def make_puffer_env(**kwargs):
    """Construct the PufferLib-compatible Tetris environment.

    Parameters
    ----------
    **kwargs:
        Keyword arguments forwarded to the underlying Tetris environment
        constructor.

    Returns
    -------
    object
        A wrapped environment compatible with the PufferLib interface.

    Raises
    ------
    ImportError
        If PufferLib is not installed when the function is actually called.
    """
    raise NotImplementedError
