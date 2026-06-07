from __future__ import annotations

import pytest

from conftest import load_symbol


def test_incremental_average_matches_sample_mean():
    incremental_average = load_symbol(
        "bellman2tetris.project_00_bandits", "incremental_average"
    )

    estimate = 0.0
    rewards = [2.0, 4.0, 8.0]

    for step, reward in enumerate(rewards, start=1):
        estimate = incremental_average(estimate, reward, step)

    assert estimate == pytest.approx(sum(rewards) / len(rewards))


def test_incremental_average_first_step_equals_reward():
    incremental_average = load_symbol(
        "bellman2tetris.project_00_bandits", "incremental_average"
    )

    assert incremental_average(old_estimate=123.0, reward=7.5, step=1) == pytest.approx(
        7.5
    )


def test_incremental_average_handles_negative_rewards():
    incremental_average = load_symbol(
        "bellman2tetris.project_00_bandits", "incremental_average"
    )

    estimate = 0.0
    rewards = [-2.0, 4.0, -6.0, 8.0]

    for step, reward in enumerate(rewards, start=1):
        estimate = incremental_average(estimate, reward, step)

    assert estimate == pytest.approx(sum(rewards) / len(rewards))
