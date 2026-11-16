"""Reproducible Monte Carlo estimate of P(heads)."""
from random import Random


def estimate_heads(n: int = 10000, seed: int = 42) -> float:
    if n <= 0:
        raise ValueError("n must be positive")
    rng = Random(seed)
    return sum(rng.random() < 0.5 for _ in range(n)) / n


if __name__ == "__main__":
    print(f"Estimated P(heads): {estimate_heads():.4f}")
