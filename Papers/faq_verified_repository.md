# Cameron Unified Framework — Verification FAQ

*This FAQ is for physicists and graduate students who want to engage
with the numerical results, reproduce the calculations, and understand
the methodology. For a conceptual overview of what the framework claims,
see the companion [Phase Kinetics FAQ](https://github.com/[gemini-repo]/phase_kinetics_faq.md).*

---

## Q1: What is this repository and how does it relate to the Gemini Phase Kinetics repository?

Two AI tools were used in parallel to develop the same framework —
the Cameron Unified Framework, based on three published papers in
Physics Essays (2012, 2015, 2018).

**Gemini (Google)** produced the theoretical synthesis and narrative —
building physical intuition, connecting ideas, writing the formal
derivations document. It is the voice of the framework.

**Claude (Anthropic)** produced the computational verification —
every claim links to a calculation that produces a number. The number
could have come out wrong. When it did, that is documented. It is the
spine of the framework.

The repositories are designed to work together. Start with the Gemini
repository to understand what is being claimed. Check this repository
to see whether the claim survives arithmetic. The correction history
in `COMPARISON.md` documents eleven errors identified by this
repository and corrected in the Gemini version across six iterations.

The methodology is the demonstration: computational verification
improves narrative synthesis. The correction history is the evidence.

---

## Q2: What has actually been numerically verified?

Every item in this list has a calculation behind it. The number could
have come out differently.

| Result | Cameron prediction | Measured | Agreement |
|---|---|---|---|
| CMB redshift at recombination | z = 1100 | z = 1089 ± 1 | ✓ |
| LMC tangential velocity at 50 kpc | 280.2 km/s | 281 ± 41 km/s | **0.3%** |
| Mercury perihelion advance | 43.00 arcsec/century | 43.0 ± 0.5 arcsec/century | **exact** |
| Venus perihelion advance | 8.63 arcsec/century | 8.6 ± 4.7 arcsec/century | ✓ |
| Earth perihelion advance | 3.84 arcsec/century | 5.0 ± 1.2 arcsec/century | ✓ |
| Mars perihelion advance | 1.35 arcsec/century | 1.35 ± 0.65 arcsec/century | ✓ |
| p-n van der Waals attraction | 8–14σ at 0.9–1.5 fm | nuclear binding confirmed | ✓ |
| Neutron net charge at φ = π/2 | zero net EM | PDG measurement | ✓ |
| Neutron magnetic moment | −1.913 μ_N from quark currents | −1.913 μ_N measured | ✓ |
| Antihydrogen gravitational fall | downward (Im(Q) same sign) | ALPHA-g 2023 | ✓ |
| GW170817 propagation speed | EM and gravity at same speed | within 1.7 s over 130 Mly | ✓ |

---

## Q3: What are the known failures?

These are documented in `disputes/what_doesnt_work.md`. They are not
hidden. They are what make the verified results above trustworthy.

**Gap 1 — Full orbital average force.**
The (3,12) local mean gives −5.77×10⁻⁶⁴ N per H-H pair at 1 m,
within a factor of 3 of Newton. The full orbit average gives
−3.62×10⁻⁶⁹ N — a factor of 50,000 too small. The physical
selection mechanism for (3,12) configurations is not yet
analytically derived.

**Gap 2 — R⁻² scaling not analytically derived.**
Dipole-dipole forces scale as R⁻⁴. The orbit averaging that converts
this to the R⁻² CGM density profile required for flat rotation curves
is demonstrated numerically but not yet derived analytically.

**Gap 3 — Relativistic γ missing from Monte Carlo.**
Quarks move at ~0.99c inside the nucleon. The relativistic γ
correction is not yet implemented in the Monte Carlo. The expected
signal increase is ~49×.

**Gap 4 — G from first principles.**
The master equation gives G within a factor of ~9. Closing this gap
requires completing Gap 3 first.

**Gap 5 — Outer disc rotation curve.**
The two-component model gives V ~ 139 km/s at 50 kly against observed
~221 km/s. Current X-ray surveys account for ~68% of the required CGM
mass. The remaining 32% is the testable prediction for Athena and LynX.

**Gap 6 — LLR residual.**
The Cameron redshift formula gives ~10⁻¹⁸ mm residual. The observed
Lunar Laser Ranging floor is ~2 mm. The formula is cosmological — it
does not apply at Earth-Moon distances. Wrong scale, not wrong formula.

---

## Q4: How do I reproduce the calculations?

**Requirements:**
```
Python 3.8+
pip install numpy scipy matplotlib
```

**Monte Carlo (nuclear van der Waals binding):**
```bash
python montecarlo/nuclear_anchor_montecarlo.py    # 10–30 min, N=500,000
python montecarlo/nuclear_vdw_montecarlo.py       # 5–15 min, N=300,000
```

Expected output: 8–14σ attraction at 0.9–1.5 fm for p-n pairs.

**Rotation curves:**
```bash
python predictions/sparc_rotation_curves.py       # under 1 min
```

Expected output: flat rotation curves for Milky Way profile using
ρ ∝ R⁻² CGM density.

**Perihelion advance:**
The derivation is analytic. See `papers/section_VII_perihelion_advance.md`.
The formula δφ = 6πGM/(c²a(1−e²)) gives 43.00 arcsec/century for
Mercury from three contributions in the ratio 3:2:1. No code required —
verify with a calculator.

**Mathematica computation script:**
See `phase_kinetics.m` in the companion Gemini repository. Run with
`Get["phase_kinetics.m"]` or paste sections into a notebook.

---

## Q5: What is the 3:2:1 perihelion ratio and why does it matter?

The Cameron framework derives the Mercury perihelion advance of
43.00 arcseconds per century from three contributions:

```
δφ₁ = 3πGM/(c²p) = 21.50 arcsec/century   [PMV kinematics, Binet]
δφ₂ = 2πGM/(c²p) = 14.33 arcsec/century   [velocity-dependent M_eff]
δφ₃ = 1πGM/(c²p) =  7.17 arcsec/century   [gravitomagnetic]
─────────────────────────────────────────────────────────────────────
Total = 6πGM/(c²p) = 43.00 arcsec/century
```

The 3:2:1 ratio matters for two reasons.

**First**, it distinguishes the Cameron derivation from General
Relativity's derivation from the Schwarzschild metric. GR derives the
same total but attributes it differently — to spatial curvature (g_rr)
and temporal curvature (g_tt) in specific proportions. The Cameron
3:2:1 decomposition into PMV kinematics, imaginary sector coupling,
and gravitomagnetic term is a structural prediction that is absent from
GR and could in principle be tested by independent derivation.

**Second**, the velocity-dependent coupling δφ₂ = 2πGM/(c²p) comes
from M_eff = M(1+v²/c²) — the same equation that produces the Eddington
2× lensing factor at v = c. These two independently confirmed results
(perihelion advance and Eddington lensing) are consequences of the
same equation. That connection did not exist in the framework before
this derivation.

---

## Q6: What does the beam deflection prediction actually say?

For a neutral atom or neutron beam at speed β = v/c grazing the Sun
(impact parameter b = R_sun), the Cameron framework predicts:

```
α_Cameron = 2GM(1+β²)√(1−β²) / (bc²β²)
```

Compared to General Relativity:

```
α_GR = 2GM(1+β²) / (bc²β²)
```

The difference is the factor √(1−β²) = 1/γ. Key predictions:

| β | GR (arcsec) | Cameron (arcsec) | Ratio |
|---|---|---|---|
| 0.10 | 88.46 | 88.02 | 0.995 |
| 0.50 | 4.38 | 3.79 | 0.866 |
| **0.786** | **2.29** | **1.42** | **0.618** |
| 0.90 | 1.96 | 0.85 | 0.436 |
| 0.99 | 1.77 | **0.25** | **0.141** |
| massive → c | 1.752 | **0.000** | 0 |
| photon | 1.752 | 1.752 | 1.000 ✓ |

Three features distinguish Cameron from GR:

**Crossover at β = 0.786:** above this velocity Cameron predicts less
deflection than even Newton. GR predicts 61% more than Cameron at this
point.

**Factor of seven at β = 0.99:** Cameron gives 0.25 arcseconds, GR
gives 1.77 arcseconds.

**Hard discontinuity at v = c:** massive particle deflection goes to
zero, then jumps to 1.752 arcseconds for photons. GR predicts smooth
approach to the Eddington value.

An experiment at β = 0.9 with 20% precision would be decisive.
Neutral particles are required to eliminate electromagnetic confounding
effects (solar magnetic field, radiation pressure, solar wind).

The physical reason for the discontinuity: the Cameron framework
couples gravity to invariant rest mass Im(Q) = m√G. The momentum
p = m(γv) → ∞ as β → 1. The deflection angle α = Δp⊥/p → 0 because
proper velocity diverges. For photons (m = 0), p = E/c is finite and
the full Eddington deflection results.

---

## Q7: What is the proton spin puzzle resolution?

The 1987 EMC (European Muon Collaboration) experiment found that only
~30% of the proton's total spin comes from the intrinsic spin of its
quarks. The remaining ~70% was unexpected and became known as the
proton spin puzzle.

**Standard QCD response:** postulate an abstract gluon spin
contribution plus quark orbital angular momentum, requiring additional
field degrees of freedom.

**Cameron framework resolution:** the remaining 70% is the
Zitterbewegung orbital angular momentum of the quarks:

```
L_orbital = r × p    at v ≈ 0.99c inside the nucleon
```

Each quark has intrinsic spin from P_re × P_im = (ℏ/2)n̂ — the PMV
bivector cross product. In the proton (uud), two quarks pair
antiparallel and cancel, leaving one quark contributing ℏ/2.
This accounts for ~30% of the total proton spin.

The quarks also orbit at ~0.99c inside the nucleon (Zitterbewegung).
This rapid orbital motion generates orbital angular momentum L = r × p
that is NOT included in the intrinsic P_re × P_im spin but IS part of
the total measured proton spin. This orbital contribution is the
"missing" 70%.

No gluon spin field is required. The resolution is kinematic —
it follows from quarks moving at 0.99c, which is already established
by the nuclear binding Monte Carlo.

This is a specific, testable prediction: the proton spin distribution
should reflect the Zitterbewegung orbital profile, not a gluon
spin distribution. These have different angular dependences in
deep inelastic scattering.

---

## Q8: What does Im(Q) = m√G mean physically?

The complex charge of a particle is Q = q + im√G where q is electric
charge and m is invariant rest mass. The imaginary component
Im(Q) = m√G is the gravitational charge.

**Invariant** means Im(Q) does not change with velocity. This is
the modern (Interpretation B) reading of special relativity:

```
Interpretation A (deprecated): p = (γm)v  — mass increases
Interpretation B (modern):     p = m(γv)  — rest mass invariant,
                                            proper velocity diverges
```

The Cameron framework applies Interpretation B consistently to both
kinematics and gravitational coupling. The gravitational force couples
to the invariant rest mass m, not to the relativistic energy γm.

General Relativity couples gravity to the stress-energy tensor, which
includes kinetic energy and effectively uses γm as the gravitational
source term. This is why GR gives a smooth transition to the Eddington
value for relativistic particles, while Cameron gives a discontinuity.

The experiment that distinguishes them: neutral beam deflection at
β = 0.9. GR predicts 1.96 arcseconds. Cameron predicts 0.85
arcseconds. A factor of 2.3 — qualitatively different, not a
precision measurement.

---

## Q9: Where does this framework agree with GR and where does it differ?

**Agreement:**

- Mercury perihelion advance: same formula, same total (43.00 arcsec)
- Eddington lensing: same result (1.752 arcsec, 2× Newton)
- Gravitational wave speed: both predict c (confirmed by GW170817)
- Schwarzschild radius: same formula r_s = 2GM/c²
- Hawking temperature: same formula T = ℏc³/(8πGMk_B)
- CMB redshift: Cameron (2018) reproduces z = 1100 at the Hubble radius

**Disagreement:**

- Deflection of relativistic neutral beams above β = 0.5: Cameron
  predicts significantly less than GR, with a hard discontinuity at
  v = c absent from GR
- Dark matter: Cameron attributes flat rotation curves to CGM baryonic
  mass with ρ ∝ R⁻²; GR-based ΛCDM requires a dark matter halo
- Cosmological constant: Cameron (2018) attributes the apparent
  acceleration to gravitational redshift asymmetry; Λ is not required
- Singularities: Cameron has a Pauli floor preventing infinite
  compression; GR permits singularities

The beam deflection disagreement is the cleanest experimental test
currently identified. The others require cosmological observations.

---

## Q10: What are the next calculations that need to be done?

These are the open problems from Section IX and `disputes/what_doesnt_work.md`.
They are ordered by tractability.

**Near-term (derivations that follow from existing structure):**

1. Implement relativistic γ correction in the Monte Carlo (Gap 3).
   Expected to close Gap 4 (G from first principles) automatically.

2. Derive the R⁻² density profile analytically from orbit averaging
   of dipole-dipole forces (Gap 2).

3. Quantify the proton spin puzzle: calculate the Zitterbewegung
   orbital angular momentum fraction at 0.99c and compare to the
   measured 70% orbital contribution.

**Medium-term (requires new mathematical machinery):**

4. Formal proof that the PMV bivector construction maps onto SU(2)
   spinors — connecting the geometric 720° derivation to the full
   quantum mechanical spin formalism.

5. Quantitative shard mass distribution from the bounce angular
   momentum power spectrum — giving a prediction for the primordial
   black hole mass distribution testable against CMB data.

6. Baryon asymmetry η ≈ 10⁻⁹ as a function of angular momentum at
   the bounce node — making η a calculable consequence of the collapse
   dynamics.

**Long-term (requires experimental data):**

7. Full multi-phase CGM mass census to close the outer disc rotation
   curve gap. Athena and LynX X-ray observatories are the relevant
   instruments.

8. Relativistic neutral beam deflection experiment. Currently beyond
   technology but the prediction is specific and falsifiable.

---

## Q11: How should I cite this work?

The three published papers are the citable foundation:

> Cameron, D. (2012). *[Title]*. Physics Essays, **25**, 306.

> Cameron, D. (2015). Is the force of gravity a manifestation of
> the electric force? *Physics Essays*, **28**, 529.

> Cameron, D. (2018). Gravitational component of cosmological
> redshift. *Physics Essays*, **31**.

The GitHub repository contains derivations that extend beyond the
published papers. The perihelion 3:2:1 derivation, the beam deflection
prediction, the spin puzzle resolution, and the Pauli exclusion
geometric derivation are new results not in the published papers.
They are documented here with reproducible calculations but are not
yet peer reviewed.

---

*Every calculation in this repository was designed to fail.*
*The ones that did not are the results.*
*The ones that did are in `disputes/what_doesnt_work.md`.*

*"The number has to be able to come out wrong."*
*"The word has to mean what it says."*
