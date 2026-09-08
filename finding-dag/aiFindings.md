---
node: aiFindings
kind: derived
label: "{{PRODUCT_NAME}} Findings (disease)"
inputs: [patientAssessment, markerLevels]
basis: "The per-system disease finding — the central synthesis."
tags: [dag/derived]
---

# {{PRODUCT_NAME}} Findings (disease)

The per-system disease finding — the central synthesis.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]

## Reasoning

ORDER the array by clinical severity, highest first. Severity reflects the
  strength of the finding(s) within that area: how far markers sit outside
  personalized targets, how strongly the pattern points to a real disease
  process vs an isolated value, and the magnitude of downstream risk (e.g.
  ASCVD, end-organ damage, mortality contribution). Areas with no finding
  identified sort to the bottom.

  Within the same severity tier, order acute before chronic — i.e. areas
  where the picture is actively deteriorating or recently flipped out of
  range come before areas where the abnormality has been stable for years.
  An area with a sharp recent change beats an area with a long-standing
  drift at the same severity level.

  For each entry:
    group: the category name as above.
    finding: 3–6 sentences of plain prose. The focus of this section is the
      patient's HEALTH — what their situation actually means for them as a
      person — not a list of marker values. Lead with the lay meaning, then
      substantiate with metrics.

      Sentence 1 (and possibly 2) should explain in plain language what is
      happening to the patient's body and what it means for them in
      everyday terms — the kind of explanation a smart non-clinician would
      take away from a good doctor visit. Examples: "Your cholesterol-
      carrying particles are still loading the walls of your arteries faster
      than your body clears them — exactly the long-running process behind
      most heart attacks and strokes." Or: "Your testosterone is sitting at
      the low end of a young man's range, which fits the low energy and
      slow recovery you described." Make the meaning vivid and concrete.

      THEN substantiate with the specifics — name the suspected pattern
      (e.g. "atherogenic dyslipidemia", "subclinical hypothyroidism",
      "insulin resistance") and cite the markers, symptoms, or suspicion
      that support it (e.g. "ApoB 76 against a <60 target", "free T 62
      pg/mL against an 80–150 target"). When you use a technical phrase
      like "still atherogenic" or "baseline but still atherogenic", pair
      it immediately with the plain-language meaning ("still atherogenic —
      the particles in your blood are still in the size and number range
      that drives plaque buildup"). Be precise about what the technical
      term means; do not leave it floating.

      Use "suggests", "consistent with", "raises the possibility of" —
      never assert a diagnosis.

      If the data for this area shows no concern, do NOT omit the area —
      lead with plain-language reassurance and substantiate. Example: "The
      filtering work your kidneys do is on track for your age and body
      type. No finding identified — eGFR, creatinine, and BUN all sit
      within their personalized targets." Or for an untracked area: "We
      have no way to read this picture right now because the relevant labs
      have not been drawn. No finding identified — no inflammatory markers
      (hsCRP, ESR) are currently tracked." A short "no finding" entry is
      fine; do not pad.
