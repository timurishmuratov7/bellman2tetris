from __future__ import annotations

from conftest import load_symbol


BOARD = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
]


def test_extract_features_contains_core_keys():
    extract_features = load_symbol(
        "bellman2tetris.project_05_tetris_features", "extract_features"
    )

    features = extract_features(BOARD)

    assert features["column_heights"] == [2, 3, 0, 2]
    assert features["holes"] == 1
    assert features["bumpiness"] == 6
    assert features["full_rows"] == []

