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


def test_value_iteration_finds_optimal_values():
    value_iteration = load_symbol(
        "bellman2tetris.project_01_bellman_dp", "value_iteration"
    )
    states, actions, transitions = tiny_mdp()

    values = value_iteration(
        states, actions, transitions, gamma=0.9, theta=1e-10
    )

    assert values["T"] == pytest.approx(0.0)
    assert values["B"] == pytest.approx(2.0, abs=1e-6)
    assert values["A"] == pytest.approx(2.8, abs=1e-6)


def test_trace_value_iteration_returns_sweep_history():
    trace_value_iteration = load_symbol(
        "bellman2tetris.project_01_bellman_dp", "trace_value_iteration"
    )
    value_iteration = load_symbol(
        "bellman2tetris.project_01_bellman_dp", "value_iteration"
    )
    states, actions, transitions = tiny_mdp()

    sweeps = trace_value_iteration(
        states, actions, transitions, gamma=0.9, theta=1e-10
    )
    final_values = value_iteration(
        states, actions, transitions, gamma=0.9, theta=1e-10
    )

    assert isinstance(sweeps, list)
    assert sweeps
    assert all(set(sweep) == {"A", "B", "T"} for sweep in sweeps)
    assert sweeps[-1]["A"] == pytest.approx(final_values["A"], abs=1e-6)
    assert sweeps[-1]["B"] == pytest.approx(final_values["B"], abs=1e-6)
    assert sweeps[-1]["T"] == pytest.approx(final_values["T"], abs=1e-6)

