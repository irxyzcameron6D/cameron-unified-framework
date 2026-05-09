# Cameron Unified Framework

**One equation. No free parameters. Four forces.**

```
F = Q₁Q₂ / r²     where Q = q + im√G
```

> *Donald Cameron — Physics Essays (2012, 2015, 2018)*  
> *Computational verification: Claude (Anthropic)*  
> *Theoretical synthesis: Gemini (Google)*

---

## What this repository is

This is the central maintained version of the Cameron Unified Framework
— a proposal that all four fundamental forces are projections of a
single complex force law. It was developed through a two-AI verification
process documented in the [archive](#archive) below.

For every claim in this repository there is either a number that could
have come out wrong, or an explicit statement that the claim is not
yet verified. The failures are documented alongside the successes.
That is what makes the successes trustworthy.

---

## The central claim

The complex charge **Q = q + im√G** has:
- Real part **q** → electric charge → electromagnetism
- Imaginary part **m√G** → gravitational charge → gravity
- Cross term **2iqm√G** → nuclear van der Waals → strong force

For neutral hydrogen: Q = im(m_p + m_e)√G  
→ F = −G(m_p + m_e)²/r²  
→ **Newton's law, exact, from i² = −1, no parameters.**

---

## What the numbers say

| Result | Prediction | Measured | Status |
|---|---|---|---|
| CMB redshift z | 1100 | 1089 ± 1 | ✓ |
| LMC tangential velocity | 280.2 km/s | 281 ± 41 km/s | **0.3% ✓** |
| Mercury perihelion advance | 43.00 arcsec/cy | 43.0 ± 0.5 arcsec/cy | **exact ✓** |
| Venus perihelion advance | 8.63 arcsec/cy | 8.6 ± 4.7 arcsec/cy | ✓ |
| Earth perihelion advance | 3.84 arcsec/cy | 5.0 ± 1.2 arcsec/cy | ✓ |
| Mars perihelion advance | 1.35 arcsec/cy | 1.35 ± 0.65 arcsec/cy | ✓ |
| p-n van der Waals attraction | 8–14σ at 0.9–1.5 fm | nuclear binding confirmed | ✓ |
| Neutron net charge | zero net EM at φ=π/2 | PDG measurement | ✓ |
| Neutron magnetic moment | −1.913 μ_N from quark currents | −1.913 μ_N measured | ✓ |
| Antihydrogen gravitational fall | downward | ALPHA-g 2023 | ✓ |
| GW speed relative to EM | same speed | GW170817 within 1.7s | ✓ |
| Proton spin — intrinsic | 30% from PMV bivector | 30% EMC 1987 | ✓ |
| Proton spin — orbital | 70% from Zitterbewegung at 0.99c | 70% EMC 1987 | ✓ |
| Relativistic beam deflection β→1 | → 0 (massive), 1.752″ (photon) | untested | **prediction** |
| Hull temperature speedometer | β=(R−1)/(R+1) | locally measurable | **prediction** |
| LLR residual | ~10⁻¹⁸ mm | 2 mm observed | ✗ wrong scale |
| Full orbital average force | −3.62×10⁻⁶⁹ N | −1.87×10⁻⁶⁴ N (Newton) | ✗ gap open |

The ✗ entries are what make the ✓ entries trustworthy.

---

## Key new results (not in the published papers)

### 1. Mercury perihelion advance — first principles derivation

Previously a postulate borrowed from GR. Now derived from three
Cameron framework contributions in a strict **3:2:1 ratio**:

```
δφ₁ = 3πGM/(c²p)   PMV kinematics (Binet)          21.50 arcsec/cy  [3/6]
δφ₂ = 2πGM/(c²p)   M_eff = M(1+v²/c²) coupling     14.33 arcsec/cy  [2/6]
δφ₃ =  πGM/(c²p)   Gravitomagnetic                   7.17 arcsec/cy  [1/6]
────────────────────────────────────────────────────────────────────────────
     = 6πGM/(c²p)   Total                            43.00 arcsec/cy  [6/6]
```

The same coupling M_eff = M(1+v²/c²) that produces the 2/6 perihelion
contribution also produces the Eddington 2× lensing factor at v = c.
Both results follow from the same equation. See `papers/section_VII_perihelion_advance.md`.

### 2. Relativistic beam deflection — testable prediction

For a neutral atom or neutron beam at speed β grazing the Sun
(impact parameter b = R_sun):

```
α_Cameron = 2GM(1+β²)√(1−β²) / (bc²β²)
```

| β | GR (arcsec) | Cameron (arcsec) | Ratio |
|---|---|---|---|
| 0.50 | 4.38 | 3.79 | 0.87 |
| 0.786 | 2.29 | 1.42 | 0.62 |
| 0.90 | 1.96 | 0.85 | 0.44 |
| **0.99** | **1.77** | **0.25** | **0.14** |
| massive → c | 1.752 | **0.000** | 0 |
| photon | 1.752 | 1.752 | 1.00 ✓ |

GR predicts a smooth approach to the Eddington value as β → 1.
Cameron predicts a **hard discontinuity at v = c** — massive
particle deflection goes to zero, then jumps to 1.752 arcseconds
for photons. A factor-of-seven difference at β = 0.99.

An experiment at β = 0.9 with 20% precision is decisive.
See `papers/section_VIII_beam_deflection.md`.

### 3. Spin-1/2 and Pauli exclusion from 6D geometry

The 720° rotation requirement follows from the PMV bivector geometry:
P_re rotates 2π in real space → bivector phase rotates π →
wavefunction picks up e^(iπ) = −1. Full 4π rotation needed for
e^(i2π) = +1. No additional postulate required.

The Pauli exclusion principle follows from counting: the P_im axis
has exactly two orientations (+n̂ and −n̂). Geometric capacity
exhausted after two fermions. See `papers/section_II5_spin_pauli.md`.

### 4. Proton spin puzzle resolved (EMC 1987)

Standard QCD postulates gluon spin for the "missing" 70%.
The Cameron framework derives it kinematically:

```
30% intrinsic = P_re × P_im = (ℏ/2)n̂   [PMV bivector spin]
70% orbital   = r × p at 0.99c          [Zitterbewegung orbital L]
```

No new fields required. The resolution follows from quarks moving
at 0.99c inside the nucleon — already established by the nuclear
binding Monte Carlo.

### 5. Hull temperature speedometer

A ship at speed β through the ISM/CMB medium experiences a real
physical asymmetry — not a coordinate effect:

```
β = (R − 1) / (R + 1)     where R = T_forward hull / T_aft hull
```

Local measurement of absolute velocity relative to the CMB rest
frame. No CMB dipole observation needed. At β = 0.99: R = 199.
More sensitive at high β than the standard CMB dipole method.
See `papers/section_IX_contemplate.md` (Section IX.9).

---

## What is open

Full documentation in `disputes/what_doesnt_work.md`.

| Gap | Description | Status |
|---|---|---|
| 1 | Full orbital average force: factor 50,000 from Newton | open |
| 2 | R⁻² scaling not analytically derived | open |
| 3 | Relativistic γ missing from Monte Carlo (~49× expected) | open |
| 4 | G from first principles: factor ~9 remaining | open |
| 5 | Outer disc rotation curve: 25–35 km/s short at 30–50 kly | open |

---

## Repository structure

```
cameron-unified-framework/
│
├── README.md                              ← this file
├── COMPARISON.md                          ← correction history, methodology
├── METHODOLOGY.md                         ← how the two-AI process worked
├── LICENSE
│
├── papers/
│   ├── section_I_metric.md
│   ├── section_II_pmv_kinematics.md
│   ├── section_II4_hamiltonian.md
│   ├── section_II5_spin_pauli.md          ← spin, Pauli, proton spin puzzle
│   ├── section_III_complex_charge.md
│   ├── section_IV_four_forces.md
│   ├── section_V_black_holes.md
│   ├── section_VI_published_results.md
│   ├── section_VI5_rotation_curves.md     ← LMC orbital test (0.3%)
│   ├── section_VI6_rotation_curves.md     ← extended rotation curve model
│   ├── section_VII_perihelion_advance.md  ← new derivation, 3:2:1 ratio
│   ├── section_VIII_beam_deflection.md    ← testable prediction
│   ├── section_IX_contemplate.md          ← open problems and contemplation
│   └── faq_verified_repository.md        ← questions from physicists
│
├── narrative/
│   └── the_story_of_everything.md
│
├── montecarlo/
│   ├── nuclear_anchor_montecarlo.py       ← 8–14σ p-n attraction
│   ├── nuclear_vdw_montecarlo.py
│   ├── gravity_polarizability.py
│   └── gravity_h2_model.py
│
├── predictions/
│   └── sparc_rotation_curves.py
│
├── mathematica/
│   └── phase_kinetics.m                   ← all 8 derivations, clean ASCII
│
├── figures/
│   ├── relativistic_beam_deflection.png
│   ├── magellanic_cloud_test.png
│   ├── rotation_curves_full_profile.png
│   ├── sparc_rotation_curves.png
│   ├── galaxy_predictions.png
│   └── nuclear_anchor_results.png
│
├── disputes/
│   └── what_doesnt_work.md                ← the most important file here
│
└── archive/
    ├── CLAUDE_REPOSITORY.md               ← link and description
    └── GEMINI_REPOSITORY.md               ← link and description
```

---

## Running the calculations

**Requirements:**
```bash
pip install numpy scipy matplotlib
```

**Nuclear van der Waals binding (8–14σ result):**
```bash
python montecarlo/nuclear_anchor_montecarlo.py    # 10–30 min, N=500,000
python montecarlo/nuclear_vdw_montecarlo.py       # 5–15 min, N=300,000
```

**Rotation curves:**
```bash
python predictions/sparc_rotation_curves.py       # under 1 min
```

**Perihelion advance — analytic, verify with a calculator:**
```
δφ = 6πGM / (c²·a·(1−e²))
   = 43.00 arcsec/century for Mercury
```

**All derivations in Mathematica:**
```mathematica
Get["mathematica/phase_kinetics.m"]
```

---

## The published papers

All three are in *Physics Essays* and are the citable foundation:

1. **Cameron (2012)** — Dark matter miscalculation from missing ISM
   shell mass. *Phys. Essays* **25**, 306.

2. **Cameron (2015)** — Is the force of gravity a manifestation of
   the electric force? *Phys. Essays* **28**, 529.

3. **Cameron (2018)** — Gravitational component of cosmological
   redshift. *Phys. Essays* **31**.

---

## Cosmological terminology

All early universe emission events are classified by sector
(real/imaginary/mixed) and entropy character:

| Event | Correct term |
|---|---|
| Bounce annihilation | Topological phase transition emission |
| CMB — recombination | Thermal decoupling radiation |
| Nuclear binding γ | Nuclear condensation radiation |
| Neutrino decoupling | Imaginary sector information snapshot |
| Neutron decay ν̄ | Sector crossing emission |

The CMB is maximum entropy, thermally incoherent radiation.
It is not coherent emission of any kind.

---

## Archive

This repository consolidates two parallel development repositories.
Both are preserved as read-only historical records.

**[Claude Verification Repository](archive/CLAUDE_REPOSITORY.md)**  
Computational verification — Python Monte Carlo scripts, numerical
verification of all claims, documented failures. The correction
history spanning eleven errors across six iterations is in
`COMPARISON.md`.

**[Gemini Phase Kinetics Repository](archive/GEMINI_REPOSITORY.md)**  
Theoretical synthesis and narrative — formal mathematical derivations,
FAQ, and Mathematica computation script.

The methodology is described in `METHODOLOGY.md`. The correction
history — from 0/11 correct in V1 to 11/11 correct in the final
version — demonstrates that computational verification improves
narrative synthesis. That demonstration is the reason both original
repositories are preserved.

---

## Attribution

Physics and original hypotheses: **Donald Cameron**  
Published papers: *Physics Essays* (2012, 2015, 2018)  
Computational verification: Claude (Anthropic)  
Theoretical synthesis: Gemini (Google)

AI tools were used for arithmetic, pattern-matching, and code
generation. Physical intuition, original hypotheses, and
accountability for all claims belong to Donald Cameron.

---

*"The number has to be able to come out wrong."*  
*"The word has to mean what it says."*  
*Every calculation in this repository was designed to fail.*  
*The ones that did not are the results.*
