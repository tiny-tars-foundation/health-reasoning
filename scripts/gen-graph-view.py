#!/usr/bin/env python3
"""Regenerate docs/graph-view.svg from finding-dag/*.md frontmatter.

Stdlib-only (no package.json in this repo, by design) — parses the flat
YAML-ish frontmatter directly rather than pulling in a YAML dependency.
"""

import math
import random
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DAG_DIR = REPO_ROOT / "finding-dag"
OUT_PATH = REPO_ROOT / "docs" / "graph-view.svg"

KIND_COLOR = {
    "source": "#2563eb",
    "derived": "#d97706",
    "leaf": "#059669",
    "projection": "#7c3aed",
}
KIND_ORDER = ["source", "derived", "leaf", "projection"]


def parse_frontmatter(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: no frontmatter block")
    fields = {}
    for line in m.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def parse_inputs(raw):
    raw = raw.strip()
    if not raw.startswith("[") or not raw.endswith("]"):
        raise ValueError(f"unexpected inputs format: {raw!r}")
    inner = raw[1:-1].strip()
    if not inner:
        return []
    return [item.strip() for item in inner.split(",")]


def load_nodes():
    nodes = {}
    for path in sorted(DAG_DIR.glob("*.md")):
        fields = parse_frontmatter(path)
        node_id = fields["node"]
        nodes[node_id] = {
            "kind": fields["kind"],
            "label": fields["label"].strip('"'),
            "inputs": parse_inputs(fields["inputs"]),
        }
    return nodes


def build_edges(nodes):
    # An edge from each of a node's inputs *to* that node (data flows into it).
    return [(src, dst) for dst, data in nodes.items() for src in data["inputs"]]


def layout(nodes, edges, width, height, seed=42, iterations=400):
    rng = random.Random(seed)
    ids = list(nodes)
    pos = {
        n: (
            width / 2 + rng.uniform(-width / 3, width / 3),
            height / 2 + rng.uniform(-height / 3, height / 3),
        )
        for n in ids
    }
    area = width * height
    k = math.sqrt(area / max(len(ids), 1)) * 0.9
    t = width / 10  # initial "temperature" (max displacement per step)
    cooling = t / iterations

    for _ in range(iterations):
        disp = {n: [0.0, 0.0] for n in ids}

        for i, a in enumerate(ids):
            ax, ay = pos[a]
            for b in ids[i + 1 :]:
                bx, by = pos[b]
                dx, dy = ax - bx, ay - by
                dist = math.hypot(dx, dy) or 0.01
                force = k * k / dist
                fx, fy = dx / dist * force, dy / dist * force
                disp[a][0] += fx
                disp[a][1] += fy
                disp[b][0] -= fx
                disp[b][1] -= fy

        for src, dst in edges:
            ax, ay = pos[src]
            bx, by = pos[dst]
            dx, dy = ax - bx, ay - by
            dist = math.hypot(dx, dy) or 0.01
            force = dist * dist / k
            fx, fy = dx / dist * force, dy / dist * force
            disp[src][0] -= fx
            disp[src][1] -= fy
            disp[dst][0] += fx
            disp[dst][1] += fy

        for n in ids:
            dx, dy = disp[n]
            dist = math.hypot(dx, dy) or 0.01
            capped = min(dist, t)
            x, y = pos[n]
            x += dx / dist * capped
            y += dy / dist * capped
            margin = 60
            x = min(width - margin, max(margin, x))
            y = min(height - margin, max(margin, y))
            pos[n] = (x, y)

        t -= cooling

    return pos


def render_svg(nodes, edges, pos, width, height):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'font-family="Helvetica, Arial, sans-serif">',
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
    ]

    for src, dst in edges:
        x1, y1 = pos[src]
        x2, y2 = pos[dst]
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#cbd5e1" stroke-width="1"/>'
        )

    radius = 7
    for node_id, data in nodes.items():
        x, y = pos[node_id]
        color = KIND_COLOR[data["kind"]]
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{color}"/>')
        parts.append(
            f'<text x="{x + radius + 4:.1f}" y="{y + 3:.1f}" font-size="10" fill="#1f2937">'
            f"{node_id}</text>"
        )

    legend_x, legend_y = 20, height - 20 - 18 * len(KIND_ORDER)
    parts.append(
        f'<text x="{legend_x}" y="{legend_y - 12}" font-size="12" font-weight="bold" '
        f'fill="#1f2937">kind</text>'
    )
    for i, kind in enumerate(KIND_ORDER):
        y = legend_y + i * 18
        parts.append(
            f'<circle cx="{legend_x + 6}" cy="{y}" r="6" fill="{KIND_COLOR[kind]}"/>'
        )
        parts.append(
            f'<text x="{legend_x + 18}" y="{y + 4}" font-size="12" fill="#1f2937">{kind}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


def main():
    nodes = load_nodes()
    edges = build_edges(nodes)
    width, height = 1200, 900
    pos = layout(nodes, edges, width, height)
    svg = render_svg(nodes, edges, pos, width, height)
    OUT_PATH.write_text(svg + "\n")
    print(f"wrote {OUT_PATH} ({len(nodes)} nodes, {len(edges)} edges)", file=sys.stderr)


if __name__ == "__main__":
    main()
