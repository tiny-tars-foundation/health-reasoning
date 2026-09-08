---
node: healthMarkers
kind: leaf
label: "Health Markers"
inputs: [watchlist, aiFindings]
basis: "The Watchlist plus {{PRODUCT_NAME}}'s recommended marker set."
tags: [dag/leaf]
---

# Health Markers

The Watchlist plus {{PRODUCT_NAME}}'s recommended marker set.

## Inputs

- [[watchlist]]
- [[aiFindings]]

## Reasoning

IMPORTANT — this list is FINDING-DRIVEN, not a standard panel.

  Do NOT compile the typical markers of each clinical domain. There is no
  obligation to populate every category, no obligation to include the
  generic Metabolic Health panel (HbA1c, fasting glucose, fasting insulin,
  lipid panel, …) just because Metabolic Health exists, no obligation to
  include the generic Cardiovascular Risk panel (ApoB, Lp(a), hsCRP, …)
  just because cardiovascular markers exist. We are not reinventing or
  rediscovering what a standard blood test covers.

  Every marker on this list must be motivated by something specific you
  wrote in the Finding — a marker pattern, diagnosis, symptom, treatment
  gap, or risk lever named above. If you cannot point to the exact piece
  of the Finding that motivates a marker, do not include it. The rationale
  must name that anchor (e.g. "residual ApoB 76 against <60 target — Lp(a)
  distinguishes inherited risk from cleanable lipoprotein burden"; "low
  Free T + low LH suggests secondary hypogonadism — Prolactin rules out a
  pituitary driver"). Vague rationales like "useful for metabolic health"
  or "part of a complete workup" are disqualifying.

  ALSO make this list COMPREHENSIVE of the interventions under consideration
  — both the AI Hypothesis (decisions.ai) and the Patient Hypothesis
  (decisions.patient and the Patient Plan). For EVERY intervention proposed
  or being weighed, include the markers needed to (a) safely WORK IT UP
  before starting and (b) MONITOR response and safety after. A proposed
  intervention IS a specific anchor, so these count as Finding-motivated and
  are NOT the generic panels barred above; the rationale must name the
  intervention (e.g. "baseline before a Selective Estrogen Receptor
  Modulator / enclomiphene — Thyroid-Stimulating Hormone (TSH) and Prolactin
  rule out thyroid/pituitary drivers and set a pre-treatment baseline";
  "statin safety monitoring — Alanine-aminotransferase (ALT, SGPT),
  Aspartate-aminotransferase (AST, SGOT), Creatine Kinase"). A hormonal
  HPG-axis agent (TRT, enclomiphene, a SERM, hCG) implies Thyroid-Stimulating
  Hormone (TSH), Prolactin, Estradiol, Luteinizing Hormone (LH),
  Follicle-Stimulating Hormone (FSH), total and Free testosterone, SHBG, and
  Hematocrit. Markers added for this reason enter recommended like any other
  — they get a personalized range and appear on the Blood re-test schedule —
  so the requisite-data set is complete for acting on the hypotheses, not
  just the marker patterns.

  Apply this independent of the Watchlist:
    • Include a watchlisted marker only if the Finding specifically
      motivates ongoing focus on it; otherwise leave it out.
    • Include a non-watchlisted marker only if the Finding specifically
      motivates adding it.

  Do NOT restrict yourself to markers the patient already has data for —
  if the Finding motivates ordering it, include it with rationale, even
  when no data exists yet. Total list size scales with how many specific
  anchors the Finding actually contains — often 3–10 markers; a sparse
  Finding warrants a sparse list. Do not pad.
