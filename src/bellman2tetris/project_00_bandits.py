"""Project 00: stationary multi-armed bandits.

This file is the hand-written API surface for the first project in the course.
You implement one symbol at a time and test or visualize it separately.

What lives here:
- a sample-average update rule for one action value,
- greedy action selection with random tie-breaking,
- epsilon-greedy exploration,
- and a full stationary Gaussian bandit simulation trace.

Conventions used throughout this file:
- An "action" is a zero-based integer index into a list such as
  ``arm_means`` or ``values``.
- ``rng`` means a ``random.Random`` instance. Use that object for every random
  choice instead of the global ``random`` module state so results stay
  reproducible for a fixed seed.
- ``simulate_bandit(...)`` returns a dictionary with these exact keys:
  ``arm_means``, ``optimal_action``, ``actions``, ``rewards``, ``estimates``,
  ``counts``, and ``cumulative_reward``.

Tests for this file live in ``tests/00_bandits/``.
Use ``python project_00.py list`` from the repo root to see the checkpoints.
"""

from __future__ import annotations

import random
from typing import Sequence


def incremental_average(old_estimate: float, reward: float, step: int) -> float:
    """Update a sample mean after observing one more reward.

    Parameters
    ----------
    old_estimate:
        The previous estimate before incorporating ``reward``. In bandit terms
        this is usually the old action-value estimate ``Q_n``.
    reward:
        The newly observed scalar reward.
    step:
        The 1-based count of how many rewards have been seen for this action
        after including ``reward``. For the first observation, ``step == 1``.

    Returns
    -------
    float
        The new sample-average estimate
    """
    raise NotImplementedError


def argmax_tie_break(values: Sequence[float], rng: random.Random) -> int:
    """Return the index of the largest value, breaking ties uniformly at random.

    Parameters
    ----------
    values:
        A non-empty sequence of numeric scores, one per action.
    rng:
        A ``random.Random`` generator used only for tie-breaking when multiple
        actions share the same maximum value.

    Returns
    -------
    int
        The zero-based index of one maximizing entry in ``values``.
    """
    raise NotImplementedError


def epsilon_greedy_action(
    values: Sequence[float], epsilon: float, rng: random.Random
) -> int:
    """Choose one action with epsilon-greedy exploration.

    Parameters
    ----------
    values:
        Current action-value estimates, one score per action.
    epsilon:
        Exploration probability in the closed interval ``[0.0, 1.0]``.
        With probability ``epsilon`` choose a random action uniformly from all
        actions. With probability ``1 - epsilon`` choose greedily using
        ``argmax_tie_break(...)``.
    rng:
        A ``random.Random`` generator used for both the explore/exploit coin
        flip and the random action selection.

    Returns
    -------
    int
        The chosen zero-based action index.

    Raises
    ------
    ValueError
        If ``epsilon`` is smaller than ``0.0`` or larger than ``1.0``.
    """
    raise NotImplementedError


def simulate_bandit(
    arm_means: Sequence[float], steps: int, epsilon: float, seed: int = 0
) -> dict:
    """Simulate a stationary Gaussian bandit and record the entire learning trace.

    Parameters
    ----------
    arm_means:
        True mean reward of each bandit arm. If ``arm_means[a] == 0.5``, then
        action ``a`` should draw rewards from a Gaussian centered at ``0.5``.
    steps:
        Number of interaction steps to simulate.
    epsilon:
        Exploration probability passed to ``epsilon_greedy_action(...)``.
    seed:
        Integer seed used to create the local ``random.Random`` instance for the
        full simulation.

    Returns
    -------
    dict
        A dictionary with the exact structure below.

        ``trace["arm_means"]``
            ``list[float]`` copy of the true arm means.
        ``trace["optimal_action"]``
            ``int`` index of the arm with the largest true mean.
        ``trace["actions"]``
            ``list[int]`` of length ``steps`` containing the selected action at
            each time step.
        ``trace["rewards"]``
            ``list[float]`` of length ``steps`` containing the observed reward
            after each chosen action.
        ``trace["estimates"]``
            ``list[list[float]]`` where each entry is a snapshot of all current
            action-value estimates immediately after that step.
        ``trace["counts"]``
            ``list[list[int]]`` where each entry is a snapshot of how many times
            each action has been selected so far.
        ``trace["cumulative_reward"]``
            ``list[float]`` of running reward totals, one prefix sum per step.
    """
    raise NotImplementedError
