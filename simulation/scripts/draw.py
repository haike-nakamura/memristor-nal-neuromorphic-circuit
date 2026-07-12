"""Plot PSpice exported CSV waveforms.

Usage (from repo root):
    python simulation/scripts/draw.py
    python simulation/scripts/draw.py --csv simulation/data/yeharm.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CSV = ROOT / "simulation" / "data" / "yeharm.csv"

plt.rcParams.update(
    {
        "font.size": 14,
        "axes.labelsize": 14,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
    }
)


def plot_yeharm(csv_path: Path) -> None:
    df = pd.read_csv(csv_path, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    time = df["Time"]
    v_vr = df["V(VR3)"]
    v_vm = df["V(VM3)"]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(time, v_vr, color="#1E90FF", linewidth=1.5)
    ax1.set_ylabel("V(VR3) (V)")
    ax1.grid(True, linestyle="--", alpha=0.7)

    ax2.plot(time, v_vm, color="#1E90FF", linewidth=1.5)
    ax2.set_ylabel("V(VM3) (V)")
    ax2.set_xlabel("Time (s)")
    ax2.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description="Plot PSpice CSV exports")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="CSV file path")
    args = parser.parse_args()
    plot_yeharm(args.csv)


if __name__ == "__main__":
    main()
