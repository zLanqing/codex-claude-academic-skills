# Writing a Related Work Section: The 3-Move Sequence

## Overview

Related work is a positioning tool, not a literature survey. It should be under 10K characters and every cited work should serve the purpose of positioning YOUR contribution.

---

## Placement Decision

Two strategies:

**Post-evaluation placement** (most systems papers): Related work appears AFTER the evaluation. This is a confidence signal — "you'll understand why existing work is insufficient only after seeing our results." Use when novelty is primarily empirical.

**Integrated into background** (most ML papers): Related work is woven into the background/motivation section. Use when the paper needs to establish a landscape before the contribution makes sense.

**Rule**: Choose placement based on whether the paper needs to DEFEND (post-eval) or ESTABLISH (pre-eval) its positioning.

---

## Move 1: Category Clustering

**Function**: Group prior work into 2–4 categories, each with a named limitation.

**How to do it**: Name categories by approach type (e.g., "Crowdsourced / Controlled / Hybrid"), not by individual paper. Never more than 4 categories — more signals the author hasn't found the right abstraction.

**Test**: Can the reader hold the full taxonomy in working memory?

---

## Move 2: Per-Category Limitation

**Function**: After presenting each category, identify its structural limitation.

**How to do it**: The limitation must be STRUCTURAL (an inherent property of the approach), not quantitative (just didn't do enough). Structural limitations motivate new approaches; quantitative gaps motivate more experiments.

**Test**: Does the limitation connect to a feature of your system that addresses it?

---

## Move 3: Positioning Sentence

**Function**: A single sentence that places the paper relative to the entire landscape.

**How to do it**: "Unlike X, our approach provides Y while maintaining Z." Or: "This paper does not compete in category X; it creates category Y." This preempts the "incremental" criticism by carving out ARCHITECTURAL space.

**Test**: Does the positioning sentence name your key abstraction? Is it honest about what you DON'T do?

---

## Anti-Patterns

1. **Exhaustive literature survey**: If your related work is over 10K characters, it's a survey, not a positioning section. Cut to representative examples per category.

2. **Symmetric treatment**: Don't give equal space to every category. Weight toward what matters for positioning YOUR paper.

3. **Missing the positioning sentence**: Without it, reviewers will ask "how is this different from X?" Don't make them guess — state it explicitly.

4. **Tutorial paragraphs**: Don't explain foundational concepts the venue audience already knows. If you're submitting to SIGCOMM, don't explain TCP.

---

## Consistency Checks

Before finalizing:
- Does the positioning sentence align with the key abstraction in the introduction?
- Are the baselines mentioned in related work the same baselines used in the evaluation?
- If a reviewer asks "how is this different from [closest work]?", does the related work preemptively answer?
