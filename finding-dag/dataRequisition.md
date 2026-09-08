---
node: dataRequisition
kind: leaf
label: "Data Requisition"
inputs: [aiFindings, markerLevels]
basis: "Data to obtain next, by body system (W27) then modality, plus standard-of-care intervals."
tags: [dag/leaf]
---

# Data Requisition

Data to obtain next, by body system (W27) then modality, plus standard-of-care intervals.

## Inputs

- [[aiFindings]]
- [[markerLevels]]

## Reasoning

follow-on imaging the Finding implies, with timing driven by Today
      vs the date of the prior study (e.g. a repeat coronary artery
      calcium / CTA given the years elapsed since the patient's prior
      cardiac imaging in Diagnosed Disease);
    • RE-SCAN every condition in Diagnosed Disease whose status is tracked
      by imaging or a procedure and whose last study is stale relative to
      Today, so the requisition UPDATES the prior finding rather than leaving
      it frozen at diagnosis. Walk the Diagnosed Disease list and, for each
      such condition with no more-recent equivalent study on file, requisition
      the modality that re-stages it — e.g. hepatic steatosis / NAFLD →
      liver ultrasound or MRI-PDFF with MR elastography / FibroScan (the
      quantitative re-stage of steatosis and fibrosis), coronary plaque →
      CAC / CTA. State the prior finding, its date, and the elapsed time in
      the rationale, and where a Plan drug plausibly changed that organ (e.g.
      Tirzepatide / weight loss on hepatic fat) anchor the timing so the
      re-scan captures the treated state. Do NOT treat blood enzymes (ALT/AST)
      as a substitute for the imaging re-stage of a structural diagnosis.
    • age- and history-appropriate standard-of-care screenings that are
      due or overdue (e.g. colonoscopy if none in ~10 years, DEXA, skin
      check), judged against Today and the patient's age.
  Each rationale is one short clause naming WHY — the marker pattern,
  diagnosis, elapsed time, or guideline interval. Where the USEFUL timing of
  a requisition depends on a step in the Patient Plan — a draw or scan whose
  result only becomes meaningful once a planned drug has been started, dosed
  to target, or been on board long enough — make that relative timing
  EXPLICIT in the rationale, naming the plan step it hinges on (e.g. "ideally
  after the statin has been on board for 6+ months so the result reflects
  the future treatment regime", or "draw 6–8 weeks after the Tirzepatide
  titration to 10–15 mg lands"). Do this only where it genuinely changes
  WHEN to order; routine draws need no such clause. Group only the modalities
  that have items; if a group would be empty, omit it. Use the patient's
  actual dates and Today to reason about elapsed time; never invent a date.
