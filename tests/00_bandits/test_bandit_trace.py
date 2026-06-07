from __future__ import annotations

import pytest

from conftest import load_symbol


def test_simulate_bandit_returns_complete_trace():
    simulate_bandit = load_symbol(
        "bellman2tetris.project_00_bandits", "simulate_bandit"
    )

    trace = simulate_bandit([0.2, 0.5, -0.1], steps=25, epsilon=0.1, seed=0)

    assert set(trace) == {
        "arm_means",
        "optimal_action",
        "actions",
        "rewards",
        "estimates",
        "counts",
        "cumulative_reward",
    }
    assert trace["arm_means"] == [0.2, 0.5, -0.1]
    assert trace["optimal_action"] == 1
    assert len(trace["actions"]) == 25
    assert len(trace["rewards"]) == 25
    assert len(trace["estimates"]) == 25
    assert len(trace["counts"]) == 25
    assert len(trace["cumulative_reward"]) == 25
    assert all(len(snapshot) == 3 for snapshot in trace["estimates"])
    assert all(len(snapshot) == 3 for snapshot in trace["counts"])
    assert sum(trace["counts"][-1]) == 25


def test_simulate_bandit_cumulative_reward_matches_reward_prefix_sums():
    simulate_bandit = load_symbol(
        "bellman2tetris.project_00_bandits", "simulate_bandit"
    )

    trace = simulate_bandit([0.2, 0.5, -0.1], steps=10, epsilon=0.1, seed=3)

    running_total = 0.0
    expected = []
    for reward in trace["rewards"]:
        running_total += reward
        expected.append(running_total)

    assert trace["cumulative_reward"] == pytest.approx(expected)


def test_simulate_bandit_snapshots_are_independent_lists():
    simulate_bandit = load_symbol(
        "bellman2tetris.project_00_bandits", "simulate_bandit"
    )

    trace = simulate_bandit([0.2, 0.5, -0.1], steps=5, epsilon=0.1, seed=1)

    if len(trace["estimates"]) >= 2:
        assert trace["estimates"][0] is not trace["estimates"][1]
    if len(trace["counts"]) >= 2:
        assert trace["counts"][0] is not trace["counts"][1]


def test_simulate_bandit_is_deterministic_for_seed():
    simulate_bandit = load_symbol(
        "bellman2tetris.project_00_bandits", "simulate_bandit"
    )

    first = simulate_bandit([0.1, 0.8], steps=15, epsilon=0.2, seed=7)
    second = simulate_bandit([0.1, 0.8], steps=15, epsilon=0.2, seed=7)

    assert first["actions"] == second["actions"]
    assert first["counts"] == second["counts"]
    assert first["rewards"] == pytest.approx(second["rewards"])
