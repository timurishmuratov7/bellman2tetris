from __future__ import annotations

import random

from conftest import load_symbol


def test_argmax_tie_break_is_deterministic_for_seeded_rng():
    argmax_tie_break = load_symbol(
        "bellman2tetris.project_00_bandits", "argmax_tie_break"
    )

    first = argmax_tie_break([1.0, 5.0, 5.0, 2.0], random.Random(7))
    second = argmax_tie_break([1.0, 5.0, 5.0, 2.0], random.Random(7))

    assert first in {1, 2}
    assert first == second

