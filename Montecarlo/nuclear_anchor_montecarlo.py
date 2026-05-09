"""
Nuclear Van der Waals — Charge Asymmetry / Anchor Model
Cameron Unified Framework

Key physics:
  - Heavy quarks act as anchors — pulled to nucleon center
  - Lighter majority quarks pushed to surface by mutual repulsion
  - Time-averaged charge distribution is asymmetric:
      Proton:  u(surface), u(surface), d(center)
      Neutron: d(surface), d(surface), u(center)
  - This creates preferred attractive orientation at nuclear separations
  - No relativistic time integration needed — use static charge distribution

This avoids the computer crash problem of tracking v~0.99c quarks in real time.
"""

import numpy as np
import sys

np.random.seed(42)

# Physical constants
k_e  = 8.988e9
e    = 1.602e-19
fm   = 1e-15

# Quark charges
Q_U = +2.0/3.0
Q_D = -1.0/3.0

# Nucleon radius
r_N = 0.87 * fm

# Anchor model: equilibrium orbital radii from charge balance
# Proton (uud): u quarks at r_surface, d quark pulled to r_center
# Neutron (udd): d quarks at r_surface, u quark pulled to r_center
# Ratio r_surface/r_center ~ 2.3 from force balance equation
RATIO = 2.3

r_surface = r_N * (RATIO / (1.0 + RATIO))   # ~0.63 fm
r_center  = r_N * (1.0 / (1.0 + RATIO))     # ~0.27 fm

print(f"Anchor model orbital radii:")
print(f"  Surface quarks: {r_surface/fm:.3f} fm")
print(f"  Center quark:   {r_center/fm:.3f} fm")
print(f"  Ratio:          {r_surface/r_center:.2f}")
print()

# Width of Gaussian spread around mean orbital radius
# Heisenberg uncertainty: sigma ~ hbar/(2 * p) at each radius
hbar = 1.055e-34
c    = 3e8
# Relativistic momentum at confinement: p ~ hbar/r_N
p_quark = hbar / r_N
sigma_quark = hbar / (2.0 * p_quark)   # ~ r_N/2
sigma = min(sigma_quark, r_N * 0.25)   # cap at 0.25 * r_N

print(f"Position uncertainty sigma: {sigma/fm:.3f} fm")
print()

# Pauli exclusion minimum separation
r_min = 0.10 * fm

# Separation distances
R_VALUES = np.array([
    0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
    1.1, 1.2, 1.4, 1.5, 1.7, 2.0, 2.5, 3.0
]) * fm

N = 500_000   # samples per distance


# =============================================================================
# Nucleon charge configurations
# =============================================================================

def make_proton_config():
    """
    Proton = u(surface) u(surface) d(center)
    Returns quark positions (3,3) and charges (3,)
    """
    charges = np.array([Q_U, Q_U, Q_D])

    # u quarks at surface radius, d quark at center radius
    radii = np.array([r_surface, r_surface, r_center])
    return radii, charges


def make_neutron_config():
    """
    Neutron = u(center) d(surface) d(surface)
    Returns radii (3,) and charges (3,)
    """
    charges = np.array([Q_U, Q_D, Q_D])
    radii   = np.array([r_center, r_surface, r_surface])
    return radii, charges


def sample_positions_asymmetric(radii, n, sigma_pos, r_min_sep):
    """
    Sample n sets of 3 quark positions.
    Each quark is Gaussian-distributed around its mean orbital radius.
    Pauli exclusion: reject if any two quarks < r_min_sep apart.

    Returns shape (n, 3, 3)
    """
    valid  = np.zeros((n, 3, 3))
    filled = 0

    while filled < n:
        b = max(2*(n - filled), 10000)

        # Sample on sphere surfaces at each quark's radius
        # then add Gaussian spread
        cos_t = 2*np.random.random((b, 3)) - 1.0
        phi   = 2*np.pi * np.random.random((b, 3))
        sin_t = np.sqrt(np.maximum(1.0 - cos_t**2, 0.0))

        # Base position on sphere at orbital radius
        pos = np.stack([sin_t*np.cos(phi),
                        sin_t*np.sin(phi),
                        cos_t], axis=2)  # (b, 3, 3) unit vectors

        # Scale each quark by its orbital radius + Gaussian jitter
        for qi in range(3):
            r_jitter = np.random.normal(radii[qi], sigma_pos, b)
            r_jitter = np.maximum(r_jitter, r_min_sep * 0.5)
            pos[:, qi, :] *= r_jitter[:, np.newaxis]

        # Pauli exclusion check
        d01 = np.linalg.norm(pos[:,0] - pos[:,1], axis=1)
        d02 = np.linalg.norm(pos[:,0] - pos[:,2], axis=1)
        d12 = np.linalg.norm(pos[:,1] - pos[:,2], axis=1)
        ok  = (d01 >= r_min_sep) & (d02 >= r_min_sep) & (d12 >= r_min_sep)

        tk = min(int(ok.sum()), n - filled)
        if tk > 0:
            valid[filled:filled+tk] = pos[ok][:tk]
            filled += tk

    return valid


def mc_force_asymmetric(radii1, charges1, radii2, charges2, R, n):
    """
    Monte Carlo inter-nucleon force using asymmetric charge distributions.
    Returns array of n force samples (x-component).
    """
    a1 = charges1 * e
    a2 = charges2 * e

    p1 = sample_positions_asymmetric(radii1, n, sigma, r_min)
    p2 = sample_positions_asymmetric(radii2, n, sigma, r_min)
    p2_abs = p2 + np.array([R, 0.0, 0.0])

    F = np.zeros(n)
    for i in range(3):
        for j in range(3):
            rv  = p2_abs[:, j, :] - p1[:, i, :]
            rm  = np.linalg.norm(rv, axis=1)
            mk  = rm > 1e-20
            F[mk] += k_e * a1[i] * a2[j] * rv[mk, 0] / rm[mk]**3

    return F


# =============================================================================
# Also run the symmetric (uniform sphere) model for comparison
# =============================================================================

def sample_positions_uniform(n, r_quark, r_min_sep):
    """Uniform sphere sampling — original model for comparison."""
    valid  = np.zeros((n, 3, 3))
    filled = 0
    while filled < n:
        b   = max(2*(n - filled), 5000)
        ct  = 2*np.random.random((b, 3)) - 1.0
        ph  = 2*np.pi * np.random.random((b, 3))
        st  = np.sqrt(np.maximum(1.0 - ct**2, 0.0))
        pos = r_quark * np.stack([st*np.cos(ph), st*np.sin(ph), ct], axis=2)
        d01 = np.linalg.norm(pos[:,0]-pos[:,1], axis=1)
        d02 = np.linalg.norm(pos[:,0]-pos[:,2], axis=1)
        d12 = np.linalg.norm(pos[:,1]-pos[:,2], axis=1)
        ok  = (d01 >= r_min_sep) & (d02 >= r_min_sep) & (d12 >= r_min_sep)
        tk  = min(int(ok.sum()), n - filled)
        if tk > 0:
            valid[filled:filled+tk] = pos[ok][:tk]
            filled += tk
    return valid


def mc_force_uniform(charges1, charges2, R, n):
    a1 = charges1 * e
    a2 = charges2 * e
    p1 = sample_positions_uniform(n, r_N*0.35, r_min)
    p2 = sample_positions_uniform(n, r_N*0.35, r_min)
    p2_abs = p2 + np.array([R, 0.0, 0.0])
    F = np.zeros(n)
    for i in range(3):
        for j in range(3):
            rv = p2_abs[:, j, :] - p1[:, i, :]
            rm = np.linalg.norm(rv, axis=1)
            mk = rm > 1e-20
            F[mk] += k_e * a1[i] * a2[j] * rv[mk, 0] / rm[mk]**3
    return F


# =============================================================================
# Main run
# =============================================================================

J_MeV = 1.0 / 1.602e-13

PROTON  = np.array([Q_U, Q_U, Q_D])
NEUTRON = np.array([Q_U, Q_D, Q_D])

r_proton,  c_proton  = make_proton_config()
r_neutron, c_neutron = make_neutron_config()

print("="*65)
print("ANCHOR MODEL — Asymmetric charge distributions")
print("="*65)

results_asym = {}
configs = [
    ('pp', r_proton,  c_proton,  r_proton,  c_proton,  'Proton-Proton'),
    ('pn', r_proton,  c_proton,  r_neutron, c_neutron, 'Proton-Neutron [naive=0, pure vdW]'),
    ('nn', r_neutron, c_neutron, r_neutron, c_neutron, 'Neutron-Neutron [naive=0, pure vdW]'),
]

for key, r1, c1, r2, c2, label in configs:
    means = []
    errs  = []
    print(f"\n--- {label} ---")
    sys.stdout.flush()

    for R in R_VALUES:
        F   = mc_force_asymmetric(r1, c1, r2, c2, R, N)
        m   = np.mean(F)
        s   = np.std(F) / np.sqrt(N)
        sig = abs(m)/s if s > 0 else 0.0
        means.append(m)
        errs.append(s)
        tag = "ATTRACTIVE ✓" if m < 0 else "repulsive  "
        print(f"  R={R/fm:.2f}fm  F={m:+.4e}N  "
              f"err={s:.1e}N  {sig:5.1f}σ  {tag}")
        sys.stdout.flush()

    results_asym[key] = (np.array(means), np.array(errs))

# Print potential wells
print("\n" + "="*65)
print("POTENTIAL WELLS — Anchor Model")
print("="*65)
for key, (ms, es) in results_asym.items():
    V = np.zeros(len(R_VALUES))
    for i in range(len(R_VALUES)-2, -1, -1):
        dR = R_VALUES[i+1] - R_VALUES[i]
        V[i] = V[i+1] + 0.5*(ms[i] + ms[i+1]) * dR
    Vm   = -V * J_MeV
    imin = np.argmin(Vm)
    print(f"  {key}: V_min = {np.min(Vm):+.4f} MeV  "
          f"at R = {R_VALUES[imin]/fm:.2f} fm")

print("\nEmpirical nuclear binding: ~2–8 MeV/nucleon")
print("Expected: anchor model should give larger signal than uniform model")

# Save results
np.savez('/home/claude/mc_anchor_results.npz',
         R=R_VALUES,
         pp_m=results_asym['pp'][0], pp_e=results_asym['pp'][1],
         pn_m=results_asym['pn'][0], pn_e=results_asym['pn'][1],
         nn_m=results_asym['nn'][0], nn_e=results_asym['nn'][1],
         r_surface=r_surface, r_center=r_center)

print("\nResults saved to mc_anchor_results.npz")
