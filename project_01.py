"""Convenience runner for Project 01 checkpoints.

Run this file from the repository root to test or visualize one dynamic-
programming checkpoint at a time without installing the package first.
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
    "return-test": {
        "description": "Run the discounted-return checkpoint test.",
        "type": "test",
        "target": "tests/01_bellman_and_dp/test_discounted_return.py",
    },
    "backups-test": {
        "description": "Run the Bellman backup checkpoint tests.",
        "type": "test",
        "target": "tests/01_bellman_and_dp/test_expected_backups.py",
    },
    "policy-test": {
        "description": "Run the policy-evaluation checkpoint tests.",
        "type": "test",
        "target": "tests/01_bellman_and_dp/test_policy_evaluation.py",
    },
    "value-test": {
        "description": "Run the value-iteration checkpoint tests.",
        "type": "test",
        "target": "tests/01_bellman_and_dp/test_value_iteration.py",
    },
    "dp-vis": {
        "description": "Visualize value-iteration sweeps on the tiny MDP.",
        "type": "viewer",
        "target": "dp",
    },
    "all-tests": {
        "description": "Run every Project 01 test checkpoint.",
        "type": "test",
        "target": "tests/01_bellman_and_dp",
    },
    "list": {
        "description": "Print every available Project 01 command.",
        "type": "meta",
        "target": "",
    },
}


def _print_commands() -> None:
    print("Project 01 commands:\n")
    for name, config in COMMANDS.items():
        print(f"  {name:<12} {config['description']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Project 01 checkpoint runner")
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
