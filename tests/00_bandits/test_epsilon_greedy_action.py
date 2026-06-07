from __future__ import annotations

import random

import pytest

from conftest import load_symbol


def test_epsilon_greedy_prefers_greedy_action_when_epsilon_is_zero():
    epsilon_greedy_action = load_symbol(
        "bellman2tetris.project_00_bandits", "epsilon_greedy_action"
    )

    action = epsilon_greedy_action([0.1, 0.9, 0.2], 0.0, random.Random(0))
    assert action == 1


def test_epsilon_greedy_validates_epsilon():
    epsilon_greedy_action = load_symbol(
        "bellman2tetris.project_00_bandits", "epsilon_greedy_action"
    )

    with pytest.raises(ValueError):
        epsilon_greedy_action([0.1, 0.9], -0.1, random.Random(0))

    with pytest.raises(ValueError):
        epsilon_greedy_action([0.1, 0.9], 1.1, random.Random(0))


def test_epsilon_greedy_explores_when_epsilon_is_one():
    epsilon_greedy_action = load_symbol(
        "bellman2tetris.project_00_bandits", "epsilon_greedy_action"
    )

    rng = random.Random(123)
    actions = {
        epsilon_greedy_action([0.0, 10.0, 0.0], 1.0, rng)
        for _ in range(40)
    }

    assert actions.issubset({0, 1, 2})
    assert len(actions) > 1
