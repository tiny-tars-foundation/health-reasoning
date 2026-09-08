---
node: aiOnPlan
kind: leaf
label: "Plan Assessment"
inputs: [patientPlan, patientAssessment, markerLevels, aiFindings, hypothesisEvaluation]
basis: "{{PRODUCT_NAME}}'s read on the Patient Plan — per action and as a whole."
tags: [dag/leaf]
---

# Plan Assessment

{{PRODUCT_NAME}}'s read on the Patient Plan — per action and as a whole.

## Inputs

- [[patientPlan]]
- [[patientAssessment]]
- [[markerLevels]]
- [[aiFindings]]
- [[hypothesisEvaluation]]

## Reasoning

assessment: 1–2 sentences on THAT specific action — is it well-aimed, correctly timed, the right dose/agent, and specifically how it interacts with what the patient is ALREADY taking (treatmentHistory's currently-ongoing rows, identifiable by their [Since X] date tag with no closed end) — this action is one of the emerging additions being brought to bear alongside that existing regimen. Name synergy where it exists (complementary mechanisms, a cofactor pairing such as vitamin D3 with vitamin K2) and flag its absence or a conflict where one exists (redundant or conflicting mechanisms, a known interaction risk, or a fat-soluble vitamin/mineral being added without its usual cofactor already present in the ongoing list). Name the specific ongoing treatment(s) involved; do not force a mention when nothing relevant applies.
