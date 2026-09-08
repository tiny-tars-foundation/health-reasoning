---
node: familyResults
kind: leaf
label: "Family History Result"
inputs: [patientAssessment, markerLevels, patientFamilyHistory, aiFindings]
basis: "{{PRODUCT_NAME}}'s response to each family history entry, tagged to a body system."
tags: [dag/leaf]
---

# Family History Result

{{PRODUCT_NAME}}'s response to each family history entry, tagged to a body system.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[patientFamilyHistory]]
- [[aiFindings]]

## Reasoning

result: 3–6 sentences of plain prose on what this family history means for the patient's own risk — whether it's consistent with, or a plausible contributor to, patterns already visible in their lab markers or disease findings, and what's reasonable to monitor or raise with a physician given the stated relation and condition. Do not state any fact not present in patientFamilyHistory above. Never assert a diagnosis or a genetic conclusion the data doesn't support — use language like "may modestly raise", "worth monitoring", "consistent with".
