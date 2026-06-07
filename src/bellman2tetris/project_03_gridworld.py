"""Project 03: a first Gymnasium-style GridWorld.

This file is your first environment API project. The goal is not complexity;
the goal is to learn the exact ``reset``/``step`` contract cleanly.

Conventions for this project:
- The board is a square of size ``size x size``.
- The agent starts at the top-left corner ``(0, 0)``.
- The goal is fixed at the bottom-right corner ``(size - 1, size - 1)``.
- Actions are encoded as integers:
  ``0 = up``, ``1 = right``, ``2 = down``, ``3 = left``.
- Observations are dictionaries with exactly two entries:
  ``{"agent": ..., "goal": ...}``.

Tests for this file live in ``tests/03_gridworld_env/``.
"""

from __future__ import annotations


class GridWorldEnv:
    """Small deterministic grid world with one agent and one fixed goal.

    The environment should expose standard Gymnasium attributes such as
    ``action_space`` and ``observation_space`` and should return the usual
    five-tuple from ``step(...)``.
    """

    def __init__(self, size: int = 5):
        """Create the environment.

        Parameters
        ----------
        size:
            Width and height of the square grid in cells.
        """
        raise NotImplementedError

    def reset(self, *, seed=None, options=None):
        """Reset the environment to its start state.

        Parameters
        ----------
        seed:
            Optional Gymnasium seed passed through to the environment RNG.
        options:
            Optional Gymnasium reset options dictionary. This project does not
            need to use it, but the parameter must be accepted.

        Returns
        -------
        tuple[dict, dict]
            ``(observation, info)`` where ``observation`` is a dictionary with
            ``"agent"`` and ``"goal"`` entries and ``info`` is typically ``{}``.
        """
        raise NotImplementedError

    def step(self, action: int):
        """Apply one movement action.

        Parameters
        ----------
        action:
            Integer code for one of the four moves:
            ``0 = up``, ``1 = right``, ``2 = down``, ``3 = left``.

        Returns
        -------
        tuple[dict, float, bool, bool, dict]
            ``(observation, reward, terminated, truncated, info)`` following
            the Gymnasium API.
        """
        raise NotImplementedError


def register_envs() -> None:
    """Register the environment with Gymnasium under ``BellmanGridWorld-v0``.

    Returns
    -------
    None
        This helper exists for its side effect on Gymnasium's registry.
    """
    raise NotImplementedError
