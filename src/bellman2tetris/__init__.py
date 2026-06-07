"""Handwritten RL implementations for the bellman2tetris curriculum.

Tracked starter files live in ``src/bellman2tetris/``.
Local-only overrides can live in ``.local/bellman2tetris/``.
If a module exists in both places, the local copy wins on that machine while
the tracked starter surface stays unchanged for everyone else.
"""

from __future__ import annotations

from pathlib import Path


_ROOT = Path(__file__).resolve().parents[2]
_LOCAL_PACKAGE = _ROOT / ".local" / "bellman2tetris"

if _LOCAL_PACKAGE.exists():
    local_package = str(_LOCAL_PACKAGE)
    if local_package not in __path__:
        __path__.insert(0, local_package)
