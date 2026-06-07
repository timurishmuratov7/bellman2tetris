from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")
from gymnasium.utils.env_checker import check_env

from conftest import load_symbol


def test_tetris_env_passes_env_checker():
    TetrisEnv = load_symbol("bellman2tetris.project_07_tetris_env", "TetrisEnv")
    check_env(TetrisEnv(width=6, height=10, seed=0).unwrapped)

