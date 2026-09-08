# Changelog

All notable changes are documented here, by hand, one entry per version — not generated from
commit history. See [`CONTRIBUTING.md § Versioning`](CONTRIBUTING.md#versioning) for why: a
version entry records *why* something changed, which a commit log can't reconstruct for a future
non-engineer reader.

## [0.1.12] - 2026-09-06

Initial commit.

Tiny Tars Foundation's health-literacy reasoning content, framed as a Sovereign Health
Literacy / Digital Public Good. Docs avoid "clinical"/"patient" language (using "health" /
"literacy" / "expert" / "person" instead) since that wording risks a Google Ad Grant or DPGA
reviewer bucketing this as a hospital/research org — an excluded category — rather than the
health-education charity it is; see `CLAUDE.md` for the full rule and its scope.

`finding-dag/` holds one file per DAG reasoning node (frontmatter: `node`, `kind`, `label`,
`inputs`, `basis`, `tags`), validated by `scripts/validate-vault.sh` and diagrammed into
`docs/graph-view.svg` by `scripts/gen-graph-view.py`.

`.github/workflows/ci.yml` validates every brain and auto-bumps/tags/releases on push to `main`.
