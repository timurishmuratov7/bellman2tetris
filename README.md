# bellman2tetris

An RL-flavored, nand2tetris-style curriculum for learning reinforcement learning from first principles and ending with a Tetris environment that plugs into PufferLib.

This repo is intentionally code-light. You write the code by hand. The repo gives you:

- a 14-day schedule,
- project specs,
- curated reading links,
- tests that act as the contract for each checkpoint,
- and a minimal visualization path so each project has something dynamic to look at.

## Ground Rules

- Treat `src/bellman2tetris/` as the public starter surface.
- Write your own local implementations in `.local/bellman2tetris/` with the same filenames as the starter modules you want to override.
- Read the matching project brief in `projects/<project_name>/README.md` before writing code.
- Run only the tests for your current project until they pass.
- Use the matching visual checkpoint once the tests pass.
- Keep notes as you go. If you can explain the Bellman equation in plain English, you are learning the right thing.

## Local Workflow

The repo is designed so the tracked files can stay as clean stubs for anyone who
clones it, while your real code lives only on your machine.

- Starter surface: `src/bellman2tetris/project_00_bandits.py`
- Local implementation: `.local/bellman2tetris/project_00_bandits.py`

When you run `python project_00.py ...`, `python project_01.py ...`, or `pytest`,
imports from `bellman2tetris` will prefer the local file if it exists.

More detail lives in [docs/local_workflow.md](docs/local_workflow.md).

## Suggested Workflow

1. Install the light dependencies:

```sh
python -m pip install -r requirements.txt
```

2. Install the visualization dependency when you want the live viewers:

```sh
python -m pip install -r requirements-visuals.txt
```

3. Work through the schedule in [docs/roadmap.md](docs/roadmap.md).

4. Activate your virtual environment first so `python` points at the project
   interpreter, then use the root-level helper runners:

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

5. Project 01 follows the same pattern:

```sh
python project_01.py return-test
python project_01.py backups-test
python project_01.py policy-test
python project_01.py value-test
python project_01.py dp-vis
```

6. Only run the full suite after you have implemented everything:

```sh
pytest -q
```

## Repo Layout

- `docs/roadmap.md`: the 14-day plan with hour budgets and pacing.
- `docs/references.md`: the short, high-signal reading list.
- `docs/local_workflow.md`: how local ignored implementations override the starter stubs.
- `docs/platform_notes.md`: practical notes about Windows, WSL, and PufferLib.
- `docs/visualizations.md`: the visualization contract and viewer commands.
- `project_00.py` and `project_01.py`: easy root-level runners for the earliest checkpoints.
- `projects/`: one folder per project, each with its own brief.
- `tests/`: one folder per project, split into small checkpoints.
- `src/bellman2tetris/`: one starter file per project.

## Scope

The goal is not to learn every RL algorithm. The goal is to build a strong staircase:

1. Bellman equations and tabular RL.
2. Tiny custom environments.
3. A simple falling-object game.
4. Tetris board mechanics and features.
5. A Gymnasium Tetris environment.
6. A PufferLib-compatible wrapper and training entry point.

## Important Honesty Clause

"Solve Tetris" is ambitious. For this repo, treat success as:

- your environment works correctly,
- a simple baseline policy beats random,
- and your final RL training setup learns a stable non-trivial strategy.

If you exceed that and get strong play on full-size Tetris, even better.
