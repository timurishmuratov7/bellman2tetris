from __future__ import annotations

import pytest

gymnasium = pytest.importorskip("gymnasium")
from gymnasium.utils.env_checker import check_env

from conftest import load_symbol


def test_catch_env_passes_env_checker():
    CatchEnv = load_symbol("bellman2tetris.project_04_catch", "CatchEnv")
    check_env(CatchEnv(width=5, height=6).unwrapped)

