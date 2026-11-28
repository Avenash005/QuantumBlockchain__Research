"""Toy sampler for computational-basis outcomes of the Bell state |Phi+>.

For |Phi+> = (|00> + |11>) / sqrt(2), ideal computational-basis
measurements return 00 or 11 with equal probability.

This script samples that probability distribution. It does NOT simulate
quantum dynamics, physical hardware, or the measurement process itself.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter


def sample_bell_phi_plus(shots: int, seed: int | None = None) -> Counter[str]:
    """Return counts for ideal 00/11 measurements."""
    if shots <= 0:
        raise ValueError("shots must be a positive integer")

    rng = random.Random(seed)
    return Counter("00" if rng.random() < 0.5 else "11" for _ in range(shots))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sample ideal computational-basis outcomes of |Phi+>."
    )
    parser.add_argument("--shots", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    counts = sample_bell_phi_plus(args.shots, args.seed)
    print(f"Shots: {args.shots}")
    for outcome in ("00", "01", "10", "11"):
        count = counts.get(outcome, 0)
        print(f"{outcome}: {count:>6}  ({count / args.shots:.3f})")


if __name__ == "__main__":
    main()
