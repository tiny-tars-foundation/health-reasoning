---
node: treatmentGroups
kind: leaf
label: "Treatment Groups"
inputs: [patientHypothesis, patientPlan, aiHypothesis, aiFindings]
basis: "Patient ↔ {{PRODUCT_NAME}} treatments partitioned by body system then drug class."
tags: [dag/leaf]
---

# Treatment Groups

Patient ↔ {{PRODUCT_NAME}} treatments partitioned by body system then drug class.

## Inputs

- [[patientHypothesis]]
- [[patientPlan]]
- [[aiHypothesis]]
- [[aiFindings]]

## Reasoning

the patient's view beside the AI's — so a doctor can see where they agree, differ, or have no counterpart.
