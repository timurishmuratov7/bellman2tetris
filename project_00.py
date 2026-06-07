"""Convenience runner for Project 00 checkpoints.

Run this file from the repository root to test or visualize one tiny piece at a
time without installing the package first.
"""

from __future__ import annotations

import argparse
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def _run_pytest(path: str) -> int:
    import pytest

    return pytest.main([str(ROOT / path), "-q"])


def _run_viewer(viewer_name: str) -> None:
    from bellman2tetris import visualize

    visualize.VIEWERS[viewer_name]()


COMMANDS = {
    "avg-test": {
        "description": "Run the incremental-average checkpoint test.",
        "type": "test",
        "target": "tests/00_bandits/test_incremental_average.py",
    },
    "avg-vis": {
        "description": "Visualize incremental-average updates over a fixed reward list.",
        "type": "viewer",
        "target": "bandit-average",
    },
    "argmax-test": {
        "description": "Run the argmax tie-break checkpoint test.",
        "type": "test",
        "target": "tests/00_bandits/test_argmax_tie_break.py",
    },
    "argmax-vis": {
        "description": "Visualize random tie-breaking between equal max values.",
        "type": "viewer",
        "target": "bandit-argmax",
    },
    "epsilon-test": {
        "description": "Run the epsilon-greedy checkpoint test.",
        "type": "test",
        "target": "tests/00_bandits/test_epsilon_greedy_action.py",
    },
    "epsilon-vis": {
        "description": "Visualize how epsilon changes the action histogram.",
        "type": "viewer",
        "target": "bandit-epsilon",
    },
    "bandit-test": {
        "description": "Run the full stationary-bandit trace checkpoint test.",
        "type": "test",
        "target": "tests/00_bandits/test_bandit_trace.py",
    },
    "bandit-vis": {
        "description": "Visualize the full Project 00 bandit trace.",
        "type": "viewer",
        "target": "bandit",
    },
    "all-tests": {
        "description": "Run every Project 00 test checkpoint.",
        "type": "test",
        "target": "tests/00_bandits",
    },
    "list": {
        "description": "Print every available Project 00 command.",
        "type": "meta",
        "target": "",
    },
}


def _print_commands() -> None:
    print("Project 00 commands:\n")
    for name, config in COMMANDS.items():
        print(f"  {name:<12} {config['description']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Project 00 checkpoint runner")
    parser.add_argument("command", nargs="?", default="list", choices=tuple(COMMANDS))
    args = parser.parse_args()

    command = COMMANDS[args.command]
    if command["type"] == "meta":
        _print_commands()
        return 0

    if command["type"] == "test":
        return _run_pytest(command["target"])

    _run_viewer(command["target"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
