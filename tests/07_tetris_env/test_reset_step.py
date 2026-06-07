from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")

from conftest import load_symbol


def test_tetris_env_reset_and_step_shape():
    TetrisEnv = load_symbol("bellman2tetris.project_07_tetris_env", "TetrisEnv")

    env = TetrisEnv(width=6, height=10, seed=0)
    obs, info = env.reset(seed=0)

    assert hasattr(obs, "shape")
    assert tuple(obs.shape) == (10, 6)
    assert env.action_space.n == 5
    assert info == {}

    obs, reward, terminated, truncated, info = env.step(4)

    assert tuple(obs.shape) == (10, 6)
    assert isinstance(float(reward), float)
    assert isinstance(terminated, bool)
    assert isinstance(truncated, bool)
    assert isinstance(info, dict)

