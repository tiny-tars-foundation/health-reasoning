---
node: allergyResults
kind: leaf
label: "Allergy Result"
inputs: [patientAssessment, markerLevels, patientAllergies, aiFindings]
basis: "{{PRODUCT_NAME}}'s response to each known allergy, tagged to a body system."
tags: [dag/leaf]
---

# Allergy Result

{{PRODUCT_NAME}}'s response to each known allergy, tagged to a body system.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[patientAllergies]]
- [[aiFindings]]

## Reasoning

result: 3–6 sentences of plain prose on the allergy and reaction itself — what standing precaution the severity (mild/moderate/severe) and reaction described actually warrant (e.g. a severe/anaphylactic reaction warrants carrying rescue medication; a mild seasonal reaction does not), and any well-established, DIRECT clinical fact about that specific allergen worth knowing (e.g. a real cross-reactivity class, a genuinely common misconception worth correcting). Do not speculate about hypothetical future prescriptions, procedures, or supplements the patient has not been shown to be taking or considering — only connect to markerLevels/aiFindings above when the link is concrete and direct, not a hypothetical "if X is ever started" aside. Do not state any fact (onset date, prior testing, etc.) not present in patientAllergies above. Never assert a diagnosis.
