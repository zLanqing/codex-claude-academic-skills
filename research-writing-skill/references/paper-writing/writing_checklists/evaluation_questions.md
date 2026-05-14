# Self-Diagnostic: Evaluation Section

## Source
Derived from evaluation rhetorical move analysis across 6 papers (see `section_rhetorical_moves/evaluation.md` and `author_profile/claim_evidence_patterns.md`).

---

## Claim-Evidence Alignment (Principle 1)
- [ ] Can you list **every claim** the introduction makes?
- [ ] Does each claim have a **dedicated evaluation subsection**?
- [ ] If the paper makes **two types of claims** (e.g., system correctness + downstream improvement), are they in **separate evaluation sections**? (Principle 9)
- [ ] Can each subsection be described as: "This section shows that [specific claim]"?

## Setup Anchoring
- [ ] Are **all baselines named** (not "prior methods" or "state-of-the-art")?
- [ ] Are baselines **described precisely enough** for the reader to understand what they are?
- [ ] Are **metrics defined** and **justified** (why these metrics for these claims)?
- [ ] Is the dataset described (size, source, time period, any biases)?

## Result Presentation
- [ ] Are detailed numerical comparisons in **tables or figures**, not inline prose?
- [ ] Does prose **interpret patterns** rather than **list numbers**? (Principle: "Table 3 shows..." + pattern, not "Model A: 92%, Model B: 87%...")
- [ ] Do figures have **proper axis labels, units, and captions**?
- [ ] Does the text **match the figures** exactly? (No contradictions with table captions, no wrong time ranges)

## Takeaway Paragraphs (Principle 8)
- [ ] Does every experiment cluster end with an explicit **"Takeaway."** paragraph?
- [ ] Does the Takeaway state the **implication** (not just the result)?
- [ ] Is the Takeaway interpretable **without reading the detailed results**?
- [ ] Does the Takeaway **tie back to a specific design claim or contribution**?

## Deep Dive / Disaggregation
- [ ] Are results **disaggregated** by relevant conditions (e.g., by RTT, speed tier, geographic region)?
- [ ] Do disaggregated results reveal **where the system helps most** and **where it helps least**?
- [ ] If aggregate results are "surprising," is there a **distribution-level analysis** explaining why?

## Ablation
- [ ] Is there an ablation study that validates key design choices?
- [ ] Does the ablation **support** the design narrative (not undermine it)?
- [ ] If an ablation variant outperforms the full system, is this **acknowledged and explained**?

## Robustness
- [ ] Are results tested under **conditions not in the training set** (concept drift, new data, edge cases)?
- [ ] Is the deployment overhead or scalability addressed?

## The Evaluation Maturity Test
Rate your evaluation on this scale:
| Level | Description | Missing element |
|-------|-------------|----------------|
| 1 | Lab notebook | Results without interpretation |
| 2 | Technical report | Comprehensive but unfocused (no claim structure) |
| 3 | Conference paper | Results organized by research questions |
| 4 | Systems narrative | \smartparagraph + Takeaway markers + claim-first headings |

Target: Level 4.
