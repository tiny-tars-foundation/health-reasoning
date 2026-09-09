---
node: studyResults
kind: leaf
label: "Study Result"
inputs: [patientAssessment, markerLevels, pursuedStudy, aiFindings]
basis: "{{PRODUCT_NAME}}'s answer to each pursued study, tagged to a body system."
tags: [dag/leaf]
---

# Study Result

{{PRODUCT_NAME}}'s answer to each pursued study, tagged to a body system.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[pursuedStudy]]
- [[aiFindings]]

## Reasoning

result: 4–7 sentences of plain prose answering what the patient's data actually says about THAT study line — what does the named investigation conclude? The study's focus label is only a short title, so OPEN by re-introducing the study in one sentence: restate, in plain language and grounded in THIS patient's assessment, what the study actually investigates and why it matters for them — never assume the reader recalls the scope. THEN lead with the plain-language answer and substantiate with the specific markers, trajectory, and treatment timing that support the verdict. Apply the DATE AWARENESS rule before crediting any treatment effect to a study line. Use "suggests", "consistent with", "the data does not yet support" — never assert a diagnosis.
