## What changed and why

## Structural-edit checklist

(From [CONTRIBUTING.md](../CONTRIBUTING.md) — only applies if this PR adds, removes, or rewires
nodes; skip for prose-only fixes.)

- [ ] Required frontmatter present: `node`, `kind`, `label`, `inputs`, `basis`, `tags`.
- [ ] `kind` and `tags` agree (`kind: leaf` implies `tags: [dag/leaf]`, etc).
- [ ] Every `inputs` entry has a matching `[[wikilink]]` in `## Inputs`, and vice versa.
- [ ] No new orphaned `source` nodes (nothing lists it as an input).
- [ ] `{{PRODUCT_NAME}}` used instead of the literal product name anywhere it would otherwise
      appear.
- [ ] `## Inputs`/`## Reasoning` present or absent per
      [ARCHITECTURE.md § Section-presence convention](../ARCHITECTURE.md#section-presence-convention).
- [ ] `scripts/validate-vault.sh` passes locally.
