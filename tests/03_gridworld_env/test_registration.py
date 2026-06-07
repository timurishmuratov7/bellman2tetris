from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")
from gymnasium.utils.env_checker import check_env

from conftest import load_symbol


def test_gridworld_registration_and_env_checker():
    register_envs = load_symbol(
        "bellman2tetris.project_03_gridworld", "register_envs"
    )
    GridWorldEnv = load_symbol(
        "bellman2tetris.project_03_gridworld", "GridWorldEnv"
    )

    register_envs()
    env = gymnasium.make("BellmanGridWorld-v0")
    check_env(GridWorldEnv(size=4).unwrapped)
    env.close()

