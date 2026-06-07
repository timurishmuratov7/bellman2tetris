from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")

from conftest import load_symbol


def test_tetris_hard_drop_creates_locked_blocks():
    TetrisEnv = load_symbol("bellman2tetris.project_07_tetris_env", "TetrisEnv")

    env = TetrisEnv(width=6, height=10, seed=0)
    env.reset(seed=0)
    obs, _, _, _, _ = env.step(4)

    values = set(obs.flatten().tolist())
    assert values.issubset({0, 1, 2})
    assert 1 in values

