# Section III — Complex Charge and Force Unification

*Cameron Unified Framework — Paper Draft*  
*Status: In preparation. Not yet peer reviewed.*  
*Updated: Neutron electromagnetic structure corrected and expanded.*

---

For the spin and Pauli exclusion consequences of the PMV bivector, see Section II.5.

---

## III.1 The Complex Charge

In the pseudo-Euclidean dual hourglass metric, particles have two
distinct charge-like properties: electric charge q (coupling to the
real sector) and gravitational charge (coupling to the imaginary
sector). These are the real and imaginary components of a single
complex number.

The **complex charge** Q of a particle is:

```
Q  =  q  +  i · m · √G                                    (III.1)
```

where q is the electric charge (Coulombs), m is the rest mass (kg),
G is Newton's gravitational constant, and i is the imaginary unit.

**Dimensional note:** In Gaussian CGS units, [q²] = [Gm²] = erg·cm,
making this combination dimensionally consistent without supplementary
constants. √G is the explicit conversion factor between charge and
mass units in Gaussian CGS — a pre-existing feature of the
mathematics, not an invention of this framework.

The **phase angle** of Q:

```
φ  =  arg(Q)  =  atan( m·√G / q )                        (III.2)
```

This phase angle is identical to the PMV phase angle established
in Section II. φ = 0 is pure electromagnetism. φ = π/2 is pure
gravity in terms of net charge. All physical particles lie between
these extremes.

---

## III.2 Complex Charge of Fundamental Particles

All values computed from measured constants with no adjustable parameters.

| Particle | Re(Q) = q | Im(Q) = m√G | Phase φ (rad) | Character |
|---|---|---|---|---|
| Electron | −1.602×10⁻¹⁹ C | 7.44×10⁻³⁶ | ≈ π − 4.9×10⁻²² | EM dominated |
| Proton | +1.602×10⁻¹⁹ C | 1.37×10⁻³² | 8.5×10⁻¹⁴ | EM dominated |
| Neutron | 0 (net, exactly) | 1.37×10⁻³² | π/2 (net) | Zero net charge — see III.2.1 |
| Photon | 0 | 0 | undefined | Null geodesic |
| H atom (neutral) | 0 (charges cancel) | (m_p+m_e)√G | π/2 | Pure imaginary → Newtonian gravity ✓ |

### III.2.1 The Neutron — Net Charge vs Internal Structure

The neutron's **net** electric charge is exactly zero by measurement
(|q_n| < 2.9×10⁻²⁶ e, PDG 2022). This places its **net** complex
charge at φ = π/2 — on the imaginary axis — with no net real
component. It produces no electrostatic field at large distances
and exerts no net electrostatic force on distant particles.

However, the neutron is not electromagnetically inert at all scales.
It contains three quarks — u(+2/3), d(−1/3), d(−1/3) — which are
electrically charged and move at approximately 0.99c inside the
nucleon. At any given instant, the three quarks are not
symmetrically placed. The **instantaneous** electric field from
the neutron is therefore nonzero, oscillating rapidly as the quarks
orbit their common center of mass.

This distinction matters:

```
Net charge:           q_n = 0           (time-averaged, large distances)
Instantaneous field:  E(t) ≠ 0          (oscillates at ~10²³ Hz)
Magnetic moment:      μ_n = −1.913 μ_N  (measured, from quark currents)
Charge radius²:       r²_n = −0.114 fm² (negative: negative charge at surface)
```

All three of these nonzero quantities arise from the **internal
quark charge distribution**, not from a nonzero net charge.

The negative charge radius confirms the anchor model geometry
(Section VI.3): d quarks (negative charge −1/3 each) are pulled
to the surface by the charge balance equilibrium, while the u quark
(positive charge +2/3) sits closer to the center. The time-averaged
charge distribution has negative charge on the outside — exactly
the sign of r²_n = −0.114 fm².

**The neutron at φ = π/2 is correct for the net complex charge.**
The internal quark structure produces electromagnetic effects at
short range through the cross term in the quark-level complex
charges — which is the van der Waals mechanism of Section IV.

---

## III.3 The Unified Force Law

With complex charge defined, the force law is:

```
F  =  Q₁ · Q₂ / r²                                        (III.3)
```

Expanding the product:

```
Q₁ · Q₂  =  (q₁ + im₁√G)(q₂ + im₂√G)
           =  q₁q₂  −  Gm₁m₂  +  i(q₁m₂ + q₂m₁)√G       (III.4)
               ↑EM      ↑gravity    ↑van der Waals
```

The three terms correspond to three distinct physical interactions:

**q₁q₂ / r²** — Electrostatic force.  
Positive for like charges (repulsion), negative for opposite
charges (attraction). This is the entirety of classical
electromagnetism for charged particles.

**−Gm₁m₂ / r²** — Gravitational force.  
The factor i² = −1 produces a sign that is always negative
regardless of the sign of the masses. Mass has no negative
counterpart, so gravity is always attractive.  
**The minus sign in Newton's law is not a postulate — it is i².**

**i(q₁m₂ + q₂m₁)√G / r²** — The van der Waals cross term.  
The mixed real-imaginary interaction. For charge-neutral matter
this term averages to zero in the bulk, but near the null geodesic
boundary it produces the orbital configuration effects computed
numerically in Cameron (2015), and the oscillating quark field
effects described in Section IV.

### Newton's law is exact for neutral matter

For a neutral hydrogen atom: q = 0, so Q_H = i(m_p + m_e)√G.

```
F_H-H  =  Q_H² / r²
        =  [i(m_p+m_e)√G]² / r²
        =  −G(m_p+m_e)² / r²                               (III.5)
```

This is Newton's gravitational force law. **Exact. No approximation.
No free parameter.**

---

## III.4 The Force Hierarchy from Phase Angles

The ratio of gravitational to electromagnetic force:

```
F_grav / F_EM  =  G·m_e·m_p / (k_e·e²)  =  4.4×10⁻⁴⁰     (III.6)
```

This ratio is simply Im(Q)² to Re(Q)² for the electron-proton
system. Gravity appears weak because mass (imaginary charge) is
10²⁰ times smaller than electric charge (real charge) in natural
units. There is no hierarchy problem to solve.

### The four forces as phase states

| Force | Phase φ | Sector | Origin in Q₁Q₂ | Character |
|---|---|---|---|---|
| Electromagnetism | φ ≈ 0 | Real | Re(Q₁)·Re(Q₂) = q₁q₂ | Bipolar: attracts unlike, repels like |
| Gravity | φ = π/2 (net) | Imaginary | −Im(Q₁)·Im(Q₂) = −Gm₁m₂ | Monopolar: always attractive (i²=−1) |
| Strong force | φ ≈ π/2, inverted metric | Imaginary inside nucleon | Im(Q_quark)² at fm scale | Quark van der Waals — see Section IV |
| Weak force | φ = π/4 | Mixed | PMV rotation at θ=π/4 | W/Z bosons at real-imaginary boundary |

---

## III.5 Antimatter and the Sign of Q

Antiparticles have the same mass as their partners but opposite
electric charge:

```
Q_positron   = +e  +  i·m_e·√G                            (III.7)
Q_antiproton = −e  +  i·m_p·√G
```

The imaginary component — the gravitational charge — has the
**same sign** for both particle and antiparticle, since mass is
always positive. Antimatter gravitates in the same direction
as matter.

**Experimental confirmation:** The ALPHA-g experiment at CERN (2023)
confirmed that antihydrogen falls downward in Earth's gravitational
field. ✓

---

## III.6 The Pauli Exclusion Connection and the 32.4% Fraction

The Cameron (2015) calculation showed that gravity requires
approximately **32.4%** of atom pairs to be in (3,12)-type
orbital configurations at any instant.

The required fraction (32.4%) sits between the naive (3,12)
geometric weight (25%) and the total same-side weight (37.5%)
from the 2015 paper's own statistical analysis. No exotic
alignment mechanism is required.

The 32.4% is scale-independent: it is the same fraction whether
computed for two hydrogen atoms at 1 metre or for the Earth-Moon
system at 384,400 km. Both F_Newton and F_(3,12) scale as 1/R²,
so R cancels exactly.

---

## III.7 The Knot Force Equation

The topological knot at the real-imaginary boundary (the particle
itself) experiences a force from the metric asymmetry:

```
F_knot  =  (1/r²) · (q²  −  Gm²  +  2i·qm·√G)           (III.8)
```

This is exactly the expansion of Q²/r² = (q + im√G)²/r².

**Dimensional note:** In Gaussian CGS units both q² and Gm² carry
identical dimensions (g·cm³·s⁻²), and the expression is valid
without supplementary constants.

---

## III.8 Summary: The Unified Force Law in Three Equations

```
Q  =  q  +  i·m·√G          [complex charge]              (III.9a)

F  =  Q₁Q₂/r²               [unified force law]            (III.9b)

α/β  =  (m_e/m_p)²          [cross-tether constraint]      (III.9c)
```

From these three equations, with no additional postulates:

- Newton's law of gravitation — from Im(Q)² for neutral matter ✓
- Coulomb's law — from Re(Q)² for charged particles ✓
- Attractive-only gravity — from i² = −1 ✓
- Identical gravitational behavior of matter and antimatter ✓
- Weakness of gravity — from |Im(Q)|²/|Re(Q)|² ≈ 10⁻⁴⁰ ✓
- ALPHA-g result (antihydrogen falls down) ✓
- Neutron magnetic moment — from oscillating quark cross terms ✓
- Neutron charge radius sign — from anchor model geometry ✓
- van der Waals residual — Cameron (2015), confirmed at 8–14σ ✓

---

## III.9 Open Questions

**What determines the value of G?**  
The master equation G ∝ e²a₀²/m_p² gives G to within a factor
of ~9 from the quark geometry. Closing this gap requires completing
the relativistic quark Monte Carlo (Gap 3 in disputes/).

**Why is m_e/m_p = 1/1836?**  
This ratio — encoded in the cross-tether α/β = (m_e/m_p)² — is
what makes gravity appear weak. Its origin from quark geometry
is the central open question of the framework.

---

*Next: [Section IV — The Four Forces as PMV Phase States](section_IV_four_forces.md)*  
*Previous: [Section II.4 — The Hamiltonian Structure](section_II4_hamiltonian.md)*

---

*This draft has not been submitted for peer review.*  
*Open questions documented in [disputes/what_doesnt_work.md](../disputes/what_doesnt_work.md)*
