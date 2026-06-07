from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")

from conftest import as_tuple_1d, load_symbol


def test_gridworld_reset_and_basic_step():
    GridWorldEnv = load_symbol(
        "bellman2tetris.project_03_gridworld", "GridWorldEnv"
    )

    env = GridWorldEnv(size=4)
    obs, info = env.reset(seed=0)

    assert set(obs) == {"agent", "goal"}
    assert as_tuple_1d(obs["agent"]) == (0, 0)
    assert as_tuple_1d(obs["goal"]) == (3, 3)
    assert info == {}
    assert env.action_space.n == 4

    obs, reward, terminated, truncated, info = env.step(1)

    assert as_tuple_1d(obs["agent"]) == (0, 1)
    assert reward == 0.0
    assert terminated is False
    assert truncated is False
    assert info == {}

