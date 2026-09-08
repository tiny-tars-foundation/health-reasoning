# Architecture

This file specifies health-reasoning's contract precisely — it does not teach. If you're making
your first edit, go to [START-HERE.md](START-HERE.md) instead; come back here when you need the
exact schema, a lint rule's meaning, or a hazard to avoid. Nothing here is explained a second time
in README.md or START-HERE.md — they link back to this file instead of restating it.

## Purpose and scope

health-reasoning holds the vault-authored reasoning behind one or more "brains" — dependency
graphs consumed by a private health-literacy app via an external pull/push pipeline (see Sync
hazards, below). This file
specifies: the schema every node file must satisfy, the lint rules validate-vault.sh runs and what
each means, the conventions that hold across every node in practice, and the hazards of the sync
relationship. It does not specify the pipeline's implementation, the lint engine's implementation,
or the expert-review process — see Out of scope, below.

There is one brain today (finding-dag/) and everything below is written over "a brain" in the
abstract, not finding-dag specifically — the schema and lint rules are engine-level
(@pablotech/neuro-pil), so this file is the contract for every brain this repo will ever hold. A
second brain does not get, or need, its own copy of this document.

## Vault structure

- One top-level folder per brain (e.g. finding-dag/). Each is independently openable as an
  Obsidian vault.
- One .md file per graph node, named for its node key (e.g. aiFindings.md holds the
  aiFindings node).
- One .obsidian/ folder per brain, holding that brain's Obsidian config — see
  Obsidian config contract, below.

## Frontmatter schema

Every node file opens with YAML frontmatter:

| Key | Type | Required | Meaning |
|---|---|---|---|
| node | string | always | The node's key. Matches the filename (minus .md) and every place this node is referenced from another node's inputs. |
| kind | source, derived, leaf, or projection | always | The node's role. source: no inputs, raw data supplied by the person the reasoning is about. derived: synthesizes other nodes into a new judgment. leaf: a final output surfaced to the app. projection: a cross-cutting view recombining existing nodes along a different axis (e.g. markerGroups regroups findings by body system rather than by derivation order). |
| label | string | always | Human-readable display name. May contain the PRODUCT_NAME placeholder (see below). |
| inputs | string array | always | The node keys this node depends on. Empty for source nodes. Must exactly match the wikilinks in the body's Inputs section. |
| basis | string | always | One-line summary of what the node represents. May contain the PRODUCT_NAME placeholder. |
| tags | one dag/kind tag | always | Mirrors kind as a tag, so Obsidian's Graph View can filter/color by it. Always exactly one tag, always dag/ plus the kind value. |
| note | true | only on note-input sources | See Conditional keys, below. |
| noteSink | true | only on the one node note inputs may feed | See Conditional keys, below. |

## Conditional keys

Two node files in finding-dag/ carry a 7th frontmatter key beyond the six above, encoding a rule
the lint engine enforces but that appears nowhere else in this repo:

- note: true marks a source node as holding a person's free-text (today: pursuedNotes).
- noteSink: true marks the one node allowed to consume a note-tagged node as an input
  (today: noteResults).
- The rule: a note-tagged node's content may only feed a noteSink-tagged node. Wiring a
  note node into any other node's inputs fails lint with note-feeds-non-sink — see Lint
  rules, below. The rule exists because a person's free-text note is meant to be triaged through
  exactly one purpose-built node, never blended silently into an unrelated one.
- If a future brain needs more than one note/sink pair, or a note feeding more than one sink, that
  is a real schema question to raise before adding it — this section states today's rule, not a
  ceiling on the engine.

## Section-presence convention

- All 15 `source`-kind nodes have `inputs: []` and omit both `## Inputs` and `## Reasoning` — a
  source node has nothing to derive from and nothing to explain the derivation of.
- Every `derived`, `leaf`, and `projection` node has a `## Inputs` section (wikilinks matching
  `inputs:`).
- Almost every `derived`/`leaf`/`projection` node also has a `## Reasoning` section — the actual
  expert judgment prose synced into the app's prompt. The one exception in `finding-dag/` today
  is `markerLevels`: it has `## Inputs` but no `## Reasoning`, because its `basis` ("Lab data with
  {{PRODUCT_NAME}}-inferred personalized levels") already fully describes a mechanical range lookup
  with no separate judgment call to spell out in prose. **The rule, precisely**: `## Reasoning` is
  present whenever there is expert judgment beyond what `basis` already states — not "always
  present on non-source nodes."

## The PRODUCT_NAME placeholder

`label`, `basis`, and `## Reasoning` prose may contain the literal string `{{PRODUCT_NAME}}` in
place of the private app's product name. This repo must never name that product directly (see
README.md). A downstream export step substitutes the real name when this vault is synced into the
app; here, in the vault, the placeholder is what should appear in any new prose. Currently used in
13 of `finding-dag/`'s 36 node files — reach for it whenever an edit would otherwise need to name
the product.

## Lint rules

`scripts/validate-vault.sh` runs `@pablotech/neuro-pil`'s `validate()` — the checks below, in
plain language, with what would trigger each:

| Rule | Meaning | Example that triggers it |
|---|---|---|
| `duplicate-key` | Two node files declare the same `node` key. | Copy-pasting a file and forgetting to change `node:`. |
| `unknown-input` | An `inputs` entry (or `[[wikilink]]`) names a node key that doesn't exist. | A typo in an input name, or deleting a node without updating what referenced it. |
| `source-has-inputs` | A `kind: source` node has a non-empty `inputs`. | Adding an input to a node that should instead become `kind: derived`. |
| `cycle` | The `inputs` graph has a cycle. | Node A lists B as an input, and B (directly or transitively) lists A. |
| `orphan` | A `kind: source` node has zero consumers — nothing lists it as an input. | Adding a source node and forgetting to wire any other node to depend on it. Does not fire for non-source kinds. |
| `note-feeds-non-sink` | A `note: true` node feeds a node that isn't `noteSink: true`. | See § Conditional keys. |

One additional rule, `missing-slice`, exists in the engine but is host-only — it never runs via
`validate-vault.sh` and is not a check this repo's contributors need to satisfy.

## What lint cannot check

`validate-vault.sh` checks graph *shape* only: unknown references, cycles, orphans, the
`note`/`noteSink` rule. It has no mechanism — and was never intended to have one — for judging
whether the reasoning prose in a `## Reasoning` section is medically sound, current, complete, or
safe. **A green `validate-vault.sh` run means the graph is well-formed. It is never evidence that
the reasoning has been expert-reviewed.** These are two separate gates (see also
[CONTRIBUTING.md](CONTRIBUTING.md), which states this as one of its two review gates) and neither
substitutes for the other. Treat any claim that "lint passed, so this is fine" as incomplete on its
face.

## Sync hazards

An external pipeline (outside this repo) pulls this vault to regenerate the app's copy of the
graph, and a corresponding push operation seeds or updates this vault from the app's side. The
hazard that matters here: the push direction **owns its target brain folder and overwrites it
destructively** — it deletes and regenerates every node file in the folder from scratch. It writes
only generated node `.md` files; it does not know about, and will silently delete, anything else
placed inside a brain folder (a scratch file, a draft, a note-to-self).

**Mitigation**: never hand-add a non-node file inside a brain folder. Keep drafts and scratch
content entirely outside `finding-dag/` (or any other brain folder) — the repo root, an unrelated
folder, anywhere the push operation doesn't own. Git history is the only recovery path if this is
violated, and only for what was actually committed before the next push.

## Obsidian config contract

Each brain folder's `.obsidian/` carries two categories of file:

- **Committed** (`app.json`, `appearance.json`, `core-plugins.json`, `graph.json`): a shared,
  brain-agnostic starter config — Graph View pre-colored by the four `dag/<kind>` tags, arrows
  enabled, `alwaysUpdateLinks` on so renaming a node file doesn't silently break its wikilinks.
  Nothing in these four files names a specific brain, so the same four files are what
  [CONTRIBUTING.md § Adding a brain](CONTRIBUTING.md#adding-a-brain) says to copy into any new
  brain folder unchanged.
- **Gitignored, permanently, for every brain folder**: `workspace.json`, `workspace-mobile.json`,
  `plugins/` — per-user session/window state that was never meant to be shared and never will be.

The four committed files are a convenience, not a dependency: [START-HERE.md](START-HERE.md)'s
Track A spells out the same Graph View setup as real, standalone manual steps, so the tutorial
works identically from a bare clone with `.obsidian/` deleted.

## Out of scope

- The external pipeline's implementation (the app's own repo owns this).
- The lint engine's implementation (`@pablotech/neuro-pil`, developed in the public `pilos` repo).
- The expert-review process itself — who reviews, how, and what they're checking for is an
  organizational process, not something this repo can enforce technically. § What lint cannot
  check states the boundary; it does not define the process on the other side of it.
