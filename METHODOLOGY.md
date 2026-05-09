# Methodology: The Two-AI Verification Process

This document explains how the Cameron Unified Framework was developed
and why the central repository is structured as it is.

---

## The problem this methodology solves

AI language models produce compelling narrative. They connect ideas,
find analogies, and generate physically motivated language at high
speed. They also produce errors — dimensional inconsistencies,
incorrect numbers, claims presented as derivations that are actually
postulates, and narrative symmetry substituted for mathematical
precision.

A single AI tool working alone on a theoretical physics framework
will produce a document that reads well and contains errors that are
not obvious to a non-specialist reader.

The two-AI methodology addresses this directly.

---

## How it worked

**Gemini (Google)** was used for theoretical synthesis:
- Building physical intuition and connecting ideas across the framework
- Writing the formal derivations document and FAQ
- Producing narrative accessible to a non-specialist reader
- Generating the Mathematica computation script

**Claude (Anthropic)** was used for computational verification:
- Checking every equation for dimensional consistency
- Computing specific numerical predictions and comparing to measurement
- Identifying where claims were postulates rather than derivations
- Documenting failures alongside successes

The two tools worked on the same framework from different directions.
Errors identified by the Claude repository were sent back to Gemini
for correction. The correction history is documented in `COMPARISON.md`.

---

## The correction history

Starting from Version 1 of the Gemini formal derivations document,
Claude identified eleven specific errors:

| Error | V1 | Final |
|---|---|---|
| H = γmc² (not zero) | ✗ | ✓ |
| Neutron weak decay correct | ✗ | ✓ |
| LMC velocity 281 km/s | ✗ | ✓ |
| ρ ∝ R⁻² rotation code | ✗ | ✓ |
| Spin equation derived | ✗ | ✓ |
| Spin equation dimensionally correct | ✗ | ✓ |
| Wave equation labelled postulate | ✗ | ✓ |
| GW170817 with specific numbers | ✗ | ✓ |
| Perihelion 3:2:1 ratio correct | ✗ | ✓ |
| Beam deflection discontinuity | ✗ | ✓ |
| Speculation removed | ✗ | ✓ |

**Score: 0/11 correct in V1 → 11/11 correct in the final version.**

The spin section (Section II.5) achieved 4/4 correct in its first
full draft after structured instructions — the fastest correction
cycle in the project.

Gemini's self-diagnosis on the perihelion correction:
*"Claude caught me red-handed trying to force narrative symmetry
where the physics demanded strict mathematical precision."*

---

## The two principles

Two principles governed every decision about what to include and
how to describe it:

**"The number has to be able to come out wrong."**

Every claim that can be expressed numerically was expressed
numerically, and the number was checked. The failures — the six
open gaps in `disputes/what_doesnt_work.md` — are documented
because their presence makes the verified results trustworthy.

**"The word has to mean what it says."**

The CMB is maximum entropy, thermally incoherent radiation. Calling
it a "cosmic laser" inverts its physical character. The Cameron
framework classifies all early universe emission events by sector
(real/imaginary/mixed) and entropy character — a two-axis system
that gives each event a precise identity. See Section IX.8 of the
contemplation section for the complete terminology standard.

---

## Why this methodology is useful beyond this project

The combination of narrative AI and verification AI is a general
tool for theoretical work. The narrative tool produces the ideas
quickly. The verification tool catches the errors before they become
embedded. The iteration between them produces something neither
could produce alone.

The correction history in `COMPARISON.md` is the evidence that
this works. It is preserved in the archive repositories so that
future researchers can see not just what the framework claims but
how those claims were stress-tested.

---

*For the full correction history see: `COMPARISON.md`*  
*For the open problems see: `disputes/what_doesnt_work.md`*
