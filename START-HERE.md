# Start here

Two tracks, depending on why you're here. Neither requires writing code.

- **Track A — editing health reasoning.** You've been asked to add, review, or correct the
  reasoning behind a Finding. ~5 minutes to read, then hands-on in Obsidian.
- **Track B — wiring the pipeline, or adding a brain.** You're touching how this vault is
  validated, or scaffolding a new brain folder. ~10 minutes, hands-on in a terminal.

Read [README.md](README.md) first if you haven't — it says what this repo is and isn't. This file
is the tutorial; [ARCHITECTURE.md](ARCHITECTURE.md) is the exact contract — README teaches,
ARCHITECTURE specifies, and nothing is explained twice.

## Track A — editing health reasoning

### The scenario

Someone has asked you to review or extend the reasoning behind one Finding — say, how the app
decides a marker deserves a caveat, or what counts as a "favorable" trajectory in someone's own
results. That reasoning lives here, as prose in a markdown file, not in the app's code — turning a
person's lab data into something they can actually read and discuss with a physician is a
health-literacy problem, and the reasoning behind it deserves to be reviewed as plain-language
writing, not buried in application code.

### What's actually in this repo

- **One folder = one "brain"** — a named dependency graph. `finding-dag/` is the first.
- **One file = one graph node.** A node is one piece of reasoning: what it's derived from
  (`inputs`), and what it feeds forward.
- **Frontmatter is metadata** — `node`, `kind`, `label`, `inputs`, `basis`, `tags`, and two rarer
  keys (`note`, `noteSink`). Exact schema:
  [ARCHITECTURE.md § Frontmatter schema](ARCHITECTURE.md#frontmatter-schema).
- **`[[wikilinks]]` in a node's `## Inputs` section are real edges** — Obsidian draws them, and
  they must match the `inputs` list in frontmatter exactly (one of the things
  `validate-vault.sh` checks).
- **What this is not**: not the app, not code, no PHI, no credentials, and not a diagnostic tool
  itself — this vault is the health-literacy reasoning template behind one, never a substitute for
  a doctor. Nothing here ever touches a real person's data — the app's private repo owns that;
  this vault only owns the reasoning template every person's Finding is generated through.

### Glossary

| Term | Meaning | Detail |
|---|---|---|
| Node | One markdown file; one piece of reasoning | [ARCHITECTURE.md § Vault structure](ARCHITECTURE.md#vault-structure) |
| DAG / brain | The whole dependency graph a folder holds | [ARCHITECTURE.md § Purpose and scope](ARCHITECTURE.md#purpose-and-scope) |
| `kind` | `source` \| `derived` \| `leaf` \| `projection` — a node's role in the graph | [ARCHITECTURE.md § Frontmatter schema](ARCHITECTURE.md#frontmatter-schema) |
| Tag | `dag/<kind>` — mirrors `kind`, used for Obsidian's graph coloring | [ARCHITECTURE.md § Frontmatter schema](ARCHITECTURE.md#frontmatter-schema) |
| Wikilink | `[[nodeName]]` — an edge from this node to an input | This file, below |
| Lint | `validate-vault.sh`'s structural checks | [ARCHITECTURE.md § Lint rules](ARCHITECTURE.md#lint-rules) |

### Visualizing the graph in Obsidian

1. **Install [Obsidian](https://obsidian.md)** (free, desktop, macOS/Windows/Linux).
2. **Open the brain folder itself as the vault** — File → Open folder as vault → pick
   `finding-dag/` (not the `health-reasoning` repo root — the root holds multiple brains and isn't
   itself a vault).
3. **Open Graph View** — the graph icon in the left sidebar, or `Cmd/Ctrl+P` → "Open graph view."
   Because the vault root *is* the brain folder, every node already shown belongs to this brain —
   there is nothing else in the vault to filter out.
4. **Color by kind.** In the Graph View panel, open **Groups** and add one query per `kind`, each
   with its own color:
   - `tag:#dag/source`
   - `tag:#dag/derived`
   - `tag:#dag/leaf`
   - `tag:#dag/projection`

   This is a real, from-scratch setup — nothing here depends on Obsidian settings someone else
   saved. If this repo's `.obsidian/` template is present (see
   [ARCHITECTURE.md § Obsidian config contract](ARCHITECTURE.md#obsidian-config-contract)), these
   four groups are already there; the steps above are what to do from a bare clone, or if the
   config ever drifts.
5. **Turn on arrows** — Graph View → **Display** → "Show arrows." Needed for the next point.
6. **Read the arrow direction correctly.** Obsidian draws an arrow from the *linking* note to its
   *target*. A node's `## Inputs` section links it to its upstream sources — so the arrow points
   **from the node to what it depends on**, i.e. leaf → source. If you're used to reading a DAG
   top-down (sources at the top, arrows flowing down to outputs), this is the opposite direction.
   This is the single most common first-read confusion — use `kind`/tag color, not arrow direction,
   to tell which end is upstream.
7. **Local Graph before editing a node.** Open a node, then its Local Graph (sidebar icon), to see
   only its immediate neighbors — what it depends on and what depends on it — instead of the whole
   36-node graph.

### Making a structural edit

- **Add a node**: new `.md` file, frontmatter per
  [ARCHITECTURE.md § Frontmatter schema](ARCHITECTURE.md#frontmatter-schema), a `## Inputs` section
  whose wikilinks match `inputs:` exactly (omit both `## Inputs` and `## Reasoning` if
  `kind: source` — see
  [ARCHITECTURE.md § Section-presence convention](ARCHITECTURE.md#section-presence-convention)).
- **Add or remove an edge**: edit both the frontmatter `inputs:` array and the `## Inputs`
  wikilink list — they must agree.
- **Pick the right `kind`/`tags`**: `source` (no inputs), `derived` (synthesizes other nodes),
  `leaf` (a final output), `projection` (a cross-cutting view over existing nodes, like
  `markerGroups`). `tags:` is always `[dag/<kind>]`.

### Checking your edit

```
scripts/validate-vault.sh
```

Run from anywhere inside a clone of this repo. On failure, don't parse the CLI output alone — find
the rule name in [ARCHITECTURE.md § Lint rules](ARCHITECTURE.md#lint-rules) for what it means and a
worked example.

> **Passing lint is not the same as being expert-reviewed.** `validate-vault.sh` only checks
> that the *graph* is well-formed — no unknown inputs, no cycles, no orphaned nodes. It has no way
> to judge whether the reasoning *prose* is medically sound, current, or complete. A green
> `validate-vault.sh` run means "safe to sync"; it does not mean "medically sound." Full
> statement: [ARCHITECTURE.md § What lint cannot check](ARCHITECTURE.md#what-lint-cannot-check).

## Track B — wiring the pipeline, or adding a brain

### Breaking the vault on purpose

Clone the repo and run the clean baseline first:

```
$ scripts/validate-vault.sh
...
0 findings
```

Now sever a wikilink without touching the frontmatter it should match — open `aiFindings.md`,
delete `- [[markerLevels]]` from its `## Inputs` list, but leave `markerLevels` in the frontmatter
`inputs:` array:

```
$ scripts/validate-vault.sh
...
[unknown-input] aiFindings: inputs references "markerLevels", but no matching [[markerLevels]]
wikilink was found in the body
1 findings
```

Undo that, then break something subtler: `noteResults.md` carries `noteSink: true`; rewire a
non-`noteSink` node (say, `aiFindings.md`) to also list `pursuedNotes` (a `note: true` node) as an
input:

```
$ scripts/validate-vault.sh
...
[note-feeds-non-sink] aiFindings: node "pursuedNotes" is tagged note: true and may only feed a
noteSink node
1 findings
```

The first failure is an obvious graph-shape problem — anyone would notice a severed link. The
second is not: the graph is still acyclic and every input resolves; nothing *looks* wrong by eye.
It's a domain rule (a person's free-text note is meant to be triaged through exactly one
purpose-built node, never blended silently into an unrelated one) that exists nowhere in this repo
except [ARCHITECTURE.md § Conditional keys](ARCHITECTURE.md#conditional-keys) — which is exactly
why that section is documented locally instead of only in the engine's own docs.

Undo both changes before committing anything.

### Reading order

| Read | For |
|---|---|
| [README.md](README.md) | What this repo is, isn't, and where things live |
| [ARCHITECTURE.md](ARCHITECTURE.md) §§ Frontmatter schema, Lint rules, Sync hazards | The exact contract you're validating against or writing tooling around |
| [CONTRIBUTING.md](CONTRIBUTING.md) | The checklist and review process before a PR |

### Objection: why prose + a lint script, not real schema validation or types?

Because the people making structural edits are health-literacy experts working in Obsidian, not engineers in an
IDE — a TypeScript schema or a JSON-Schema validator would be correct but unusable by exactly the
people this repo exists to serve. This repo already made the same call once before: the app that
consumes this vault dropped its own guardrail wrapper in favor of depending on this vault directly
("the app depends on this vault, not the reverse"). `validate-vault.sh` checks the one thing a
machine actually can check — graph shape. Whether the reasoning is *correct* is checked by a human
expert reviewer, every time, with no tooling substitute — see
[ARCHITECTURE.md § What lint cannot check](ARCHITECTURE.md#what-lint-cannot-check). Conflating the
two is the one mistake this whole document structure exists to prevent.

### Adding a brain

Full recipe: [CONTRIBUTING.md § Adding a brain](CONTRIBUTING.md#adding-a-brain). In short: a
sibling top-level folder, its own independently-opened Obsidian vault, its own `.obsidian/` (copied
verbatim from the template — it's brain-agnostic, since every brain shares the same
`dag/source|derived|leaf|projection` tag vocabulary). There is deliberately no repo-root
unification of multiple brains into one vault — each brain stays fully self-contained, which is
what keeps adding a second brain a folder copy rather than a redesign (no cross-brain tag
collisions to manage, no filtering to get right, no risk of one brain's graph swamping another's in
a shared Graph View).
