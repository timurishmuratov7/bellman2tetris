from __future__ import annotations

import random

from conftest import load_symbol


def test_epsilon_greedy_from_q_explores_and_exploits():
    epsilon_greedy_from_q = load_symbol(
        "bellman2tetris.project_02_td_control", "epsilon_greedy_from_q"
    )

    assert epsilon_greedy_from_q([0.1, 0.9], 0.0, random.Random(0)) == 1

    rng = random.Random(42)
    actions = {epsilon_greedy_from_q([0.1, 0.9], 1.0, rng) for _ in range(30)}
    assert actions == {0, 1}

