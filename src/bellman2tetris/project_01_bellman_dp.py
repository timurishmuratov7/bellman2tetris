"""Project 01: Bellman equations and dynamic programming.

This file is the math-only API surface for planning in a finite Markov decision
process (MDP). No rendering or environment code belongs here.

Data conventions used in this file:
- ``states`` is an iterable of hashable state ids such as strings or integers.
- ``actions`` is a mapping like ``actions[state] -> tuple_of_actions``.
- ``transitions`` is a mapping whose keys are ``(state, action)`` pairs and
  whose values are lists of ``(probability, next_state, reward)`` tuples.
- ``policy`` is a mapping like ``policy[state] -> {action: probability}``.
- ``values`` is a mapping like ``values[state] -> V(state)``.

Tests for this file live in ``tests/01_bellman_and_dp/``.
Use ``python project_01.py list`` from the repo root to see the checkpoints.
"""

from __future__ import annotations


def discounted_return(rewards, gamma: float) -> float:
    """Compute the discounted return of a finite reward sequence.

    Parameters
    ----------
    rewards:
        Rewards ordered in time as ``[R_1, R_2, ..., R_n]``.
    gamma:
        Discount factor. Each reward is weighted by a power of ``gamma``.

    Returns
    -------
    float
        ``R_1 + gamma * R_2 + gamma^2 * R_3 + ...`` for the provided sequence.
    """
    raise NotImplementedError


def expected_q(state, action, values, transitions, gamma: float) -> float:
    """Compute a one-step Bellman expectation backup for ``Q(state, action)``.

    Parameters
    ----------
    state:
        The source state whose action value is being evaluated.
    action:
        The specific action to evaluate in ``state``.
    values:
        Current state-value estimate dictionary ``values[next_state]``.
    transitions:
        Mapping from ``(state, action)`` to a list of
        ``(probability, next_state, reward)`` tuples.
    gamma:
        Discount factor.

    Returns
    -------
    float
        The expected one-step backup
        ``sum_a p * (reward + gamma * values[next_state])`` over the transition
        outcomes for ``(state, action)``.
    """
    raise NotImplementedError


def expected_v(state, values, policy, actions, transitions, gamma: float) -> float:
    """Compute a one-step Bellman expectation backup for ``V(state)``.

    Parameters
    ----------
    state:
        State whose value is being updated.
    values:
        Current state-value dictionary.
    policy:
        Mapping from each state to an action-probability dictionary.
    actions:
        Mapping ``actions[state] -> iterable_of_available_actions``.
    transitions:
        Mapping from ``(state, action)`` to a list of
        ``(probability, next_state, reward)`` tuples.
    gamma:
        Discount factor.

    Returns
    -------
    float
        The policy-weighted expectation
        ``sum_action policy[state][action] * expected_q(...)``.
    """
    raise NotImplementedError


def policy_evaluation(
    states, actions, transitions, policy, gamma: float, theta: float = 1e-8
) -> dict:
    """Iteratively evaluate a fixed policy until the values converge.

    Parameters
    ----------
    states:
        Iterable of all states in the finite MDP.
    actions:
        Mapping ``actions[state] -> available actions``.
    transitions:
        Mapping from ``(state, action)`` to a list of
        ``(probability, next_state, reward)`` tuples.
    policy:
        Fixed policy represented as ``policy[state][action] = probability``.
    gamma:
        Discount factor.
    theta:
        Convergence tolerance. Stop once the largest absolute change in a full
        sweep is strictly smaller than ``theta``.

    Returns
    -------
    dict
        A dictionary mapping each state to its converged value under ``policy``.
    """
    raise NotImplementedError


def greedy_policy_from_values(states, actions, transitions, values, gamma: float) -> dict:
    """Create a deterministic greedy policy from a state-value function.

    Parameters
    ----------
    states:
        Iterable of all states.
    actions:
        Mapping ``actions[state] -> available actions``.
    transitions:
        Mapping from ``(state, action)`` to a list of
        ``(probability, next_state, reward)`` tuples.
    values:
        State-value dictionary used to score each action via Bellman backup.
    gamma:
        Discount factor.

    Returns
    -------
    dict
        A policy dictionary where each non-terminal state maps to a single
        action with probability ``1.0``, for example ``{"A": {"go": 1.0}}``.
    """
    raise NotImplementedError


def value_iteration(states, actions, transitions, gamma: float, theta: float = 1e-8) -> dict:
    """Compute the optimal state-value function by value iteration.

    Parameters
    ----------
    states:
        Iterable of all states.
    actions:
        Mapping ``actions[state] -> available actions``.
    transitions:
        Mapping from ``(state, action)`` to a list of
        ``(probability, next_state, reward)`` tuples.
    gamma:
        Discount factor.
    theta:
        Convergence tolerance for the maximum absolute update in one sweep.

    Returns
    -------
    dict
        A dictionary mapping each state to its optimal value estimate.
    """
    raise NotImplementedError


def trace_value_iteration(
    states, actions, transitions, gamma: float, theta: float = 1e-8
) -> list[dict]:
    """Record the full value table after every sweep of value iteration.

    Parameters
    ----------
    states:
        Iterable of all states.
    actions:
        Mapping ``actions[state] -> available actions``.
    transitions:
        Mapping from ``(state, action)`` to a list of
        ``(probability, next_state, reward)`` tuples.
    gamma:
        Discount factor.
    theta:
        Convergence tolerance used for the stopping condition.

    Returns
    -------
    list[dict]
        A non-empty list where each entry is a complete snapshot of the value
        dictionary after one sweep. The last snapshot should match the output of
        ``value_iteration(...)`` run with the same inputs.
    """
    raise NotImplementedError
