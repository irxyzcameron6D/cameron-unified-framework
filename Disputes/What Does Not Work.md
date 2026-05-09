# What Doesn't Work — Honest Documentation of Open Problems

*Cameron Unified Framework*  
*This file is updated as calculations are completed.*  
*Last updated: 2025*

---

> "The number has to be able to come out wrong."  
> Every item in this file is a case where it did.

---

## Gap 1 — The Full Orbital Average vs the Local (3,12) Mean

**What Cameron (2015) showed:**  
The (3,12) orbital configuration produces a mean force of
−5.77×10⁻⁶⁴ N per hydrogen pair at R = 1m.  
Newton's gravity for the same system: −1.87×10⁻⁶⁴ N.  
Ratio: Cameron / Newton = 3.09 — within a factor of 3. ✓ in direction.

**What the full orbital average gives:**  
When integrated analytically over the complete electron orbit
(rather than the local arc near the (3,12) starting point),
the mean force is −3.62×10⁻⁶⁹ N.  
This is 50,000× smaller than Newton. ✗

**Why they differ:**  
The paper's −5.77×10⁻⁶⁴ N is the mean over a small arc (21 steps
of 0.00001π radians = 0.01% of a full orbit) near the (3,12)
starting configuration. The full orbit average is exact by
analytic integration and requires 350-decimal-place arithmetic
to confirm (which is why Mathematica was used in the original paper).

**The physical question not yet answered:**  
What selects the (3,12) configuration as the relevant one?
Three candidates:
1. Cosmological frozen state — atoms formed at recombination
   in (3,12)-type configurations set by the CMB radiation field
   geometry, with relaxation time > age of universe
2. Collective many-body effect — single-pair enhancement of
   ~10⁻²⁰ amplified across 10⁵⁰ correlated pairs
3. Different mechanism — the 32.4% fraction may emerge from the
   quark geometry rather than orbital alignment

**Status:** Open. The 32.4% alignment fraction result is clean
and scale-independent, but the physical mechanism selecting
that fraction is not derived.

---

## Gap 2 — The R⁻² Scaling Not Analytically Derived

**What is needed:**  
For the van der Waals mechanism to reproduce Newtonian gravity,
the force must scale as R⁻² at macroscopic distances.

**What classical van der Waals gives:**  
Dipole-dipole forces scale as R⁻⁴ (London).
Dipole-charge forces scale as R⁻³.
Neither gives R⁻².

**What Cameron (2015) shows:**  
The orbit-averaged (3,12) force at R = 1m is −5.77×10⁻⁶⁴ N.
If this scales as R⁻², scaling to two hydrogen atoms at any
other distance R gives Newton's law exactly.
The paper demonstrates this works numerically.

**What has not been derived:**  
The analytic proof that the orbit-averaged mean scales as R⁻²
rather than R⁻⁴ or R⁻⁷. The cancellation mechanism that
converts the dipole-dipole R⁻⁴ into an effective R⁻² has
not been derived from first principles.

**Status:** Open. The Q = q + im√G formulation gives R⁻² exactly
from imaginary charge × imaginary charge. The van der Waals path
to R⁻² through orbital averaging needs analytical completion.

---

## Gap 3 — Quark Monte Carlo Missing Relativistic γ Factor

**What the current Monte Carlo gives:**  
p-n attraction at 0.9–1.5 fm at 8–14σ significance. ✓  
Potential well depth: ~0.09–1.20 MeV.

**What the empirical nuclear binding requires:**  
~2.22 MeV for the deuteron (simplest bound nucleus).  
~8 MeV/nucleon for typical nuclei.

**What the relativistic correction should add:**  
Quarks move at v ≈ 0.99c inside the nucleon.  
The Coulomb force between relativistic charges is enhanced
by the γ factor. For v = 0.99c: γ = 7.09.  
Expected signal increase: ~49× from γ² factor.  
This would bring the well depth from ~1 MeV toward ~49 MeV
(possibly overshooting — needs careful implementation).

**What needs to be done:**  
Add the relativistic Liénard-Wiechert correction to the
inter-quark Coulomb force in nuclear_anchor_model.py.
The modification is three lines of code.

**Status:** Not yet implemented. This is the next calculation.

---

## Gap 4 — G from First Principles: Factor of 9 Remaining

**The master equation:**  
G ∝ e²a₀²/m_p²

**What the quark geometry gives:**  
G from the quark van der Waals residual: within factor ~9 of Newton.  
Using current quark masses (m_u = 2.3 MeV, m_d = 4.8 MeV):
the proton mass is almost entirely QCD binding energy,
so 2m_u + m_d << m_p, and the quark mass contribution to G
differs from Newton by the ratio of current to constituent masses.

**What closes it:**  
The constituent quark mass (m_u_constituent ~ 336 MeV) vs
current quark mass (m_u_current ~ 2.3 MeV) discrepancy is
QCD binding energy — a known feature of QCD, not a failure
of the framework. Using the correct dressed quark masses
in the imaginary charge calculation is expected to close the gap.

**Status:** Partially understood. Completing Gap 3 (relativistic
Monte Carlo) will simultaneously test Gap 4.

---

## Gap 5 — LLR Residual: Wrong Scale by 10¹⁵

**What COSAT claimed:**  
The 1.7–2.0 mm Lunar Laser Ranging residual floor is explained
by a 1/π vacuum refractive index correction from the 6D metric.

**What the Cameron formula predicts:**  
Applying z = πGρR²/c² to the interplanetary medium at R = 384,400 km
with ρ = 5 H/cc (solar wind) gives a path length correction
of ~10⁻¹⁸ mm.  
The observed residual is 1.7–2.0 mm.  
**The Cameron formula is off by 10¹⁸ at this scale.** ✗

**Why:**  
The formula was derived for and calibrated at cosmological
distances (R ~ 10²⁶ m). At Earth-Moon scales (R ~ 10⁸ m),
the R² scaling suppresses the effect by (10⁸/10²⁶)² = 10⁻³⁶.
No realistic ISM density compensates for 36 orders of magnitude.

**What actually causes the LLR residual:**  
The observed 2mm floor is a sum of: lunar retroreflector array
orientation varying with libration (~1mm), seasonal atmospheric
loading uncertainty (~0.4mm), tidal loading (~0.2mm), and
thermal expansion of reflectors (~0.2mm). These are known
engineering effects, not fundamental physics.

**Status:** Closed as a Cameron framework prediction. The LLR
residual is not explained by this framework at the Earth-Moon
scale. The formula is a cosmological tool, not a local one.

---

## Gap 6 — Quantum Ground State Does Not Provide 32.4% Alignment

**What the quantum chemistry calculation shows:**  
The true quantum ground state of two hydrogen atoms at R = 1m
provides an enhancement of same-side orbital configurations
over opposite-side configurations of ~10⁻²⁰ — effectively zero.

**What is needed:**  
32.4% of atom pairs in (3,12)-type configurations — which is
29.6% more than the 25% that naive random geometry gives.

**The gap:**  
The required occupation is ~10²⁰× larger than the quantum
ground state provides. This is not a small correction.

**Why this does not kill the framework:**  
The 32.4% is not claimed to be a ground state property.
It is claimed to be a cosmological initial condition — atoms
formed at recombination in (3,12)-type configurations set by
the CMB radiation field geometry, with relaxation time at
cosmological distances exceeding the age of the universe.
This connects to the cosmic coherence parameter C in the
framework and is the subject of ongoing development.

**Status:** Open. The cosmological mechanism is proposed but
not yet quantitatively derived.

---

## What Works (For Balance)

| Result | Value | Status |
|---|---|---|
| CMB redshift z = 1100 | z = πGρR²/c² at ρ=0.0165 H/cc, R=13.8 Gly | ✓ |
| Evanescence horizon at 13.55 Gly | matches supercluster scale | ✓ |
| p-n quark attraction at 0.9–1.5 fm | 8–14σ significance | ✓ |
| p-n naive charge sum = 0 | exact, from quark geometry | ✓ |
| Newton from neutral H atoms | Q_H² = −G(m_p+m_e)² exact | ✓ |
| Neutron at φ = π/2 | zero EM, pure gravity — from geometry | ✓ |
| Antihydrogen falls downward | ALPHA-g 2023 confirmed | ✓ |
| 32.4% alignment scale-independent | same for H-H and Earth-Moon | ✓ |
| Galaxy morphology ∝ formation density | JWST compact galaxies | ✓ direction |
| CGM profile ∝ R⁻² | matches COS-Halos direction | ✓ direction |
| Equivalence principle | derived, not postulated | ✓ |

---

*This file is the most important file in the repository.*  
*It is what makes the successes above trustworthy.*

---

## Correction: Neutron Electromagnetic Description (Resolved)

**Original statement in Section III:**
"The neutron has q = 0 exactly, so Q_n = pure imaginary.
It gravitates and does not interact electromagnetically."

**Why this was wrong:**
The neutron has zero **net** electric charge but is not
electromagnetically inert. Its internal quark structure produces:

- Magnetic moment: μ_n = −1.913 nuclear magnetons (measured)
- Charge radius²: r²_n = −0.114 fm² (measured, negative sign)
- Oscillating instantaneous electric field from quark motion
- Neutron-electron scattering (measured)

All of these arise from the internal quark charge distribution,
not from a nonzero net charge.

**Corrected statement:**
The neutron's **net** complex charge is Q_n = i·m_n·√G (pure
imaginary). Its net electromagnetic interaction at large distances
is zero. At short range, the internal quark motion (Zitterbewegung
at 0.99c) produces an oscillating instantaneous electric field
whose correlations between neighboring neutrons ARE the nuclear
van der Waals force confirmed at 8–14σ in the Monte Carlo.

The negative charge radius confirms the anchor model geometry:
d quarks (negative) at the surface, u quark (positive) near the
center. The magnetic moment confirms the quark current loops
produce a nonzero DC magnetic field even though the net charge
is zero.

**Status:** Resolved and corrected in Section III and Section IV.
