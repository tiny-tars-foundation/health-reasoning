---
node: markerGroups
kind: projection
label: "Marker Groups"
inputs: [aiFindings, labData, watchlist]
basis: "Every marker assigned to a body system (System Analysis order), cross-source — the Markers grouping axis."
tags: [dag/projection]
---

# Marker Groups

Every marker assigned to a body system (System Analysis order), cross-source — the Markers grouping axis.

## Inputs

- [[aiFindings]]
- [[labData]]
- [[watchlist]]

## Reasoning

You assign a patient's lab/biometric markers to the patient's own body systems
(the AI Finding's disease areas), so each marker is read alongside the others
that speak to the same underlying system. This is cross-source: a marker may come
from bloodwork, a scan, or a body-composition scale — assign by what it MEANS
clinically, not by the panel or device it came from (e.g. an aortic-root diameter
and ApoB both belong to Cardiovascular Risk; Android % Fat belongs to Body
Composition).

EVERY listed name is a DISTINCT marker you must place, even when it closely
resembles another one. A free vs total, a percentage vs mass vs area, a ratio vs
its components, a high-sensitivity vs standard assay, a per-segment vs whole-body
measure are DIFFERENT markers (e.g. Apolipoprotein B, Apo B : Apo A-1, and
Apolipoprotein A-1 are three separate Cardiovascular markers; hsCRP and CRP are
both Inflammation; Free testosterone and Testosterone are both Hormonal).

Within a group, order markers from most to least central to the system.
