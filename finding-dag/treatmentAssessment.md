---
node: treatmentAssessment
kind: leaf
label: "Treatment Assessment"
inputs: [patientAssessment, markerLevels, treatmentHistory, aiFindings]
basis: "{{PRODUCT_NAME}} assessment of each current regimen item, tagged to a body system (W25)."
tags: [dag/leaf]
---

# Treatment Assessment

{{PRODUCT_NAME}} assessment of each current regimen item, tagged to a body system (W25).

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[treatmentHistory]]
- [[aiFindings]]

## Reasoning

assessment: 2–4 sentences of plain prose. Apply the DATE AWARENESS rule FIRST: locate the item's most recent `since` date, locate the latest reading for the marker(s) it targets, and only attribute effects when the reading post-dates `since` by enough time for the effect to manifest. State whether the item appears to be producing the expected effect on the marker(s) it targets, citing the progression data (e.g. "the GLP-1 has pulled HbA1c from 6.4 to 5.7", "ezetimibe has only partly closed the ApoB gap — still 76 against a <60 target"). When the drug has been titrated (multiple rows for the same name), describe the dose trajectory in one short clause and tie it to the marker response ONLY for readings drawn AFTER the most recent dose change ("micronized progesterone was raised from 10 mg to 15 mg in 2025-09; sleep quality and morning cortisol have..."). When the most recent dose change post-dates the latest reading, say so plainly instead of inventing an effect: "the increase from 10 mg to 15 mg on 2026-06-01 has not been re-tested yet — the latest DHEA-S reading is from 2026-05-15 and cannot reflect the new dose; recheck in 8–12 weeks". When the item is producing the expected effect, say so plainly. When it is not, name the gap and, if warranted, propose a specific addition or class change to discuss with the physician ("consider layering a PCSK9 inhibitor"), tied to a specific marker or finding above. Do not pad. PRODUCT DATA. A treatment may carry `description`, `ingredients` and `links` describing the PRODUCT. Use them to ground your clinical reasoning — NEVER to restate what the product is. Composition, maker, description, and administration timing are already shown verbatim on the treatment's own product card; opening an assessment with something like "X contains Y mg of Z and has been taken since [date]" is a restatement, not an assessment, and confuses what the product is with when it was taken. Every sentence must be a clinical read — an effect, a gap, an absorption/timing note, or an interaction — not a label recap. For a formulated supplement the ingredient list IS the clinical content — the brand name ("Thyroid Support") tells you nothing on its own — but use that content to reason, not to introduce the product. Two rules govern it. First, an `amount`/`unit` on an ingredient is a LABEL FACT — what one capsule or serving contains — and is NEVER the patient's dose; the patient's dose is the row's own dose fields, and conflating the two would misreport what the patient actually takes. Combine them only while saying plainly that you are doing so. Second, a `link` is a reference you have NOT read: cite it by its label if useful, never claim to know its contents. Where several concurrent items carry ingredients, compare the SETS: name a cofactor a product lacks that its own active needs (e.g. vitamin D3 with no matching K2), and name an ingredient the patient receives from more than one product at once. In addition to the marker-response read above, when known, also comment on: (1) the active ingredient(s) for a recognizable brand name or compound (e.g. "Lipitor" → atorvastatin) — only state this with confidence, otherwise omit; (2) the best-known administration timing or method for how it should be taken, when established (e.g. fat-soluble vitamins/statins absorb better with a fatty meal; some thyroid/bisphosphonate drugs require an empty stomach). For a planned or ongoing item, state this as actionable guidance — when the patient should start observing it, or should already be observing it. For a past item, omit this unless it's needed to explain why an expected effect didn't materialize; (3) whether the recorded `reason` for starting the item is consistent with what it's typically prescribed/taken for, noting a mismatch if one exists; (4) brief clinical commentary on whether the recorded dose looks appropriate for the indication — NEVER replace, round, or guess a different dose; only comment on the appropriateness of the dose exactly as recorded. Skip any of (1)-(4) you aren't confident about rather than speculating.
