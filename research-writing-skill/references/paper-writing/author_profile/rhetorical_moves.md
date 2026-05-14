# Rhetorical Moves: Cross-Section Summary

## Source
Derived from final versions of accepted and rejected papers across systems and ML venues.

---

## Introduction (6-Move Sequence)

| Move | Function | What it looks like |
|------|----------|-------------------|
| 1. Stakes | Why the domain matters | Name specific actors (users, operators, policymakers) or applications. Never open with "ML has shown great promise." |
| 2. Problem Gap | Structural limitation of current approaches | The gap is always structural, not quantitative. Not "existing tools aren't good enough" but "existing tools are fundamentally limited because..." |
| 3. Key Abstraction | Named concept — the paper's intellectual core | A coined term that captures the core insight. Appears ONLY in final versions — discovered through writing. |
| 4. Design Intuition | One-paragraph mental model | The "elevator pitch" — how the system works at the highest level. No algorithmic details. |
| 5. Contributions | Numbered, labeled, claim-first | Each item: bold label + claim (not process). "We show X" not "We propose X." |
| 6. Results Preview | Headline number(s) | Written AFTER the evaluation is complete. Anchors the introduction with concrete evidence. |

**Critical observation**: Move 3 (Key Abstraction) appears ONLY in final versions. It is discovered through writing, not planned before it.

**Accepted vs. rejected**: Accepted papers have specific stakes and clear named abstractions. Rejected papers have vague or overly abstract stakes.

---

## Design (5-Move Sequence)

| Move | Function | What it looks like |
|------|----------|-------------------|
| 1. Abstraction Introduction | User-facing mental model | Present what users reason about, not what the system computes internally. |
| 2. Design Justification | Why THIS design | Often a negative result: "the obvious approach fails because X." Makes the chosen design feel inevitable. |
| 3. Component Architecture | Named stages/modules | Always a pipeline or structured flow the reader can trace. Component names become the evaluation's vocabulary. |
| 4. Key Design Decision | The non-obvious "knob" | A configurable parameter that shows the system isn't one-size-fits-all. |
| 5. Robustness | What happens when assumptions fail | Often added late per reviewer/advisor feedback. Signals defensive design awareness. |

**Anti-patterns**: Opening with implementation details (not abstractions). Formal math replacing intuition. Missing the "why" argument.

---

## Evaluation (6-Move Sequence)

| Move | Function | What it looks like |
|------|----------|-------------------|
| 1. Setup Anchoring | Dataset, baselines, metrics | Compressed. Just enough for reproducibility, not a technical report. |
| 2. Head-to-Head | Direct comparison vs. named baselines | The paper's core evidence. Baselines NAMED, not "prior work." |
| 3. Deep Dive | Disaggregated analysis | Break down by meaningful conditions. Show WHERE the system helps most and least. |
| 4. Takeaway Synthesis | Pattern statement after each experiment cluster | Ties results to claims. Prevents readers from drawing wrong conclusions. |
| 5. Ablation | Design choice validation | Shows each component contributes. Answers "is your design over-engineered?" |
| 6. Robustness | External validity | Temporal generalization, spatial generalization, computational overhead. |

**Evolution**: Student drafts use Move 2 only (head-to-head). The advisor adds Moves 3–6. The Takeaway (Move 4) is the signature addition — absent from all early drafts, present in all final versions.

---

## Related Work (3-Move Sequence)

| Move | Function | What it looks like |
|------|----------|-------------------|
| 1. Category Clustering | Group prior work by approach type | 2–4 categories max. Named by approach type, not by individual paper. |
| 2. Per-Category Limitation | Structural limitation of each category | Must be STRUCTURAL (inherently unable) not quantitative (not good enough). |
| 3. Positioning Sentence | Differentiate this paper from all categories | "Unlike X, our approach provides Y while maintaining Z." Carves out architectural space. |

**Placement**: Post-evaluation in systems papers (confidence signal). Integrated into background in ML papers.

**Anti-patterns**: Exhaustive literature survey (>10K chars). Equal treatment of all categories. Missing the positioning sentence.

---

## Cross-Section Coherence Rules

1. **Introduction promises = Evaluation delivers**: Each contribution maps to a specific evaluation subsection.
2. **Key abstraction propagates**: The named concept from Introduction Move 3 appears in Design Move 1, Evaluation Move 1, and Related Work Move 3.
3. **Heading consistency**: If the introduction says "(1) Learning problem. (2) Design. (3) Evaluation.", the section headings reflect this order.
4. **Figure-claim linkage**: Each evaluation head-to-head or deep dive references a specific figure or table.
