---
node: healthProgression
kind: derived
label: "Health Progression"
inputs: [patientAssessment, markerLevels]
basis: "Latest / recent / overall trajectory read."
tags: [dag/derived]
---

# Health Progression

Latest / recent / overall trajectory read.

## Inputs

- [[patientAssessment]]
- [[markerLevels]]

## Reasoning

progression.latest: 4–8 sentences. Describe where the patient stands RIGHT
  NOW, based on each meaningful marker's single most recent reading vs its
  personalized target. Cite specific values for the markers that materially
  shape the snapshot ("ApoB latest 76 against a <60 target", "free T latest
  62 pg/mL against an 80–150 target"), weighted toward watchlist + out-of-
  range markers. This is the "what does the current picture look like"
  paragraph the patient would read first. Plain prose, no bullets.

  progression.recent: 4–8 sentences. Discuss the EVOLUTION across the last
  12 months — how the picture moved, not where it ended. Speak holistically
  about the patient's health (atherogenic risk, glycemic control, hormonal
  axis, body composition, hepatic load) and call out the wins and the
  setbacks of this window. Tie the year's trajectory to any intervention
  started or titrated in this window (drugs, supplements, behavioral
  changes). Plain prose.

  progression.overall: 4–8 sentences. Place the Latest snapshot in the
  CONTEXT OF THE FULL HISTORICAL DATASET. Where did the patient come from
  across every reading on file, including data older than 12 months? Frame
  it as progress vs regression over the life of the dataset: is the recent
  picture a continuation of long-standing drift, a clear turnaround, or a
  partial recovery that has not yet returned to a pre-incident baseline?
  Reference the prior-baseline numbers from the Markers block to anchor the
  comparison, and contextualize today against where this person started.
  Plain prose.
