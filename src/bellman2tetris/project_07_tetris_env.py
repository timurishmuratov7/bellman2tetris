"""Project 07: a Gymnasium-style Tetris environment.

This file wraps the pure board mechanics from Project 06 in an environment API
that can be stepped, reset, checked with Gymnasium tools, and later wrapped for
PufferLib.

Conventions for this project:
- The observation is a board of shape ``(height, width)``.
- Recommended cell values are:
  ``0 = empty``, ``1 = locked block``, ``2 = currently falling piece``.
- Actions are encoded as integers:
  ``0 = move left``, ``1 = move right``, ``2 = rotate clockwise``,
  ``3 = soft drop``, ``4 = hard drop``.
- ``test_env_hard_drop.py`` specifically expects action ``4`` to perform a
  hard drop.

Tests for this file live in ``tests/07_tetris_env/``.
"""

from __future__ import annotations


class TetrisEnv:
    """Minimal single-agent Tetris environment for debugging and training.

    The environment should expose Gymnasium-style ``reset`` and ``step``
    methods, plus ``action_space`` and ``observation_space`` attributes.
    """

    def __init__(self, width: int = 6, height: int = 10, seed: int | None = None):
        """Create the environment.

        Parameters
        ----------
        width:
            Number of board columns.
        height:
            Number of board rows.
        seed:
            Optional initial RNG seed used for piece generation.
        """
        raise NotImplementedError

    def reset(self, *, seed=None, options=None):
        """Reset the environment to the start of a new episode.

        Parameters
        ----------
        seed:
            Optional Gymnasium seed.
        options:
            Optional Gymnasium reset options dictionary. This project does not
            need to use it, but the parameter must be accepted.

        Returns
        -------
        tuple[object, dict]
            ``(observation, info)`` where ``observation`` is the board state
            and ``info`` is typically ``{}``.
        """
        raise NotImplementedError

    def step(self, action: int):
        """Apply one Tetris action.

        Parameters
        ----------
        action:
            Integer action code:
            ``0 = left``, ``1 = right``, ``2 = rotate``, ``3 = soft drop``,
            ``4 = hard drop``.

        Returns
        -------
        tuple[object, float, bool, bool, dict]
            ``(observation, reward, terminated, truncated, info)`` following
            the Gymnasium API.
        """
        raise NotImplementedError
