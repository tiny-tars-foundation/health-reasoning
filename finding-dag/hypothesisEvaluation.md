---
node: hypothesisEvaluation
kind: leaf
label: "Hypothesis Evaluation"
inputs: [patientAssessment, markerLevels, patientHypothesis, aiFindings, aiHypothesis]
basis: "{{PRODUCT_NAME}} pros/cons/alternatives/recommendation on each patient hypothesis (decisions.patient)."
tags: [dag/leaf]
---

# Hypothesis Evaluation

{{PRODUCT_NAME}} pros/cons/alternatives/recommendation on each patient hypothesis (decisions.patient).

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[patientHypothesis]]
- [[aiFindings]]
- [[aiHypothesis]]

## Reasoning

pros: 3–6 short bullets (≤30 words) tied to this patient's specific data (labs, age, symptoms, goals). cons: 3–6 short bullets (≤30 words) covering the risks/costs a thoughtful clinician would raise for THIS patient, adapted to the specific intervention. alternatives: 2–5 short bullets (≤40 words) naming other ways to pursue the same stated purpose, with a one-clause why. recommendation: 3–6 sentences of plain prose — should the patient pursue this, hold off, or pursue an alternative first, anchored to this patient's data, naming whether the data on file already gates action now or what specific step must come first. Use "consider", "discuss with the prescribing physician", "could be reasonable if" — never a hard directive. questions: 2–4 short bullets (5–25 words each), each phrased as a topic or question the patient should literally raise at their next appointment about THIS intervention — conversational, as if read off a list, pulled from the pros/cons/alternatives/recommendation you just wrote.
