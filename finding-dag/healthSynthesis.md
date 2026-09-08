---
node: healthSynthesis
kind: derived
label: "Health Synthesis"
inputs: [diagnosedDisease, aiFindings, markerLevels, treatmentHistory]
basis: "Two-track adverse vs favorable trajectory synthesis."
tags: [dag/derived]
---

# Health Synthesis

Two-track adverse vs favorable trajectory synthesis.

## Inputs

- [[diagnosedDisease]]
- [[aiFindings]]
- [[markerLevels]]
- [[treatmentHistory]]

## Reasoning

This is the two-track TRAJECTORY narrative a
  clinician delivers — it SYNTHESIZES across findings already established
  elsewhere in this report (Diagnosed Disease, Health Finding, the handed
  marker deltas, Treatment History). It does NOT diagnose: introduce no new
  disease claim or alarm that those sections do not already support.
    VERBATIM ANCHORING (applies to adverse, favorable, and conditioning):
    whenever you state a change, comparison, or delta, quote the source's
    EXACT descriptor for BOTH endpoints in double quotes, word-for-word from
    the Diagnosed Disease summary or the marker reading it came from — e.g.
      "left atrial volume index 29 mL/m²" (2019) → "Moderately dilated left
      atrium, volume index 43 mL/m²" (2024)
    — and only THEN, if useful, add the derived figure ("a ~14 mL/m²
    increase"). Never lead with a derived number (an absolute change, a
    percent, a span) without the two quoted endpoints behind it; the reader
    must be able to find each quoted phrase verbatim in the source report.
    Do not invent or round a descriptor the source does not contain.
    adverse: 3–6 sentences on the forces working AGAINST the patient — the
      structural, heritable, or age-clock findings the patient cannot
      lifestyle their way out of (e.g. a rising CAC score, an enlarging
      aortic root, a coded comorbidity). Cite the specific datum behind each
      claim (a delta with its dates, a structural finding, an ICD
      comorbidity).
    favorable: 3–6 sentences on the gains working IN THE PATIENT'S FAVOR —
      the lifestyle- and treatment-driven improvements the data shows. Cite
      the specific marker delta or treatment response behind each, and honor
      DATE AWARENESS: only credit a treatment with a gain when the improving
      reading post-dates that treatment's start.
    conditioning: an OPTIONAL qualitative biological-vs-chronological read
      (a "conditioning" / loose heart-age-style observation), included ONLY
      where the data genuinely supports one. It must be explicitly
      qualitative and hedged — NEVER state a computed "biological age = N"
      as a clinical fact. If the data does not support such a read, return
      an EMPTY STRING "".
    If one track is genuinely thin, keep it short and honest — do NOT invent
    a counterweight to balance the other. adverse and favorable are always
    required.
