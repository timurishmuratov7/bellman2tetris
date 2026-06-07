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


def test_expected_q_uses_one_step_bellman_backup():
    expected_q = load_symbol("bellman2tetris.project_01_bellman_dp", "expected_q")
    _, _, transitions = tiny_mdp()

    values = {"A": 0.0, "B": 2.0, "T": 0.0}
    q_value = expected_q("A", "go", values, transitions, gamma=0.9)

    assert q_value == pytest.approx(1.0 + 0.9 * 2.0)


def test_expected_v_aggregates_over_policy():
    expected_v = load_symbol("bellman2tetris.project_01_bellman_dp", "expected_v")
    _, actions, transitions = tiny_mdp()
    values = {"A": 0.5, "B": 2.0, "T": 0.0}
    policy = {
        "A": {"wait": 0.25, "go": 0.75},
        "B": {"finish": 1.0},
        "T": {},
    }

    value = expected_v("A", values, policy, actions, transitions, gamma=0.9)
    assert value == pytest.approx(0.25 * 0.45 + 0.75 * 2.8)

