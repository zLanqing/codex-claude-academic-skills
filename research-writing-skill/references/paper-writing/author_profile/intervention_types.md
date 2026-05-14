# Advisor Intervention Types

## Overview

This document classifies the 7 types of editorial interventions an advisor typically makes on student drafts. Use this to simulate advisor feedback: given a draft, identify which intervention types apply, then apply them in the order listed.

---

## Type 1: Framing Intervention

**What it is**: Changing the paper's top-level narrative — what the paper claims to be "about."

**When it fires**: When the draft's framing doesn't match the actual contribution, or is too broad/narrow for the target venue.

**Mechanism**: Complete rewrite of introduction and/or background. Near-zero sentence survival. New version created from scratch rather than editing in place.

**Example pattern**: "Survey of approaches in domain X" → "Methodology-agnostic layer that addresses specific problem Y."

---

## Type 2: Structural Rewrite

**What it is**: Reorganizing sections — splitting, merging, renaming, reordering — without necessarily changing content substance.

**When it fires**: When the section structure reflects how the author THOUGHT about the work rather than how the reader needs to RECEIVE it.

**Example patterns**: Consolidating 4 sections into 2. Splitting a monolithic evaluation into separate sections by claim type. Replacing formal math with a pipeline narrative.

---

## Type 3: Background Deletion

**What it is**: Removing substantial amounts of background/tutorial material that doesn't sharpen the contribution.

**When it fires**: When background sections are longer than design + evaluation combined, or when they explain concepts the venue audience already knows.

**Quantitative signature**: The largest single deletions are always tutorial material. Reductions of 50–65% in background sections are common.

---

## Type 4: Evaluation Strengthening

**What it is**: Adding structure, baselines, and narrative control to the evaluation.

**When it fires**: When results are presented without interpretation, baselines are unnamed, or figure-text inconsistencies exist.

**Mechanism**: Addition of Takeaway paragraphs, named baselines, formal metrics sections, consistency checks between figures and text.

---

## Type 5: Terminology Tightening

**What it is**: Replacing vague terms with specific, named alternatives.

**When it fires**: When a term could mean multiple things, or a generic term obscures the specific mechanism.

**Example patterns**: "heuristics" → "static thresholds, protocol-specific signals, timing-based strategies." "Data generation" → a coined term like "progressive disaggregation."

---

## Type 6: Contribution Reframing

**What it is**: Changing how the contribution list is expressed — from process descriptions to claim-first statements.

**When it fires**: When contributions read like a task list rather than claims the paper defends.

**Example pattern**: "We propose a data-driven approach" → "We cast problem X as an optimal stopping problem, exposing the accuracy-cost trade-off as a configurable parameter."

---

## Type 7: Argument Clarification

**What it is**: Adding explicit reasoning that connects claims to evidence.

**When it fires**: When results are presented without connecting them to design claims.

**Mechanism**: Adding connecting sentences ("This confirms that...", "The implication is...") between data presentation and interpretation.

---

## Intervention Sequence

In practice, these interventions are applied in two passes:

**Pass 1 (structural)**: Types 1, 2, 3, 5, 6 — simultaneously during a major rewrite.

**Pass 2 (polish)**: Types 4, 7, + compression — during the final editing pass.

When simulating advisor feedback, apply the highest-priority type first (framing > structure > terminology), then move to pass 2.
