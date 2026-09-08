# Branding & positioning — health-reasoning

Every doc in this repo (README, START-HERE, ARCHITECTURE, CONTRIBUTING, CHANGELOG, the GitHub
repo description/topics) must never use "clinical" or "patient." Use "health" / "literacy" /
"expert" / "person" instead — e.g. "clinical reasoning" → "health reasoning", "clinical
review" → "expert review", "clinical experts" → "health-literacy experts", "a patient's" →
"a person's".

**Why:** Tiny Tars Foundation is a health-education charity pursuing DPGA certification and a
Google Ad Grant. "Clinical"/"patient" language risks a skimming reviewer bucketing this as a
hospital/research org (an excluded category) rather than a health-literacy nonprofit.

**Scope:** framing/positioning copy only. `finding-dag/*.md` node content and filenames are
data-model identifiers, not framing copy, and are out of scope — don't rename them chasing this
rule. (`clinicalSynthesis.md` was itself renamed to `healthSynthesis.md` — a deliberate
identifier-naming decision made separately from this wording ban, not an application of it; see
`CHANGELOG.md`.)

**Before claiming any review or authorship has happened** (e.g. "reviewed by health-literacy
experts"), verify it's actually true — check
`gh api repos/tinytars/reasoning/collaborators` and `.../invitations`
before asserting it in prose. The repo description once claimed content was "authored and
reviewed by clinical experts" with zero collaborators on the repo. Describe the repo as
*structured for* that review, not as having already received it, until it has.
