---
node: doctorConversation
kind: leaf
label: "Doctor Conversation"
inputs: [patientAssessment, markerLevels, patientHypothesis, aiFindings, aiHypothesis, hypothesisEvaluation]
basis: "Questions to raise, by disease group / decision."
tags: [dag/leaf]
---

# Doctor Conversation

Questions to raise, by disease group / decision.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[patientHypothesis]]
- [[aiFindings]]
- [[aiHypothesis]]
- [[hypothesisEvaluation]]

## Reasoning

For each finding-based entry:
    group: copy the corresponding disease entry's group string verbatim
      (e.g. "Cardiovascular Risk", "Hormonal / Endocrine").
    questions: an array of 2–4 short bullets, each phrased as a topic or
      question the patient should literally raise at their next
      appointment about THIS group. Conversational tone — write each as
      if the patient is reading it off a list. Each bullet 5–25 words.
      Within a group, questions may be about a finding itself, about
      ongoing treatment for that finding (drugs/supplements the patient
      currently takes), or about hypothetical/future treatment (something
      to consider adding or changing). Mix is fine — they should cover
      the patient's most useful angles for that area.

  For each decision-based entry (patient or AI):
    group: copy the intervention name verbatim from the corresponding
      decisions.patient or decisions.ai entry (e.g. "Testosterone
      Replacement Therapy", "Tesamorelin", "Statin or PCSK9 inhibitor").
    questions: an array of 2–4 short bullets phrased as topics or
      questions the patient should literally raise about THIS decision.
      These are ADDITIONAL questions specific to weighing the decision —
      they complement, not duplicate, the finding-based questions above.
      Pull directly from the pros/cons/alternatives/recommendation you
      wrote for that decision in the decisions section. Examples for TRT:
        "Ask if enclomiphene could raise Free T while preserving fertility
         before committing to TRT."
        "Discuss how E2 will be monitored and managed if we start TRT."
        "Ask whether targeting SHBG drivers (weight, sleep) could lift Free
         T enough without a prescription."
      Conversational tone, 5–25 words each, plain language.

      Avoid obscure clinical terminology (no "acromegaly", "subclinical
      hypothyroidism", "aromatization", "atherogenic dyslipidemia") — use
      plain language or commonly-known drug-class shorthand ("statin",
      "PCSK9", "GLP-1", "estrogen blocker", "TRT", marker names like
      "IGF-1" or "ApoB" are fine). Each bullet ties back to a specific
      finding or treatment item above — these are the patient's takeaways
      condensed, not new analysis.

      Good examples grouped under Cardiovascular Risk:
        "Discuss whether a statin or PCSK9 inhibitor would help bring
         ApoB to goal."
        "Ask whether the current ezetimibe dose should change given the
         residual ApoB gap."
      Good examples grouped under Hormonal / Endocrine:
        "Ask about high IGF-1 alongside low testosterone — does that
         pattern mean anything?"
        "Ask about the role an estrogen blocker could play if we start
         TRT."

      Do not include a closing summary bullet; each item should stand on
      its own. If an area genuinely has nothing to ask, you may emit a
      single screening-style question rather than padding.
