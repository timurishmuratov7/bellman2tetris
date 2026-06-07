# Project 02: TD Learning, SARSA, and Q-Learning

Starter file:

- `src/bellman2tetris/project_02_td_control.py`

Run these checkpoints in order:

```sh
pytest tests/02_td_control/test_line_world.py -q
pytest tests/02_td_control/test_td0_update.py -q
pytest tests/02_td_control/test_q_action_selection.py -q
pytest tests/02_td_control/test_sarsa.py -q
pytest tests/02_td_control/test_q_learning.py -q
```

Read first:

- Sutton and Barto Chapters 5 and 6
- David Silver Lectures 3 and 4

Build:

1. `LineWorld`
2. `td0_update(...)`
3. `epsilon_greedy_from_q(...)`
4. `sarsa(...)`
5. `q_learning(...)`
6. `greedy_policy(...)`
