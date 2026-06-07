from __future__ import annotations

import pathlib


def test_repo_scaffold_exists():
    root = pathlib.Path(__file__).resolve().parents[1]

    required = [
        root / "README.md",
        root / "requirements.txt",
        root / "requirements-visuals.txt",
        root / "docs" / "roadmap.md",
        root / "docs" / "references.md",
        root / "docs" / "local_workflow.md",
        root / "docs" / "platform_notes.md",
        root / "docs" / "visualizations.md",
        root / "projects" / "00_bandits" / "README.md",
        root / "projects" / "08_puffer_tetris" / "README.md",
        root / "tests" / "00_bandits" / "test_incremental_average.py",
        root / "tests" / "00_bandits" / "test_argmax_tie_break.py",
        root / "tests" / "00_bandits" / "test_epsilon_greedy_action.py",
        root / "tests" / "08_puffer_tetris" / "test_make_puffer_env_runtime.py",
        root / "src" / "bellman2tetris" / "__init__.py",
        root / "src" / "bellman2tetris" / "project_00_bandits.py",
        root / "src" / "bellman2tetris" / "project_08_puffer_tetris.py",
        root / "project_00.py",
        root / "project_01.py",
        root / "src" / "bellman2tetris" / "visualize.py",
    ]

    missing = [path for path in required if not path.exists()]
    assert not missing, f"Missing scaffold files: {missing}"
