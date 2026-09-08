---
node: criticalRatios
kind: derived
label: "Critical Ratios"
inputs: [labData, diagnosedDisease, aiFindings]
basis: "Meaningful marker ratios chosen from the challenges."
tags: [dag/derived]
---

# Critical Ratios

Meaningful marker ratios chosen from the challenges.

## Inputs

- [[labData]]
- [[diagnosedDisease]]
- [[aiFindings]]

## Reasoning

that matter for THIS patient's challenges — the relationships a clinician
  reads together rather than in isolation (e.g. Triglycerides : HDL for insulin
  resistance, Total cholesterol : HDL or ApoB : ApoA1 for atherogenic balance,
  Testosterone : Estradiol or DHEA-S : Cortisol for the endocrine axis, Omega
  ratios for inflammation).
