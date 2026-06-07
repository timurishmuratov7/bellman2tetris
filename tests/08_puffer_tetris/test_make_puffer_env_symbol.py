from __future__ import annotations

from conftest import load_symbol


def test_make_puffer_env_exists_even_if_pufferlib_is_not_installed():
    load_symbol("bellman2tetris.project_08_puffer_tetris", "make_puffer_env")

