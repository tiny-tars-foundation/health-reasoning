---
node: aiHypothesis
kind: derived
label: "{{PRODUCT_NAME}} Hypothesis (alternatives)"
inputs: [patientAssessment, markerLevels, aiFindings]
basis: "{{PRODUCT_NAME}}'s own proposed intervention set (decisions.ai)."
tags: [dag/derived]
---

# {{PRODUCT_NAME}} Hypothesis (alternatives)

{{PRODUCT_NAME}}'s own proposed intervention set (decisions.ai).

## Inputs

- [[patientAssessment]]
- [[markerLevels]]
- [[aiFindings]]

## Reasoning

decisions.ai: the COLLECTIVE, COMPLETE set of specific interventions
  the Finding implies for this patient — the AI's own full recommended
  Rx/procedure plan, NOT just net-new deltas. Include an entry EVEN IF
  the patient already lists it under their Hypothesis or Plan, or is
  already taking it; the value is a precise, complete recommendation set.
  Constrain to SPECIFIC PRESCRIPTION MEDICATIONS, named evidence-based
  supplements with a clear mechanistic role (e.g. methyl-B12 /
  L-methylfolate for elevated homocysteine with low or low-normal B12),
  or named Rx-equivalent procedures. Exclude generic lifestyle advice
  (diet, sleep, exercise, weight loss) and vague "supplements".
  decisions.ai is for THERAPEUTIC interventions ONLY. NEVER put a
  diagnostic test, lab draw, imaging study, panel, or screening here
  (e.g. an hsCRP or Lipoprotein(a) measurement, a repeat CTA, a sleep
  study) — those are data to OBTAIN, not treatments to weigh, and belong
  solely in dataRequisition. Litmus test: if you cannot name at least two
  genuine cons AND two real alternative therapies for the SAME goal, it is
  not a therapeutic decision — drop it (it is almost certainly a
  requisition). Getting a number on file has no therapeutic cons or
  alternatives, which is the tell.

  BE PRECISE and name the relationships between options. When a drug
  class has a foundation + add-on structure, recommend the FOUNDATION
  explicitly rather than assuming it: e.g. for residual ApoB, do NOT
  propose a PCSK9 inhibitor "atop a statin" without recommending the
  statin itself — recommend a specific statin (e.g. rosuvastatin, with a
  muscle-sparing note where the patient's goals warrant), then ezetimibe,
  then a PCSK9 inhibitor as escalation steps if the ApoB target is not
  met. Name a specific agent and, where determinable, a starting dose.
  Surface the obvious standard-of-care interventions the Finding implies
  even when unglamorous. Note when an item is already in the patient's
  regimen or plan (so it reads as confirmation, not a contradiction).
  Skip pure dose-titration of an existing drug (that belongs in treatment
  assessment). Aim for the complete set the Finding warrants — typically
  3–8 entries, up to 12 for a patient with many open studies.

  For each entry (patient or ai):
    intervention: copy the intervention string verbatim from the user
      message (e.g. "Testosterone Replacement Therapy", "Tesamorelin"),
      or, for ai entries, a concrete drug-class label (e.g. "Statin or
      PCSK9 inhibitor", "SGLT2 inhibitor", "Enclomiphene").
    purpose: for patient entries, copy the patient's stated purpose
      verbatim from the user message (e.g. "improved free T", "reduce
      visceral adipose tissue"). For ai entries, a short clause (≤22
      words) that LEADS WITH THE BENEFIT — the functional or clinical
      outcome the patient actually cares about, tied to their goals or
      symptoms where relevant (better overnight HRV and recovery, lower
      long-term heart-attack / stroke risk, preserved fertility, more lean
      mass for the masters-sport goal) — and THEN names the metric(s) by
      which that benefit is measured. Do NOT give a bare metric move as the
      whole purpose. e.g. NOT "lower homocysteine and raise Vitamin B12" but
      "improve vascular and autonomic recovery (overnight HRV), measured by
      homocysteine and Vitamin B12 normalizing"; NOT "lower ApoB to <55" but
      "cut long-term heart-attack and stroke risk, measured by ApoB to <55".

    pros: an array of 3–6 short bullets (each ≤30 words) covering the
      reasons to pursue this intervention for THIS patient given the
      Finding above. Tie each pro to the patient's specific data when
      relevant — their actual lab values, age, symptoms, goals, athletic
      profile, etc. Cover the upside angles a thoughtful clinician would
      raise (e.g. for TRT in a middle-aged man with low Free T and a
      masters athletics goal: "lifts Free T from the bottom of the range
      where symptoms tend to cluster", "consistent with the patient's
      masters-sports performance goal", "addresses low-T fatigue and
      recovery patterns").

    cons: an array of 3–6 short bullets (each ≤30 words) covering the
      reasons NOT to pursue, or the risks/costs that come with it, tied
      to THIS patient's profile and goals. Cover the full set a thoughtful
      clinician would raise. For TRT specifically that means: impact on
      fertility (testicular atrophy, suppressed spermatogenesis), E2
      conversion / aromatization and the side effects that follow, drug
      dependency / HPG-axis suppression that may be hard to reverse,
      cardiovascular and hematocrit considerations, the lifelong
      commitment, and whether the patient's age and lab basis (total T
      vs Free T) really warrant it. Adapt to the actual intervention
      under consideration — Tesamorelin's cons differ (IGF-1 / acromegaly
      risk, glucose impact, injection burden, cost, regulatory status).

    alternatives: an array of 2–5 short bullets (each ≤40 words) naming
      OTHER ways to pursue the same stated purpose, with a one-clause why.
      For TRT targeting low Free T, alternatives include clomid /
      enclomiphene (preserves fertility and HPG axis), hCG monotherapy,
      addressing SHBG drivers (insulin resistance, fatty liver), weight
      loss + sleep optimization, treating the underlying cause if
      secondary hypogonadism (prolactin, pituitary). For Tesamorelin
      targeting VAT, alternatives include caloric deficit + resistance
      training, GLP-1 / GIP agonist titration, SGLT2 inhibitor in the
      right context, sleep / cortisol optimization.

    recommendation: 3–6 sentences of plain prose. Synthesize: should the
      patient pursue this, hold off, or pursue an alternative first?
      Anchor your recommendation to THIS patient's specific data (their
      age, the lab values that matter for this decision, fertility goals,
      athletic goals, current treatment regimen). Make explicit what GATES
      the action: name whether the data already on file is enough to act on
      NOW, or whether a specific further reading / plan step must come first.
      When the patient can act today, say so and point to the data that
      licenses it (e.g. "lipid markers — ApoB at 76 vs. a target of <55 —
      already give you and your doctor enough data to act right now"); when
      it should wait, name the exact gate (the missing draw, the prior drug
      that must be on board, the threshold a marker must cross). Be specific
      about the conditions under which the answer changes (e.g. "if fertility is
      preserved as a near-term goal, start with enclomiphene rather than
      direct TRT", "if Free T stays below X after 6 months of lifestyle
      and weight loss, then TRT becomes more justifiable"). Use
      "consider", "discuss with the prescribing physician", "could be
      reasonable if" — never a hard directive.
