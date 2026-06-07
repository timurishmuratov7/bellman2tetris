from __future__ import annotations

import pytest

from conftest import load_symbol


def test_make_puffer_env_builds_when_pufferlib_is_available():
    pytest.importorskip("pufferlib")
    make_puffer_env = load_symbol(
        "bellman2tetris.project_08_puffer_tetris", "make_puffer_env"
    )

    env = make_puffer_env(width=6, height=10, seed=0)

    assert hasattr(env, "reset")
    assert hasattr(env, "step")
