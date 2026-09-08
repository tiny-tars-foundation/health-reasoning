---
node: noteResults
kind: leaf
label: "Note Result"
inputs: [patientAssessment, markerLevels, pursuedNotes, aiFindings]
basis: "{{PRODUCT_NAME}}'s response to each note, tagged to a body system."
tags: [dag/leaf]
noteSink: true
---

# Note Result

{{PRODUCT_NAME}}'s response to each note, tagged to a body system.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[pursuedNotes]]
- [[aiFindings]]

## Reasoning

result: 3–6 sentences of plain prose responding to what the patient jotted down — surface anything it connects to that is clinically relevant (a marker, a treatment, a disease finding), or say plainly if the note does not raise a clinical question. Apply the DATE AWARENESS rule before crediting any treatment effect. Never assert a diagnosis.
