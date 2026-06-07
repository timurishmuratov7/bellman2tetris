from __future__ import annotations

import importlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def load_symbol(module_name: str, symbol_name: str):
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        raise AssertionError(
            f"Create {module_name.replace('.', '/')}.py and define {symbol_name}."
        ) from exc

    if not hasattr(module, symbol_name):
        raise AssertionError(f"{module_name} is missing the symbol {symbol_name}.")

    return getattr(module, symbol_name)


def as_tuple_2d(value):
    if hasattr(value, "tolist"):
        value = value.tolist()
    return tuple(tuple(row) for row in value)


def as_tuple_1d(value):
    if hasattr(value, "tolist"):
        value = value.tolist()
    return tuple(value)

