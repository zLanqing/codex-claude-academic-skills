# Writing an Introduction: The 6-Move Sequence

## Overview

An effective introduction follows a 6-move sequence. Each move has a specific function. Missing a move weakens the paper; getting the order wrong confuses the reader.

### The Introduction Is Written Twice

**Draft 0** is written early — before the evaluation — as a framing scaffold. It covers Moves 1–5 (Stakes through Contributions) in rough form. Its purpose is to set guardrails: what is the paper trying to show? Draft 0 clarifies thinking and constrains what experiments need to be run. It is explicitly disposable.

**The final introduction** is rewritten from scratch after the evaluation is complete. Now Move 6 (Results Preview) can be filled with real numbers, and Moves 3–5 can be sharpened to match what the evidence actually supports. The final introduction promises exactly what the paper delivers — no more, no less. Draft 0 is reference material for the rewrite, not a starting point for editing.

---

## Move 1: Stakes

**Function**: Establish why the domain matters to the reader.

**How to do it**: Name specific actors (users, operators, policymakers) or specific applications (video, gaming, cloud services). Anchor with a concrete number if possible (dollar amounts, user counts, scale of the problem).

**The rule**: Never open with the technology. "ML has shown great promise..." is a rejected-paper opening. Start with the PROBLEM.

**Test**: Would a domain expert at the target venue care about your opening sentence?

---

## Move 2: Problem Gap

**Function**: Identify the specific gap between current practice and what is needed.

**How to do it**: The gap must be STRUCTURAL, not quantitative. Not "existing tools aren't good enough" but "existing tools are fundamentally limited because they assume X, which doesn't hold when Y."

**Pattern**: Number the limitations. "Three fundamental limitations: (i) ... (ii) ... (iii) ..." Each limitation should map to a specific design choice in your system.

**Test**: Are existing approaches NAMED (not "prior work" or "existing methods")?

---

## Move 3: Key Abstraction

**Function**: Introduce the paper's defining intellectual contribution as a named concept.

**How to do it**: Coin a term that captures your core insight. Make it a compound noun phrase, ideally with an architectural metaphor. Examples of the pattern (not from specific papers): "external termination layer," "progressive disaggregation," "intrinsic evaluation framework."

**Critical insight**: The key abstraction appears ONLY in final versions of papers. It is discovered through writing, not planned in advance. If you don't have one yet, that's normal — it will emerge as you write the evaluation and design sections.

**Test**: Is the name memorable? Would other researchers cite it? Does it distinguish your approach from ALL existing categories?

---

## Move 4: Design Intuition

**Function**: Give the reader a one-paragraph mental model of how the system works.

**How to do it**: One paragraph maximum. No algorithmic details. Describe the system as a pipeline or architecture: "Two-stage framework: (1) X, (2) Y." This is the "elevator pitch."

**Test**: Can a reader understand the high-level operation from this single paragraph? Is there an overview figure that maps to the section structure?

---

## Move 5: Contributions

**Function**: Enumerate what the paper delivers.

**How to do it**:
- Always numbered or bulleted
- Each item starts with a **bold label** (e.g., "Learning problem.", "Design.", "Evaluation.")
- Each item states a CLAIM, not a process: "We show that X" not "We propose X"
- Each item has a matching evaluation subsection (Principle 1)

**Test**: Does each contribution have evidence you can point to? If not, it's an aspiration, not a contribution.

---

## Move 6: Results Preview

**Function**: Anchor the introduction with concrete numbers from the evaluation.

**How to do it**: Include a headline number (e.g., "2–4× improvement") and reference a headline figure. This move is left blank in Draft 0 and filled only in the final introduction — after the evaluation is complete.

**Test**: Are the numbers specific and defensible? Do they match what the evaluation section actually shows?

---

## Accepted vs. Rejected: What's Different?

| Element | In accepted papers | In rejected papers |
|---------|-------------------|-------------------|
| Stakes | Specific actors, specific applications | Vague ("ML is transforming...") |
| Problem gap | Structural limitation, numbered | Abstract or quantitative only |
| Key abstraction | Named, memorable, citable | Unclear or missing |
| Contributions | Claim-first, with evidence pointers | Process descriptions ("We propose...") |
| Results preview | Specific numbers from evaluation | Vague or missing |

**The pattern**: Papers that resolved their identity (key abstraction + contribution framing) before submission were accepted. Papers whose framing was still vague at submission were rejected.

### Learning the Moves from Papers You Read

The six-move sequence is not just a writing template — it is also a **reading lens**. When doing deep reading (Pass 3+ in the [literature-survey-skill](https://github.com/SNL-UCSB/literature-survey-skill)), analyze the introductions of the strongest papers in your area: identify each move, note how the authors execute it, and extract the specific craft choices they make. Which concrete actors do they name in the Stakes? How do they phrase the structural gap? What is their key abstraction's name, and when in the revision history did it appear?

The craft patterns you extract from papers you read become reference material for your own writing. The best way to learn what a strong Move 2 (Problem Gap) looks like at SIGCOMM is to dissect the Problem Gaps of three accepted SIGCOMM papers — not to read a generic guide. The move sequence tells you *what* each move must accomplish; the craft extractions from your literature survey show you *how* the best authors in your field accomplish it.

---

## Venue Variations

| Move | Systems (SIGCOMM/NSDI) | ML (NeurIPS/ICLR) |
|------|----------------------|-------------------|
| Stakes | Named stakeholders + domain specifics | Broader applicability claims |
| Problem Gap | Structural limitations (numbered) | Benchmark inadequacy or method gap |
| Key Abstraction | System architecture name | Method/framework name |
| Design Intuition | Pipeline description | Algorithm sketch |
| Contributions | Labeled paragraphs + bold labels | Prose-integrated or bulleted |
| Results Preview | Specific metrics with numbers | Benchmark improvements |
