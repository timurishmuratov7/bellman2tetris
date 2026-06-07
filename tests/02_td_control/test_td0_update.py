from __future__ import annotations

import pytest

from conftest import load_symbol


def test_td0_update_matches_equation():
    td0_update = load_symbol("bellman2tetris.project_02_td_control", "td0_update")

    updated = td0_update(
        old_value=1.0,
        reward=2.0,
        next_value=4.0,
        alpha=0.25,
        gamma=0.5,
    )

    assert updated == pytest.approx(1.75)

