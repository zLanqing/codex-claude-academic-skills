# Writing a Design Section: The 5-Move Sequence

## Overview

The design section answers "How should the reader think about this system?" before "How does it work internally?" Lead with the abstraction, not the implementation.

---

## Move 1: Abstraction Introduction

**Function**: Present the user-facing mental model before any implementation detail.

**How to do it**: Open with what users reason about, not what the system computes. Name the core abstraction — this is the intellectual contribution. The implementation is the engineering contribution.

**Test**: Does the section open with the system's core abstraction (named, defined)?

---

## Move 2: Design Justification (The "Why" Move)

**Function**: Explain why this particular design was chosen over alternatives.

**How to do it**: Often takes the form of a negative result: "We tried the obvious approach (linear method / monolithic design / single-stage pipeline) and it fails because X." This makes the chosen design feel INEVITABLE rather than arbitrary.

**Test**: For every major design choice, is there a "why" argument? Does the section explain why alternatives were rejected?

---

## Move 3: Component Architecture

**Function**: Decompose the system into named stages/modules.

**How to do it**: Always a pipeline or structured flow the reader can trace. Each component gets a name that reflects its function. Component names become the vocabulary the evaluation section uses.

**Pattern**: Overview figure → subsection per component. Each subsection explains one component.

---

## Move 4: Key Design Decision (The "Knob" Move)

**Function**: Identify the critical parameter or trade-off the user controls.

**How to do it**: Every non-trivial system has at least one configurable parameter whose existence demonstrates the system isn't one-size-fits-all. Name it, explain it, show how it affects behavior.

**Test**: Is there a parameter whose adjustment reveals a meaningful trade-off?

---

## Move 5: Robustness / Edge Cases

**Function**: Address what happens when assumptions fail.

**How to do it**: Often added late, per reviewer or advisor feedback. Common elements: safety mechanisms for edge cases, sensitivity to key parameters, handling of distribution shift.

**Its presence signals defensive design awareness. Its absence is a common reviewer concern.**

---

## Anti-Patterns to Avoid

1. **Opening with infrastructure**: Don't start with an implementation detail ("Generating realistic data..."). Start with the abstraction ("Programming model for expressing...").

2. **Formal math replacing intuition**: Dense mathematical formulation without a pipeline narrative. The math should survive but be subordinated to the flow.

3. **Missing the "why"**: Presenting "Abstract X / Concrete X" — the WHAT without the WHY. Add the justification: "Why does the simple approach fail?"

---

## The What → Why → So-What Test (Principle 3)

For each subsection, check which level the heading achieves:

- **WHAT** (minimum): "System Architecture" — names the topic
- **WHY** (better): "Why do linear approaches fail?" — argues for the design
- **SO-WHAT** (best): "Nondeterminism as a first-order requirement" — states the implication

Target: SO-WHAT headings for all subsections.
