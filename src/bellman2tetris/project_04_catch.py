"""Project 04: Catch, the bridge between toy RL and Tetris.

This environment is still tiny, but it introduces the ingredients that matter
for Tetris later: a board, falling objects, horizontal control, and terminal
success or failure.

Conventions for this project:
- The observation is a 2D board of shape ``(height, width)``.
- Cell values mean:
  ``0 = empty``, ``1 = fruit``, ``2 = paddle``.
- Actions are encoded as integers:
  ``0 = move paddle left``, ``1 = stay``, ``2 = move paddle right``.
- One environment step should always move the fruit down by exactly one row.

Tests for this file live in ``tests/04_catch_env/``.
"""

from __future__ import annotations


class CatchEnv:
    """Single-fruit, single-paddle environment on a discrete board.

    The episode ends when the fruit reaches the paddle row. Catching the fruit
    should give a positive terminal reward; missing it should end the episode
    with a non-positive reward.
    """

    def __init__(self, width: int = 5, height: int = 6):
        """Create the environment.

        Parameters
        ----------
        width:
            Number of board columns.
        height:
            Number of board rows.
        """
        raise NotImplementedError

    def reset(self, *, seed=None, options=None):
        """Reset the board to a new episode.

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
            ``(observation, info)`` where ``observation`` is the board and
            ``info`` is typically ``{}``.
        """
        raise NotImplementedError

    def step(self, action: int):
        """Advance the environment by one time step.

        Parameters
        ----------
        action:
            Integer code where ``0`` moves the paddle left, ``1`` keeps it in
            place, and ``2`` moves it right.

        Returns
        -------
        tuple[object, float, bool, bool, dict]
            ``(observation, reward, terminated, truncated, info)`` following
            the Gymnasium API.
        """
        raise NotImplementedError
