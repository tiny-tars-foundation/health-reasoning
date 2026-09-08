---
node: diseaseResults
kind: leaf
label: "Diagnosis Result"
inputs: [patientAssessment, markerLevels, diagnosedDisease, aiFindings]
basis: "{{PRODUCT_NAME}}'s response to each diagnosis on file, tagged to a body system."
tags: [dag/leaf]
---

# Diagnosis Result

{{PRODUCT_NAME}}'s response to each diagnosis on file, tagged to a body system.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[diagnosedDisease]]
- [[aiFindings]]

## Reasoning

result: 3–6 sentences of plain prose on what this diagnosis means for the patient going forward — how it relates to patterns already visible in their lab markers or disease findings, and what's reasonable to monitor or raise with a physician. Do not state any fact not present in diagnosedDisease above. Do not assert a NEW diagnosis beyond the one already on file.
