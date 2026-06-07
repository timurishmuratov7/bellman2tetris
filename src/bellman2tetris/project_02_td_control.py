"""Project 02: temporal-difference learning and control.

This file introduces the first full learning loop in the course: a tiny 1D
environment plus TD(0), SARSA, and Q-learning helpers.

Conventions used in this file:
- ``LineWorld`` states are integer positions ``0`` through ``length - 1``.
- The leftmost and rightmost states are terminal.
- Actions are encoded as integers:
  ``0 = move left`` and ``1 = move right``.
- ``rng`` means a ``random.Random`` instance used for reproducible exploration.
- A ``q_table`` should map each state to the action values for its available
  actions. The later ``greedy_policy(...)`` helper should map each state to the
  single best action index.

Tests for this file live in ``tests/02_td_control/``.
"""

from __future__ import annotations

import random


class LineWorld:
    """Minimal 1D environment with terminal rewards at both ends.

    For the default ``length=5``, the states are ``0, 1, 2, 3, 4`` and the
    starting state is the center state ``2``.

    Terminal semantics:
    - reaching state ``0`` ends the episode with reward ``-1.0``
    - reaching state ``length - 1`` ends the episode with reward ``+1.0``
    - all non-terminal transitions give reward ``0.0``
    """

    def __init__(self, length: int = 5):
        """Create the environment.

        Parameters
        ----------
        length:
            Total number of states on the line. It should be an odd integer of
            at least ``3`` so there is a unique center starting state.
        """
        raise NotImplementedError

    def reset(self) -> int:
        """Reset the environment to the center state.

        Returns
        -------
        int
            The center-state index from which each episode starts.
        """
        raise NotImplementedError

    def step(self, action: int) -> tuple[int, float, bool]:
        """Advance the environment by one action.

        Parameters
        ----------
        action:
            Integer action code where ``0`` means left and ``1`` means right.

        Returns
        -------
        tuple[int, float, bool]
            ``(next_state, reward, terminated)`` after applying the action.
        """
        raise NotImplementedError


def td0_update(
    old_value: float, reward: float, next_value: float, alpha: float, gamma: float
) -> float:
    """Apply one TD(0) update to a scalar state-value estimate.

    Parameters
    ----------
    old_value:
        Current estimate ``V(s)``.
    reward:
        Immediate reward observed after leaving state ``s``.
    next_value:
        Current estimate ``V(s')`` of the next state.
    alpha:
        Learning rate.
    gamma:
        Discount factor.

    Returns
    -------
    float
        The updated value
        ``old_value + alpha * (reward + gamma * next_value - old_value)``.
    """
    raise NotImplementedError


def epsilon_greedy_from_q(
    q_values, epsilon: float, rng: random.Random
) -> int:
    """Choose an action index from one state's Q-values.

    Parameters
    ----------
    q_values:
        The action values for one state, ordered by action index.
    epsilon:
        Exploration probability in ``[0.0, 1.0]``.
    rng:
        ``random.Random`` instance used for exploration and tie-breaking.

    Returns
    -------
    int
        The chosen action index for that state's row of Q-values.
    """
    raise NotImplementedError


def sarsa(
    env, episodes: int, alpha: float, gamma: float, epsilon: float, seed: int = 0
) -> dict:
    """Learn a Q-table with on-policy SARSA.

    Parameters
    ----------
    env:
        Environment exposing ``reset()`` and ``step(action)`` like ``LineWorld``.
    episodes:
        Number of training episodes.
    alpha:
        Learning rate.
    gamma:
        Discount factor.
    epsilon:
        Exploration probability for epsilon-greedy action selection.
    seed:
        Seed for the local random number generator used during training.

    Returns
    -------
    dict
        Learned Q-table mapping each state to its action-value row.
    """
    raise NotImplementedError


def q_learning(
    env, episodes: int, alpha: float, gamma: float, epsilon: float, seed: int = 0
) -> dict:
    """Learn a Q-table with off-policy Q-learning.

    Parameters
    ----------
    env:
        Environment exposing ``reset()`` and ``step(action)``.
    episodes:
        Number of training episodes.
    alpha:
        Learning rate.
    gamma:
        Discount factor.
    epsilon:
        Exploration probability for behavior-policy action selection.
    seed:
        Seed for the local random number generator used during training.

    Returns
    -------
    dict
        Learned Q-table mapping each state to its action-value row.
    """
    raise NotImplementedError


def greedy_policy(q_table) -> dict:
    """Convert a Q-table into a deterministic policy.

    Parameters
    ----------
    q_table:
        Mapping from state to that state's action-value row.

    Returns
    -------
    dict
        Mapping from each state to the integer index of its greedy action.
    """
    raise NotImplementedError
