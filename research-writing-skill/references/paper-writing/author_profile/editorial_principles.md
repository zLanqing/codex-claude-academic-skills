# Editorial Principles for Research Papers

## Overview

These 13 principles are distilled from systematic analysis of multiple paper revision histories across systems and ML venues. Each principle is supported by evidence from at least two independent paper revision cycles. They are ordered by their observed impact on acceptance outcomes.

---

## Principle 1: Introduction-Twice (Draft 0 → Evaluation → Final Introduction)

The introduction is written twice. **Draft 0** is a framing scaffold — stakes, problem gap, rough contribution claims — written early to set guardrails for the evaluation. It clarifies thinking and establishes what the paper is *trying* to show. Draft 0 is explicitly disposable; it probably will not survive. **The final introduction** is written after the evaluation is complete, constrained by what the evidence actually supports. Each claim in the final introduction must map to a specific evaluation subsection.

The key insight: writing is a thinking tool, not just a communication tool. A preliminary introduction forces the student to externalize their framing *before* designing experiments. Without Draft 0's guardrails, the evaluation is written without constraints — the student doesn't know what they're trying to show. But without evaluation-constrained rewriting, the introduction promises what the student *hoped* to show rather than what they *did* show.

**Observed consequence of skipping Draft 0**: Students who went straight to evaluation without framing guardrails produced evaluations that were technically complete but narratively incoherent — the experiments didn't build toward a unified argument because there was no argument to build toward.

**Observed consequence of skipping the rewrite**: Papers whose Draft 0 introduction survived to submission frequently promised capabilities (e.g., "domain adaptation," "cross-domain generality") that the evaluation couldn't deliver. These papers were rejected.

**Rule**: Write a Draft 0 introduction early (stakes, problem gap, rough contributions) to set evaluation guardrails. Write the final introduction AFTER the evaluation is complete, from scratch. Draft 0 is scaffolding, not a starting point for editing.

---

## Principle 2: Named Over Vague

Replace every generic term with a specific, named alternative. Generic adjectives ("significant," "substantial," "promising," "novel") are space-consuming non-information. Named mechanisms, specific numbers, and coined terminology earn their place.

**The test**: If a term could apply to ANY paper in the field, it doesn't belong in YOUR paper. "Data-driven approach" could describe thousands of papers. A precise phrase like "two-stage framework with configurable accuracy-cost trade-off" describes exactly one.

**Rule**: Every baseline, metric, and abstraction should have a proper name. If the paper introduces a new concept, NAME it — the name becomes citable.

---

## Principle 3: The What → Why → So-What Heading Progression

Section headings evolve through three stages as a paper matures:

1. **WHAT headings** (student drafts): descriptive, topic-naming. Example: "Experimental Results"
2. **WHY headings** (first senior edit): problem-driven. Example: "Why do linear approaches fail?"
3. **SO-WHAT headings** (final version): claim-first, stating the conclusion. Example: "System X outperforms all baselines by 2–4×"

**The test**: Can a skim-reader reconstruct the paper's argument from headings alone? If headings only name topics, the skim-reader gets nothing. If headings contain claims, the skim-reader gets the argument.

**Rule**: Rewrite every heading to contain the section's CONCLUSION, not just its TOPIC.

---

## Principle 4: Compress After Expanding

Every paper follows an expansion-compression arc. The first draft is comprehensive ("everything in"). The advisor may EXPAND first (adding structural labels, "why" arguments). Then compression removes what doesn't serve the argument. The longest version is never the final version.

**Normal compression range**: 30–50% reduction in the final pass. Compression above 50% usually signals a framing problem — content was cut because the narrative shifted fundamentally. Compression below 15% suggests the draft was already near publication-ready.

**Rule**: Write comprehensively first. Then ask of every paragraph: "Does this serve one of the paper's explicit claims?" If not, delete it.

---

## Principle 5: Structural Rewrites Over Incremental Editing

The writing process is iterative reconceptualization, not polishing. Each major version should be written from scratch with the SAME underlying results but a DIFFERENT narrative. Attempting to polish an early draft into a final version produces mediocre results because the framing decisions are baked into the sentence structure.

**When to polish vs. rewrite**: If the paper's identity (what it claims to be about) is stable, polish. If the identity needs to change, rewrite from scratch. The signal that a rewrite is needed: the introduction promises something the evaluation doesn't deliver.

**Rule**: When creating a new major version, start from a blank page. The previous version is reference material, not a starting point.

---

## Principle 6: Labeled Paragraphs as Narrative Contracts

In systems venues, labeled paragraph markers (e.g., \smartparagraph{}) function as explicit narrative contracts. Each label constrains what the following paragraph must deliver. Once the labels are set, editing is constrained to FILL them, not restructure around them. This is why labeled paragraph introduction correlates with paper stabilization.

**Venue adaptation**: Labeled paragraphs are a systems-paper convention (SIGCOMM, NSDI). For ML venues (NeurIPS, ICLR), replace with section headers using colon-style subtitles.

**Rule**: Before writing a section, write the paragraph labels first. They are the section's outline. If a paragraph doesn't fit any label, the paragraph doesn't belong, or a label is missing.

---

## Principle 7: Problem-First, Not Method-First

Student drafts frequently lead with the ML/AI technology. The advisor's intervention shifts the opening to lead with the PROBLEM the technology solves. The ML/AI component becomes the METHOD, not the MESSAGE.

**Why this matters**: Method-first openings position the paper as "another ML application" — competing against every other ML-for-X paper. Problem-first openings position the paper as solving a domain problem — competing against other solutions to that specific problem. The latter is a smaller, more winnable competitive frame.

**Rule**: The first sentence should describe the PROBLEM or DOMAIN, not the TECHNOLOGY. ML/AI should appear no earlier than the third paragraph.

---

## Principle 8: Takeaway Paragraphs in Evaluation

After every experiment or group of related experiments, insert a Takeaway paragraph that states the IMPLICATION, not just the result. The Takeaway compresses results into interpretation — it tells the reader the PATTERN, not the NUMBERS.

**Before**: "Model A: 92%, Model B: 87%, Model C: 84%, Model D: 91%."
**After**: "Takeaway. Our system outperforms all baselines, with the largest margins in challenging conditions."

**Rule**: Every evaluation subsection ends with a Takeaway paragraph. It should be interpretable without reading the detailed results — it is the skim-reader's entry point.

---

## Principle 9: Dual Evaluation for Dual Contributions

If a paper makes two fundamentally different types of claims (e.g., "the system works correctly" AND "the system improves downstream performance"), the evaluation must be split into separate sections. A monolithic evaluation that mixes claim types produces confusion because each claim requires different baselines, metrics, and experimental design.

**The test**: Can each evaluation subsection be described with a single sentence of the form "This section shows that [specific claim]"? If a subsection argues for multiple claims, it needs to be split.

**Rule**: Before writing the evaluation, list every claim from the introduction. Map each claim to baselines, metrics, and experiments. If two claims require different experimental designs, they belong in separate subsections.

---

## Principle 10: Venue-Specific Structural Adaptation

The same underlying principles (claim-first headings, named-over-vague, evaluation-organized-by-claim) apply everywhere, but surface conventions must adapt to venue norms.

**Systems venue conventions** (SIGCOMM, NSDI): Labeled paragraphs, "Design" section with named components, Takeaway paragraphs, post-evaluation related work, page-limit compression.

**ML venue conventions** (NeurIPS, ICLR): Method-naming sections with colon subtitles, reproducibility checklist, large appendix, method-driven headings.

**Rule**: Before writing, read 3–5 recent accepted papers at the target venue. Adapt surface conventions while maintaining the underlying principles.

---

## Principle 11: Rejection Drives Abstraction

Rejection forces papers to a higher level of abstraction. Each rejection identifies a framing mismatch — the paper claims to be X but delivers Y. The revision process forces alignment between claim and evidence.

**Observable pattern**: Papers that resolved their identity crises BEFORE submission were accepted. Papers whose identity was still evolving at submission were rejected. The number of pre-submission rewrites correlates with acceptance — not because rewrites are inherently good, but because they indicate the identity discovery happened in the writing room rather than during peer review.

**Rule**: After rejection, don't just address specific reviewer comments. Ask: "What does this paper claim to be about, and does the evidence support that claim?" If not, the next submission needs a structural rewrite, not a revision.

---

## Principle 12: The Student Draft Is Material, Not the Paper

The student's initial comprehensive draft is valuable raw material, not a failure to be fixed. The issue is not that students write too much — it's that knowing WHAT to keep requires understanding the paper's competitive framing, which is a skill developed through experience.

**The division of labor**: Student writes comprehensively → Advisor restructures → Advisor compresses → Joint polishing. Students should write comprehensive first drafts without self-censoring. Asking students to "be more concise" in their first draft is counterproductive — it eliminates material the advisor might need.

---

## Principle 13: Measurement Papers Have Stable Identities

Papers where the contribution is "what we found" (measurement/evaluation) have stable identities determined by the research questions. Papers where the contribution is "what we built" (systems) require discovering HOW to position the technical contribution through writing.

**Implication for advising**: Less experienced writers can succeed with measurement papers (stable identity, question-driven structure). Systems papers require framing skill that develops through experience — they benefit from early advisor involvement in framing.

---

## Principle Summary

| # | Principle | Impact |
|---|-----------|--------|
| 1 | Introduction-twice (Draft 0 → Evaluation → Final intro) | High — prevents both frameless evaluation and overcommitment |
| 2 | Named over vague | High — precision correlates with acceptance |
| 3 | What → Why → So-What headings | High — enables skim-reading |
| 4 | Compress after expanding | Medium — improves focus |
| 5 | Structural rewrites over polishing | High — fundamental to the process |
| 6 | Labeled paragraphs as narrative contracts | Medium — stabilizes structure |
| 7 | Problem-first, not method-first | High — determines competitive frame |
| 8 | Takeaway paragraphs | Medium — aids skim-reading |
| 9 | Dual evaluation for dual claims | Medium — prevents evaluation confusion |
| 10 | Venue-specific adaptation | Medium — surface conventions matter |
| 11 | Rejection drives abstraction | High — explains multi-venue journeys |
| 12 | Student draft is material | Meta — defines collaboration model |
| 13 | Measurement vs. systems identity stability | Meta — determines advising strategy |
| 14 | Technical claims require citations | High — uncited claims read as fluff |

---

## Principle 14: Technical Claims Require Citations

Every technical claim in a paper must be grounded with a citation or an explicit cross-reference. When section N references content that was established with citations in section M, it must either carry forward the relevant `\cite{}` commands or use an explicit forward/backward reference (`\S\ref{}`). Uncited technical claims — no matter how well-established — read as unsupported assertions to reviewers.

**Common violation**: A design section restates failure modes or properties described in the background section but drops all the citations that supported those claims. The result looks like the authors are asserting without evidence.

**Rule**: After drafting any section, scan for technical claims (failure modes, properties of algorithms, known limitations of baselines). Each must have either a citation or an explicit cross-reference to the section where the citation lives.

---

## How to Apply These Principles

For **writing feedback**: Given a draft, identify which principles are violated. If the introduction leads with "ML has shown impressive results...", flag Principle 7. If section headings are descriptive, flag Principle 3. If technical claims lack citations, flag Principle 14.

For **advisor simulation**: Apply in order: Principle 1 (check whether the introduction promises match evaluation evidence — if not, rewrite the introduction from scratch) → Principle 7 (reframe problem-first) → Principle 3 (rewrite headings) → Principle 2 (replace generic terms) → Principle 14 (verify citations) → Principle 4 (compress).
