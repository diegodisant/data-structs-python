"""Generates the per-data-structure complexity comparison charts.

Every chart compares the current (as implemented) step cost of each operation
against the best achievable in-place step cost, on a log scale, using a
representative input size. Bars are annotated with their big-O labels.

Usage:
    python3 docs/generate_charts.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # pylint: disable=wrong-import-position
import numpy as np  # pylint: disable=wrong-import-position

CHARTS_DIR = Path(__file__).parent / "charts"

# Representative input sizes.
N = 1_000          # list / queue / stack / tree node count
V = 1_000          # graph nodes
E = 2_000          # graph edges
K = 1_000          # graph traverse path length
H = N              # degenerate tree height (sorted insertions)
LOG_N = 10         # log2(N)

CURRENT_COLOR = "#d64545"
IMPROVED_COLOR = "#3a9d5f"
BAR_HEIGHT = 0.38

# (operation, current steps, current label, improved steps, improved label)
CHART_DATA: dict[str, list[tuple[str, float, str, float, str]]] = {
  "single-linked-list": [
    ("insert",    1, "O(1)", 1, "O(1)"),
    ("delete",    N, "O(n)", N, "O(n)"),
    ("contains",  N, "O(n)", N, "O(n)"),
    ("is_empty",  1, "O(1)", 1, "O(1)"),
    ("calc_size", 1, "O(1)", 1, "O(1)"),
  ],
  "double-linked-list": [
    ("insert",          1, "O(1)",      1,     "O(1)"),
    ("delete",          N, "O(n)",      N,     "O(n)"),
    ("contains",        N, "O(n)",      N,     "O(n)"),
    ("parallel_search", N, "O(n) wall", N / 2, "O(n/2) wall"),
    ("is_empty",        1, "O(1)",      1,     "O(1)"),
    ("calc_size",       1, "O(1)",      1,     "O(1)"),
  ],
  "queue": [
    ("enqueue",   1, "O(1)", 1, "O(1)"),
    ("dequeue",   1, "O(1)", 1, "O(1)"),
    ("at_start",  1, "O(1)", 1, "O(1)"),
    ("at_end",    1, "O(1)", 1, "O(1)"),
    ("is_empty",  1, "O(1)", 1, "O(1)"),
    ("calc_size", 1, "O(1)", 1, "O(1)"),
  ],
  "stack": [
    ("push", 1, "O(1)", 1, "O(1)"),
    ("pop",  1, "O(1)", 1, "O(1)"),
  ],
  "binary-search-tree": [
    ("insert",     H, "O(n) worst", H, "O(n) worst"),
    ("traverse",   H, "O(h) spine", N, "O(n) full"),
    ("calc_size",  1, "O(1)",       1, "O(1)"),
    ("calc_depth", 1, "O(1)*",      1, "O(1)"),
  ],
  "graph": [
    ("add",                     1,     "O(1)",         1,     "O(1)"),
    ("get_unexistent_tags",     10,    "O(R)",         10,    "O(R)"),
    ("rel",                     10,    "O(R)",         10,    "O(R)"),
    ("traverse",                K * K, "O(k²)",        K,     "O(k)"),
    ("route",                   V * E, "O(V·E) worst", V + E, "O(V+E)"),
    ("get_next_unvisited_link", 2,     "O(deg)",       1,     "O(1) amort."),
    ("get_next_unvisited_node", V,     "O(V)",         1,     "O(1)"),
  ],
}

TITLES = {
  "single-linked-list": "Single Linked List",
  "double-linked-list": "Double Linked List",
  "queue": "Queue",
  "stack": "Stack",
  "binary-search-tree": "Binary Search Tree",
  "graph": "Graph",
}

SUBTITLES = {
  "single-linked-list": f"n = {N:,} nodes (insert prepends at head)",
  "double-linked-list": f"n = {N:,} nodes (header + tail, prev/next)",
  "queue": f"n = {N:,} elements (built on DoubleList)",
  "stack": f"n = {N:,} elements (built on SingleList)",
  "binary-search-tree": f"n = {N:,} nodes, h = height (degenerate: h = n)",
  "graph": f"V = {V:,} nodes, E = {E:,} edges, k = path length",
}


def annotate_bars(axis: plt.Axes, rect_group, labels: list[str]) -> None:
  for rect, text in zip(rect_group, labels):
    axis.text(rect.get_width() * 1.15, rect.get_y() + rect.get_height() / 2,
              text, va="center", fontsize=9)


def build_chart(slug: str, rows: list[tuple[str, float, str, float, str]]) -> None:
  operations = [row[0] for row in rows]
  series = [
    ([row[1] for row in rows], [row[2] for row in rows], -BAR_HEIGHT / 2,
     CURRENT_COLOR, "current implementation"),
    ([row[3] for row in rows], [row[4] for row in rows], BAR_HEIGHT / 2,
     IMPROVED_COLOR, "best in-place improvement"),
  ]

  y = np.arange(len(operations))

  fig, axis = plt.subplots(figsize=(11, max(3.2, 0.85 * len(operations) + 1.6)))

  for steps, labels, offset, color, label in series:
    axis.barh(y + offset, steps, BAR_HEIGHT, label=label, color=color)

  biggest = max(step for steps, _, _, _, _ in series for step in steps)
  axis.set_xlim(0.8, biggest * 3)
  axis.set_xscale("log")
  axis.invert_yaxis()
  axis.set_yticks(y, labels=operations)
  axis.set_xlabel("relative steps (log scale)")
  axis.set_title(TITLES[slug], fontsize=13, fontweight="bold", loc="left")
  axis.text(0.3, 1.02, SUBTITLES[slug], transform=axis.transAxes, fontsize=9, color="#555555")
  axis.grid(axis="x", which="both", alpha=0.25)
  axis.legend(loc="lower right", fontsize=9)

  for (_, labels, _, _, _), rect_group in zip(series, axis.containers):
    annotate_bars(axis, rect_group, labels)

  fig.tight_layout()
  fig.savefig(CHARTS_DIR / f"{slug}.png", dpi=150)
  plt.close(fig)


def main() -> None:
  CHARTS_DIR.mkdir(parents=True, exist_ok=True)

  for slug, rows in CHART_DATA.items():
    build_chart(slug, rows)
    print(f"generated {slug}.png")


if __name__ == "__main__":
  main()
