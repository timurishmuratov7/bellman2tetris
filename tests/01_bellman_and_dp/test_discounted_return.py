from __future__ import annotations

import pytest

from conftest import load_symbol


def test_discounted_return_matches_hand_calculation():
    discounted_return = load_symbol(
        "bellman2tetris.project_01_bellman_dp", "discounted_return"
    )
    value = discounted_return([1.0, 2.0, 3.0], gamma=0.5)
    assert value == pytest.approx(1.0 + 0.5 * 2.0 + 0.25 * 3.0)

