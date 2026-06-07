# Local Workflow

This repo keeps the tracked curriculum files as starter surfaces.
Your real implementations can live in a local ignored overlay.

## Folder Layout

- tracked starter modules: `src/bellman2tetris/`
- local ignored modules: `.local/bellman2tetris/`

Mirror the filename of any module you want to implement locally.

Example:

- starter stub: `src/bellman2tetris/project_00_bandits.py`
- your real code: `.local/bellman2tetris/project_00_bandits.py`

## How It Works

The package loader prepends `.local/bellman2tetris/` to the package search path
when that folder exists.

That means:

- if a module exists only in `src/bellman2tetris/`, the starter version is used
- if the same module also exists in `.local/bellman2tetris/`, your local copy is used instead

This lets the public repo stay as unimplemented coursework while your machine
can still run tests, viewers, and experiments against your own code.

## Recommended Habit

1. Read the starter file in `src/bellman2tetris/`.
2. Create the matching file in `.local/bellman2tetris/`.
3. Implement there.
4. Run the normal commands:
   `python project_00.py avg-test`
   `python project_00.py avg-vis`
   `pytest tests/00_bandits/test_incremental_average.py -q`

You do not need special flags or custom commands.
