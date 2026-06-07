# Project 00: Bandits and Incremental Learning

Starter file:

- `src/bellman2tetris/project_00_bandits.py`

Run these checkpoints in order:

```sh
python project_00.py avg-test
python project_00.py avg-vis
python project_00.py argmax-test
python project_00.py argmax-vis
python project_00.py epsilon-test
python project_00.py epsilon-vis
python project_00.py bandit-test
python project_00.py bandit-vis
```

Activate your virtual environment first so `python` resolves to the project interpreter.

The visualizers are step-based, not autoplay:

- click `Prev` and `Next` like a debugger,
- use `Reset` and `Final` to jump,
- or use `Left/Right`, `A/D`, `Home`, and `End`.

Read first:

- Sutton and Barto Chapter 2
- Spinning Up RL intro

Build:

1. `incremental_average(...)`
2. `argmax_tie_break(...)`
3. `epsilon_greedy_action(...)`
4. `simulate_bandit(...)`

Checkpoint map:

1. After `incremental_average(...)`:
   `python project_00.py avg-test`
   `python project_00.py avg-vis`
2. After `argmax_tie_break(...)`:
   `python project_00.py argmax-test`
   `python project_00.py argmax-vis`
3. After `epsilon_greedy_action(...)`:
   `python project_00.py epsilon-test`
   `python project_00.py epsilon-vis`
4. After `simulate_bandit(...)`:
   `python project_00.py bandit-test`
   `python project_00.py bandit-vis`

Trace contract:

- return `arm_means`, `optimal_action`, `actions`, `rewards`, `estimates`, `counts`, and `cumulative_reward`
- make `estimates` and `counts` full per-step snapshots

Visual checkpoint:

```sh
python project_00.py bandit-vis
```
