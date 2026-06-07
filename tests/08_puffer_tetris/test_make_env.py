from __future__ import annotations

from conftest import load_symbol


def test_make_env_returns_plain_tetris_env():
    make_env = load_symbol("bellman2tetris.project_08_puffer_tetris", "make_env")

    env = make_env(width=6, height=10, seed=0)

    assert hasattr(env, "reset")
    assert hasattr(env, "step")
    assert hasattr(env, "action_space")

