# Compression Patterns

## Overview

Late-stage compression is a universal part of the writing process. This document catalogs the 7 specific compression operations, their application context, and the principles they encode.

---

## Pattern 1: Sentence Shortening

**Operation**: Remove subordinate clauses, redundant qualifiers, and throat-clearing phrases.

**Before**: "We argue that a data-driven approach that leverages machine learning techniques can potentially offer significantly better trade-offs between the measurement cost and accuracy."

**After**: "Do speed tests need to transmit their full data volume to produce accurate results?"

**Principle**: Every word must earn its place. If a clause can be removed without losing meaning, remove it.

---

## Pattern 2: Paragraph Merging

**Operation**: Merge paragraphs that make the same point with different examples into a single paragraph with the best example.

**Principle**: Multiple examples of the same point dilute rather than strengthen. One well-chosen example is stronger than three adequate ones.

---

## Pattern 3: Removal of Generic Adjectives

**Before**: "significant", "substantial", "impressive", "promising", "novel", "innovative"

**After**: Specific numbers ("2–4×"), named mechanisms, or deleted entirely.

**Principle**: Generic adjectives are space-consuming non-information. They tell the reader "this is good" without saying HOW good. Replace with metrics or delete.

---

## Pattern 4: Removal of Tutorial Explanation

**Operation**: Delete paragraphs that explain concepts the venue audience already knows.

**Typical deletions**: General optimization theory, formal definitions of well-known ML concepts, textbook-level background on the venue's core domain.

**Quantitative signature**: The largest single deletions in any paper are tutorial material.

**Principle**: If the venue's reviewers already know it, it doesn't belong. The only exception: when the paper redefines a known concept in a new way — then the redefinition IS the contribution.

---

## Pattern 5: Conversion to Claim-First Sentences

**Before (descriptive)**: "Experimental Results" / "System Architecture"

**After (claim-first)**: "System X outperforms all baselines by 2–4×" / "Why do linear approaches fail?"

**Operation**: Rewrite headings so they contain the section's conclusion, not just its topic. Rewrite paragraph openings so the claim comes first and evidence follows.

**Principle**: Readers skim headings and topic sentences. If the heading contains the finding, the skim-reader gets the argument. If it only names the topic, they get nothing.

---

## Pattern 6: Evaluation Compression via Takeaways

**Operation**: Replace multiple paragraphs of detailed result description with a compact Takeaway paragraph that synthesizes the key finding.

**Before**: 8 paragraphs of per-condition results with individual numbers.

**After**: 3 paragraphs of grouped results + 1 Takeaway paragraph that states the implication.

**Principle**: The reader doesn't need every number — they need the PATTERN. Takeaway paragraphs compress results into interpretations.

---

## Pattern 7: Figure/Table Promotion (Text → Visual)

**Operation**: Move detailed numerical comparisons from prose into figures or tables. Replace prose descriptions with figure references + interpretation.

**Before**: "Model A achieves 92%. Model B achieves 87%. Model C achieves 84%. Model D achieves 91%."

**After**: "Table 3 shows all model accuracies. Our system outperforms all baselines, with the largest margin against static thresholds."

**Principle**: Dense numerical comparisons belong in tables. Prose should interpret patterns, not list numbers.

---

## Compression Intensity Guide

| Compression ratio | What it signals |
|---|---|
| 10–20% | Draft was already close to final form. Light polish needed. |
| 30–50% | Normal. The authors now know what matters vs. what was interesting to write about. |
| 50–65% | Crisis compression — the framing changed fundamentally. Content was cut because the narrative shifted, not because it was wordy. |
| >65% | Likely indicates a structural rewrite, not just compression. |

---

## The Expansion-Compression Arc

Every paper follows this pattern:

1. **Student draft**: Comprehensive, includes everything discovered
2. **Advisor edit round 1**: May EXPAND (add "why" arguments, structural labels)
3. **Advisor edit round 2+**: COMPRESS (remove what doesn't serve the argument)

The expansion peak is never the final version. The compression pass is a sign of editorial maturity — the authors finally know what matters.

This arc is observable at every scale: sentences shorten, paragraphs merge, sections consolidate, total character count decreases in the final pass.
