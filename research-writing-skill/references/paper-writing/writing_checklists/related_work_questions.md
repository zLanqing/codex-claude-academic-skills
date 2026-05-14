# Self-Diagnostic: Related Work Section

## Source
Derived from related work analysis across 6 papers (see `section_rhetorical_moves/related_work.md`).

---

## Placement
- [ ] Is related work placed **after the evaluation** (systems venues: SIGCOMM, NSDI)?
- [ ] Or **integrated into the introduction/background** (ML venues: NeurIPS, ICLR)?
- [ ] Is the placement choice **deliberate** and **venue-appropriate**?

## Category Clustering (Move 1)
- [ ] Is prior work organized into **2-4 categories** (not a flat list)?
- [ ] Are categories named by **approach type** (e.g., "Crowdsourced / Controlled / Hybrid"), not by individual paper?
- [ ] Does each category contain **representative examples** (not exhaustive lists)?

## Per-Category Limitation (Move 2)
- [ ] For each category, is there a **specific limitation** stated?
- [ ] Is the limitation **structural** (fundamentally unable to do X) rather than **quantitative** (doesn't do X well enough)?
- [ ] Does the limitation connect to a **feature of your system** that addresses it?

## Positioning Sentence (Move 3)
- [ ] Is there a clear sentence that says: "Unlike X, our approach provides Y while maintaining Z"?
- [ ] Does the positioning sentence **name your key abstraction**?
- [ ] Is the positioning **honest** — does it acknowledge what you DON'T do?

## Anti-Patterns
- [ ] Is the section **under 10K chars**? (If longer, it's a survey, not a positioning section.)
- [ ] Are there **no tutorial paragraphs** (explaining what TCP is to a SIGCOMM audience)?
- [ ] Is the section a **limitation argument**, not a **literature review**?
- [ ] Does every cited work serve the purpose of **positioning your contribution** (not padding the bibliography)?

## Consistency Check
- [ ] Does the positioning sentence align with the **key abstraction** in the introduction?
- [ ] Are the baselines mentioned in related work the **same baselines** used in the evaluation?
- [ ] If a reviewer asks "how is this different from X?", does the related work **preemptively answer**?
