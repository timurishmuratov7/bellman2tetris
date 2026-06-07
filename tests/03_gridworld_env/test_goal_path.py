from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")

from conftest import as_tuple_1d, load_symbol


def test_gridworld_reaches_goal():
    GridWorldEnv = load_symbol(
        "bellman2tetris.project_03_gridworld", "GridWorldEnv"
    )

    env = GridWorldEnv(size=3)
    env.reset(seed=0)

    env.step(1)
    env.step(1)
    env.step(2)
    obs, reward, terminated, truncated, _ = env.step(2)

    assert as_tuple_1d(obs["agent"]) == (2, 2)
    assert reward == 1.0
    assert terminated is True
    assert truncated is False

