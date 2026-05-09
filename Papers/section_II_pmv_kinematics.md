# Section II — Primary Momentum Vectors and Relativistic Kinematics

*Cameron Unified Framework — Paper Draft*  
*Status: In preparation. Not yet peer reviewed.*

---

## II.1 The Two Primary Momentum Vectors

Every particle in the Cameron framework has two momentum vectors:

```
P_re  =  real PMV    — motion in the observable real sector
P_im  =  imaginary PMV — motion in the imaginary gravitational sector
```

The total state of a particle is completely described by the
**orientation of these two vectors relative to each other**,
specified by the angle θ between them.

This is the complete replacement for the concept of velocity
in the Cameron framework. Velocity is not a fundamental quantity
— it is a derived quantity, the projection of the PMV rotation
onto the real axis.

---

## II.2 The PMV Rotation and All of Special Relativity

The angle θ between the two PMVs generates all relativistic
mechanics through simple trigonometry.

### Velocity

```
v  =  c · sin θ                                            (II.1)
```

- At θ = 0: v = 0 — particle at rest (PMVs aligned)
- At θ = π/4: v = c/√2
- At θ = π/2: v = c — photon (PMVs perpendicular)
- At θ > π/2: imaginary velocity — virtual/inner cone region

### Lorentz factor

```
γ  =  1 / cos θ                                           (II.2)
```

### Relativistic momentum

```
p  =  m₀c · tan θ  =  γm₀v                               (II.3)
```

### Energy

```
E  =  γm₀c²  =  m₀c² / cos θ                             (II.4)
```

### The energy-momentum relation

From (II.3) and (II.4):

```
E²  =  (pc)²  +  (m₀c²)²                                 (II.5)
```

This is the standard relativistic dispersion relation —
**derived from PMV geometry, not postulated.**

### Velocity addition

If two velocities correspond to PMV rotation angles θ₁ and θ₂,
the combined rotation is θ_total = θ₁ + θ₂. Therefore:

```
v_total  =  c · sin(θ₁ + θ₂)
          =  c(sin θ₁ cos θ₂ + cos θ₁ sin θ₂)
          =  (v₁√(1−v₂²/c²) + v₂√(1−v₁²/c²))            (II.6)
```

This is the Einstein velocity addition formula — **derived from
angle addition, not postulated.** The speed limit c emerges at
θ = π/2 because sin(π/2) = 1 and tan(π/2) → ∞. No separate
postulate about the constancy of the speed of light is required.

---

## II.3 Spin as the PMV Cross Product

The cross product of the two PMVs gives spin:

```
P_re × P_im  =  ℏ · n̂                                     (II.7)
```

where n̂ is a unit vector and ℏ is the reduced Planck constant.

**Spin is derived, not postulated.** It is the angular momentum
of the PMV rotation. ℏ is the minimum quantum of PMV rotation —
the smallest angle by which the PMV pair can rotate in the
pseudo-Euclidean metric.

The spin quantum number s = 1/2 for fermions follows from the
double-cover of SO(3) required to return the PMV pair to its
original configuration after a full 2π rotation — the same
topological argument as in standard QM but now with geometric
origin.

---

## II.4 The Photon as a Special Case

At θ = π/2 (v = c):
- P_re ⊥ P_im (PMVs are perpendicular)
- The particle exists only in the plane orthogonal to its motion
- Zero distance in the direction of motion: Δx_direction = 0
- Zero time between emission and absorption: Δt = 0

The photon sits exactly at the null geodesic of the metric where
d² = 0. This means:
- In the forward direction: d² < 0 — purely imaginary distance
  (source and destination are in direct imaginary contact)
- In the backward direction: d² > 0 — purely real distance
  (the photon's history is real and observable)

**Why light has no rest frame:**
At θ = π/2, cos θ = 0, so γ → ∞. There is no rest frame
because the PMVs can never be aligned (θ = 0) for a photon —
aligning them would require reducing v to zero, which is
impossible for a massless particle that must always traverse
the null geodesic.

---

## II.5 Rest Mass as Imaginary Momentum

The most important result of the PMV analysis:

```
P_im  =  m₀c  =  constant                                 (II.8)
```

The imaginary momentum is exactly m₀c at all velocities.
It does not change under Lorentz boosts.

**The rest mass IS the imaginary momentum magnitude.**

This is why inertial mass equals gravitational mass
(the equivalence principle):
- Inertial mass: the resistance to acceleration in the real sector
  = how much P_re changes per unit force = m₀
- Gravitational mass: the imaginary charge Im(Q)/√G = m₀·√G/√G = m₀

Both are the same quantity: the magnitude of the imaginary PMV
divided by appropriate constants. They are equal because they
ARE the same number. The equivalence principle is not an
unexplained coincidence — it is a geometric identity.

---

## II.6 The Lorentz Transformation as PMV Rotation

A Lorentz boost is a rotation of the PMV pair by angle θ in
the pseudo-Euclidean plane.

Standard Lorentz transformation:
```
t'  =  γ(t − vx/c²)
x'  =  γ(x − vt)
```

PMV rotation form:
```
[t']   [cosh φ   −sinh φ] [t]
[x'] = [−sinh φ   cosh φ] [x]
```

where φ = atanh(v/c) is the **rapidity** — the true rotation
angle in pseudo-Euclidean space. The hyperbolic functions
(cosh, sinh) appear instead of circular functions (cos, sin)
because pseudo-Euclidean rotations are hyperbolic rather than
circular. This is why all worldlines of accelerating observers
are **hyperbolas** — they are the pseudo-Euclidean equivalent
of circles.

The Lorentz transformation is not a postulate in the Cameron
framework. It is the statement that changing reference frames
corresponds to rotating the PMV pair, which in pseudo-Euclidean
space produces hyperbolic motion.

---

## II.7 The PMV State Table

| θ | v/c | Physical state | PMV relationship |
|---|---|---|---|
| 0 | 0 | Rest | P_re and P_im aligned |
| 0 < θ < π/4 | 0 < v < c/√2 | Subluminal | P_re growing, P_im constant |
| π/4 | 1/√2 | v = c/√2 | P_re = P_im |
| π/4 < θ < π/2 | c/√2 < v < c | Relativistic | P_re >> P_im |
| π/2 | 1 | Photon | P_re ⊥ P_im, d² = 0 |
| π/2 < θ < π | imaginary | Virtual / inner cone | P_im inverted |

---

## II.8 Connection to the Published Papers

The PMV rotation picture connects directly to the numerical
results in the published papers:

**Cameron (2015):** The (3,12) orbital configuration is a specific
PMV orientation where the electron orbital angle creates the
asymmetric force. The 32.4% alignment fraction is the fraction
of PMV orientations that produce net attractive force.

**Cameron (2018):** The gravitational redshift formula
z = πGρR²/c² follows from the PMV kinematics applied to photon
propagation through a medium of density ρ. The photon's PMV
rotates as it passes through matter, shifting its frequency.

**Cameron (2012):** The flat rotation curves follow from the
imaginary sector force between the ISM/CGM mass distribution
and the galactic disk stars. The ISM density profile ρ ∝ R⁻²
required for flat curves is the isothermal sphere profile that
the imaginary sector naturally produces.

---

*Next: [Section II.4 — The Hamiltonian Structure](section_II4_hamiltonian.md)*  
*Previous: [Section I — The Dual Hourglass Metric](section_I_metric.md)*  
*Forward: [Section III — Complex Charge and Force Unification](section_III_complex_charge.md)*

---

*This draft has not been submitted for peer review.*  
*Open questions documented in [disputes/what_doesnt_work.md](../disputes/what_doesnt_work.md)*
