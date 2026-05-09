import numpy as np
import sys

np.random.seed(123)

k_e   = 8.988e9
e     = 1.602e-19
fm    = 1e-15
r_q   = 0.3e-15
r_min = 0.12e-15

Q_U = +2.0/3.0
Q_D = -1.0/3.0
PROTON  = np.array([Q_U, Q_U, Q_D])
NEUTRON = np.array([Q_U, Q_D, Q_D])

R_VALUES = np.array([0.5, 0.7, 0.9, 1.0, 1.2, 1.5, 1.8, 2.0, 2.5, 3.0]) * fm
N = 300000

def sample_batch(n, rq, rm):
    valid = np.zeros((n, 3, 3))
    filled = 0
    while filled < n:
        b = max(2*(n - filled), 5000)
        ct = 2*np.random.random((b, 3)) - 1
        ph = 2*np.pi * np.random.random((b, 3))
        st = np.sqrt(np.maximum(1 - ct**2, 0))
        pos = rq * np.stack([st*np.cos(ph), st*np.sin(ph), ct], axis=2)
        d01 = np.linalg.norm(pos[:,0] - pos[:,1], axis=1)
        d02 = np.linalg.norm(pos[:,0] - pos[:,2], axis=1)
        d12 = np.linalg.norm(pos[:,1] - pos[:,2], axis=1)
        ok = (d01 >= rm) & (d02 >= rm) & (d12 >= rm)
        tk = min(int(ok.sum()), n - filled)
        if tk > 0:
            valid[filled:filled+tk] = pos[ok][:tk]
            filled += tk
    return valid

def mc_force(c1, c2, R, n):
    a1 = c1 * e
    a2 = c2 * e
    p1 = sample_batch(n, r_q, r_min)
    p2 = sample_batch(n, r_q, r_min)
    p2a = p2 + np.array([R, 0.0, 0.0])
    F = np.zeros(n)
    for i in range(3):
        for j in range(3):
            rv = p2a[:, j, :] - p1[:, i, :]
            rm = np.linalg.norm(rv, axis=1)
            mk = rm > 1e-20
            F[mk] += k_e * a1[i] * a2[j] * rv[mk, 0] / rm[mk]**3
    return F

J_MeV = 1.0 / 1.602e-13

print("NAIVE CHARGE PRODUCT SUMS")
for name, c1, c2 in [("p-p", PROTON, PROTON),
                      ("p-n", PROTON, NEUTRON),
                      ("n-n", NEUTRON, NEUTRON)]:
    s = sum(q1*q2 for q1 in c1 for q2 in c2)
    note = "VAN DER WAALS ONLY" if abs(s) < 1e-9 else "net charge"
    print(f"  {name}: {s:+.6f} e^2  -> {note}")
print()

results = {}
for key, c1, c2 in [("pp", PROTON, PROTON),
                     ("pn", PROTON, NEUTRON),
                     ("nn", NEUTRON, NEUTRON)]:
    means = []
    errs  = []
    print(f"--- {key} ---")
    sys.stdout.flush()
    for R in R_VALUES:
        F = mc_force(c1, c2, R, N)
        m = np.mean(F)
        s = np.std(F) / np.sqrt(N)
        means.append(m)
        errs.append(s)
        sig = abs(m)/s if s > 0 else 0
        tag = "ATTRACTIVE" if m < 0 else "repulsive"
        print(f"  R={R/fm:.1f}fm  F={m:+.3e}N  err={s:.1e}N  {sig:.1f}sig  {tag}")
        sys.stdout.flush()
    results[key] = (np.array(means), np.array(errs))
    print()

print("POTENTIAL WELLS")
for key, (ms, es) in results.items():
    V = np.zeros(len(R_VALUES))
    for i in range(len(R_VALUES)-2, -1, -1):
        dR = R_VALUES[i+1] - R_VALUES[i]
        V[i] = V[i+1] + 0.5*(ms[i] + ms[i+1]) * dR
    Vm = -V * J_MeV
    idx = np.argmin(Vm)
    print(f"  {key}: V_min = {np.min(Vm):.4f} MeV  at R = {R_VALUES[idx]/fm:.1f} fm")

np.savez("/home/claude/mc_results.npz",
         R=R_VALUES,
         pp_m=results["pp"][0], pp_e=results["pp"][1],
         pn_m=results["pn"][0], pn_e=results["pn"][1],
         nn_m=results["nn"][0], nn_e=results["nn"][1])
print("\nResults saved to mc_results.npz")
