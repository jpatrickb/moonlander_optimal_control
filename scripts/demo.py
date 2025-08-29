#!/usr/bin/env python3
"""Run a baseline moonlander solve and save a figure.

Usage:
  python scripts/demo.py --out media/images/baseline.png --t-steps 400
"""
import argparse
from pathlib import Path
import sys

# Ensure local src/ is importable without installation
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from moonlander_optimal_control.solver import solve_baseline
from moonlander_optimal_control.plotting import plot_summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="media/images/baseline.png")
    parser.add_argument("--t-steps", type=int, default=400)
    args = parser.parse_args()

    pos = (5.0, 10.0)
    vx0 = 1.0

    t, x, y, xp, yp, ux, uy, tf = solve_baseline(pos, vx0, t_steps=args.t_steps)

    # Ensure output directory exists
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Plot and save
    plot_summary(t, x, y, xp, yp, ux, uy, tf)
    try:
        import matplotlib.pyplot as plt

        plt.savefig(out_path, dpi=200)
        print(f"Saved figure to {out_path}")
    except Exception as e:
        print(f"Could not save figure: {e}")


if __name__ == "__main__":
    main()

