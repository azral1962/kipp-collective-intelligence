import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "03-skills/python/PY-03-numerical-simulation/examples/coin_flip.py"
spec = importlib.util.spec_from_file_location("coin_flip", P)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def test_coin_flip_reproducible():
    assert module.estimate_heads(1000, seed=42) == module.estimate_heads(1000, seed=42)


def test_coin_flip_probability_reasonable():
    assert 0.45 < module.estimate_heads(10000, seed=42) < 0.55


def test_coin_flip_rejects_invalid_input():
    import pytest
    with pytest.raises(ValueError):
        module.estimate_heads(0)
