# Self-Diagnostic: Design Section

## Source
Derived from design rhetorical move analysis across 6 papers (see `section_rhetorical_moves/design.md` and `argument_evolution/`).

---

## Structure
- [ ] Does the section open with the **system's core abstraction** (named, defined)?
- [ ] Is there an **overview/architecture figure** early in the section?
- [ ] Does each subsection correspond to a **component in the overview figure**?
- [ ] Are subsection headings **claim-first** (e.g., "Nondeterminism as a first-order requirement") rather than **descriptive** (e.g., "Abstract NFA")?

## Design Justification
- [ ] For every major design choice, is there a **"why" argument**?
- [ ] Does the section explain **why alternatives were rejected** (not just what was chosen)?
- [ ] Is the justification grounded in **empirical observation** or **requirement analysis**, not just intuition?

## Abstraction vs. Implementation
- [ ] Does the section lead with **user-facing abstractions** (APIs, interfaces, programming model)?
- [ ] Are implementation details **subordinate to** the abstraction explanation?
- [ ] Could a reader understand the design **without reading the implementation section**?

## Terminology
- [ ] Is every technical term **defined on first use**?
- [ ] Is the system name used **consistently** (no accidental name variants)?
- [ ] Are there any **generic terms** that should be replaced with named mechanisms? (Principle 2)

## Audience Calibration
- [ ] Is the section calibrated for the **target venue's audience**?
- [ ] Are there **tutorial paragraphs** explaining concepts the audience already knows? (Delete them — Principle 4)
- [ ] Does the section use **venue-appropriate conventions** (\smartparagraph for systems, method-naming for ML)?

## The What → Why → So-What Test (Principle 3)
For each subsection, check:
- [ ] Does the heading state WHAT the component does? (minimum)
- [ ] Does the heading argue WHY this design choice? (better)
- [ ] Does the heading state the SO-WHAT implication? (best)
