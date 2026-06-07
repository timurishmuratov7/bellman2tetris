# Platform Notes

## Native Windows vs WSL2

For the early projects, native Windows is fine.

For the final PufferLib stretch, the safest plan is:

- do the early RL and Gymnasium work on Windows,
- then switch the final integration work to **WSL2 Ubuntu** or Linux if PufferLib installation gets painful.

Why this caution:

- The current PufferLib docs strongly emphasize Docker, CUDA, and Linux-style workflows.
- The official `pufferlib-core` PyPI page currently shows Linux and macOS wheels, but no Windows wheel listing.
- A PufferAI project page for Pokegym explicitly says: **use Linux or WSL if you are on Windows**.

Treat that as a practical warning, not a hard ban. If native Windows works later, great. If not, do not waste half a weekend fighting the toolchain.

## What To Install When

### Now

- Python
- Git
- `pytest`
- the packages in `requirements.txt`

### Later

- `torch`
- `pufferlib`
- WSL2 Ubuntu if needed

## Philosophy

Do not let infrastructure become the curriculum.

The learning goals are:

- understand RL math,
- write environments correctly,
- and ship a working Tetris training pipeline.

If WSL2 is the shortest path to that, use it.

