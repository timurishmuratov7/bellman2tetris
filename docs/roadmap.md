# 14-Day Roadmap

This schedule assumes you want to spend:

- **4 hours on work days**
- **8 hours on weekends**

That gives you **72 hours total** over 14 days.

## Daily Plan

### Day 1 - 4h

- Read the first project brief.
- Learn the agent / environment / reward / return loop.
- Implement incremental averages and epsilon-greedy action selection.
- Build the stationary bandit simulation trace.
- Pass the checkpoints in `tests/00_bandits/`.

### Day 2 - 4h

- Learn MDP notation, discounted return, and Bellman expectation backups.
- Implement the small MDP helpers.
- Implement the value sweep trace for visualization.
- Pass the first checkpoints in `tests/01_bellman_and_dp/`.

### Day 3 - 4h

- Implement policy evaluation, policy improvement, policy iteration, and value iteration.
- Pass the rest of `tests/01_bellman_and_dp/`.

### Day 4 - 4h

- Learn Monte Carlo vs TD vs bootstrapping.
- Implement the `LineWorld` environment and TD update helpers.

### Day 5 - 4h

- Implement SARSA and Q-learning in `LineWorld`.
- Pass the checkpoints in `tests/02_td_control/`.

### Day 6 - 8h

- Build your first Gymnasium environment: `GridWorldEnv`.
- Register it and validate it with the Gymnasium env checker.
- Pass the checkpoints in `tests/03_gridworld_env/`.

### Day 7 - 8h

- Build `CatchEnv`, your first tiny falling-object game.
- Use it as the bridge from toy RL to Tetris-like dynamics.
- Pass the checkpoints in `tests/04_catch_env/`.

### Day 8 - 4h

- Learn linear function approximation.
- Implement board feature helpers for future Tetris work.
- Start the checkpoints in `tests/05_tetris_math/`.

### Day 9 - 4h

- Finish feature extraction functions.
- Write down why holes, height, and bumpiness matter for Tetris.
- Pass the checkpoints in `tests/05_tetris_math/`.

### Day 10 - 4h

- Implement piece rotation and collision detection.
- Start the checkpoints in `tests/06_tetris_core/`.

### Day 11 - 4h

- Implement line clearing, locking, hard drop, and spawn/game-over logic.
- Pass the checkpoints in `tests/06_tetris_core/`.

### Day 12 - 4h

- Wrap the board engine in `TetrisEnv`.
- Pass the checkpoints in `tests/07_tetris_env/`.

### Day 13 - 8h

- Move to WSL2 or Linux if needed.
- Build the PufferLib-compatible wrapper.
- Pass the checkpoints in `tests/08_puffer_tetris/`.

### Day 14 - 8h

- Tune rewards and observations.
- Train a baseline.
- Write a short retrospective: what worked, what broke, what you still do not fully understand.

## Milestones

- End of Day 5: you understand tabular RL and can implement it.
- End of Day 7: you can write custom Gymnasium environments.
- End of Day 11: you have a correct Tetris engine.
- End of Day 14: you have a PufferLib-ready Tetris project.

Every milestone should also leave behind a working visualization, not just passing tests.

## If You Slip

If one day goes badly, cut scope in this order:

1. skip fancy plotting,
2. skip deep RL and stay with linear baselines,
3. use a smaller board for early Tetris tests,
4. delay native-speed Puffer work until after the first end-to-end Python version works.
