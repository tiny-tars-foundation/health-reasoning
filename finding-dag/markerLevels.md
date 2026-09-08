---
node: markerLevels
kind: derived
label: "Marker Levels"
inputs: [labData, patientAssessment, statedObjective, watchlist, diagnosedDisease, pinnedQueries, recommendedMarkers, personalizedRanges]
basis: "Lab data with {{PRODUCT_NAME}}-inferred personalized levels."
tags: [dag/derived]
---

# Marker Levels

Lab data with {{PRODUCT_NAME}}-inferred personalized levels.

## Inputs

- [[labData]]
- [[patientAssessment]]
- [[statedObjective]]
- [[watchlist]]
- [[diagnosedDisease]]
- [[pinnedQueries]]
- [[recommendedMarkers]]
- [[personalizedRanges]]
