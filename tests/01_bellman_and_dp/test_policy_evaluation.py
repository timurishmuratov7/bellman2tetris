from __future__ import annotations

import pytest

from conftest import load_symbol


def tiny_mdp():
    states = ("A", "B", "T")
    actions = {"A": ("wait", "go"), "B": ("finish",), "T": ()}
    transitions = {
        ("A", "wait"): [(1.0, "A", 0.0)],
        ("A", "go"): [(1.0, "B", 1.0)],
        ("B", "finish"): [(1.0, "T", 2.0)],
    }
    return states, actions, transitions


def test_policy_evaluation_solves_tiny_deterministic_mdp():
    policy_evaluation = load_symbol(
        "bellman2tetris.project_01_bellman_dp", "policy_evaluation"
    )
    states, actions, transitions = tiny_mdp()
    policy = {"A": {"wait": 0.0, "go": 1.0}, "B": {"finish": 1.0}, "T": {}}

    values = policy_evaluation(
        states, actions, transitions, policy, gamma=0.9, theta=1e-10
    )

    assert values["T"] == pytest.approx(0.0)
    assert values["B"] == pytest.approx(2.0, abs=1e-6)
    assert values["A"] == pytest.approx(2.8, abs=1e-6)


def test_greedy_policy_picks_best_action():
    greedy_policy_from_values = load_symbol(
        "bellman2tetris.project_01_bellman_dp", "greedy_policy_from_values"
    )
    states, actions, transitions = tiny_mdp()
    values = {"A": 2.8, "B": 2.0, "T": 0.0}

    policy = greedy_policy_from_values(
        states, actions, transitions, values, gamma=0.9
    )

    assert policy["A"] == {"go": 1.0}
    assert policy["B"] == {"finish": 1.0}

