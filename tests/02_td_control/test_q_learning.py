from __future__ import annotations

from conftest import load_symbol


def test_q_learning_learns_to_move_right_from_the_start_state():
    LineWorld = load_symbol("bellman2tetris.project_02_td_control", "LineWorld")
    q_learning = load_symbol("bellman2tetris.project_02_td_control", "q_learning")
    greedy_policy = load_symbol(
        "bellman2tetris.project_02_td_control", "greedy_policy"
    )

    env = LineWorld(length=5)
    q_table = q_learning(
        env,
        episodes=200,
        alpha=0.2,
        gamma=0.9,
        epsilon=0.1,
        seed=0,
    )
    policy = greedy_policy(q_table)

    assert policy[2] == 1

