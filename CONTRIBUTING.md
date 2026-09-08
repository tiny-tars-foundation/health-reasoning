# Contributing

This repo is where the plain-language reasoning behind Tiny Tars Foundation's health-literacy
tools gets written and reviewed — not where its application code lives.

## Who edits here

Health-literacy experts have full structural authority over node content — add, remove, or rewire nodes,
not just fix prose on ones that already exist. Engineers contribute when wiring the sync pipeline
or scaffolding a new brain folder. Neither role needs to write application code to work in this
repo.

## Before opening a PR

```
scripts/validate-vault.sh
```

If it fails, don't work from the CLI output alone — look up the failing rule in
[ARCHITECTURE.md § Lint rules](ARCHITECTURE.md#lint-rules) for its plain-language meaning and a
worked example.

## Structural-edit checklist

- [ ] Required frontmatter present: `node`, `kind`, `label`, `inputs`, `basis`, `tags`.
- [ ] `kind` and `tags` agree (`kind: leaf` implies `tags: [dag/leaf]`, etc).
- [ ] Every `inputs` entry has a matching `[[wikilink]]` in `## Inputs`, and vice versa.
- [ ] No new orphaned `source` nodes (nothing lists it as an input).
- [ ] `{{PRODUCT_NAME}}` used instead of the literal product name anywhere it would otherwise
      appear.
- [ ] `## Inputs`/`## Reasoning` present or absent per
      [ARCHITECTURE.md § Section-presence convention](ARCHITECTURE.md#section-presence-convention).

## Adding a brain

The full, complete procedure — not a placeholder for later:

1. Create a sibling top-level folder named for the brain (e.g. `some-other-dag/`).
2. Populate it with node `.md` files following
   [ARCHITECTURE.md § Frontmatter schema](ARCHITECTURE.md#frontmatter-schema).
3. Copy the four `.obsidian/` starter files
   (`app.json`, `appearance.json`, `core-plugins.json`, `graph.json`) from an existing brain folder
   into the new one, verbatim — they're brain-agnostic (see
   [ARCHITECTURE.md § Obsidian config contract](ARCHITECTURE.md#obsidian-config-contract)), since
   every brain shares the same `dag/source|derived|leaf|projection` tag vocabulary. No per-brain
   authoring needed.
4. Run `scripts/validate-vault.sh <folder-name>` — the script already supports a folder argument
   (see its usage comment).
5. Add one line to [README.md](README.md)'s brain list.

That's the entire procedure — no other file needs to change. This repo does not unify multiple
brains into one shared vault; each stays fully self-contained, which is what keeps this a folder
copy rather than a restructure.

## Review heuristic

A PR that touches node files outside the brain it claims to change, or that rewrites many
`basis`/`## Reasoning` sections in one pass, is a scope-creep signal — flag it in review the same
way an unexpectedly wide diff would be flagged anywhere else.

## The two gates, by design

There is no automated test suite. CI (`.github/workflows/ci.yml`) runs `validate-vault.sh` against
every brain on push and PR, and handles releases (see [Versioning](#versioning) below) — but that's
automation of the one structural gate below, not a second one. Two gates stand in for a real test
suite, deliberately, and neither substitutes for the other:

1. **`validate-vault.sh`** — structural. Confirms the graph is well-formed.
2. **Human expert review** — semantic. Confirms the reasoning itself is sound. Nothing in this
   repo can check this automatically — see
   [ARCHITECTURE.md § What lint cannot check](ARCHITECTURE.md#what-lint-cannot-check).

A PR needs both. A green `validate-vault.sh` run is necessary, never sufficient.

## Versioning

Merging to `main` auto-bumps the patch version (`0.1.0` → `0.1.1`) and tags/releases it — CI's
`release` job in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) does this after
`validate-vault.sh` passes, and its own commit carries `[skip ci]` so it doesn't trigger itself
again. One `VERSION` file at the repo root holds a single number for the whole vault, shared
across every brain — the same way `pilos`'s two packages share one patch version rather than
versioning independently. Don't hand-edit `VERSION` for a patch bump — the automation owns patch.

A MINOR or MAJOR bump is still a human call: bump `VERSION` yourself in a PR when a change earns
one (a new brain, a schema change in [ARCHITECTURE.md](ARCHITECTURE.md)). A
[CHANGELOG.md](CHANGELOG.md) entry is the same kind of deliberate, human-written call — not every
patch bump gets one, only a release worth explaining.
