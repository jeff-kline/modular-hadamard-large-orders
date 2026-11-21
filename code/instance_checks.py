"""Exact instance checks for the modular Hadamard paper (one per gadget type).

Each check builds a matrix with entries +-1 and verifies H H^T == n I (mod m),
plus a negative control (one flipped entry must fail). Single thread.
"""
import itertools
import os
import sys

import numpy as np


def paley(q):
    """Paley I Hadamard matrix of order q+1, q prime, q = 3 mod 4."""
    sq = {(x * x) % q for x in range(1, q)}
    chi = np.array([0] + [1 if x in sq else -1 for x in range(1, q)])
    Q = np.array([[chi[(j - i) % q] for j in range(q)] for i in range(q)])
    H = np.ones((q + 1, q + 1), dtype=np.int64)
    H[1:, 0] = -1
    H[1:, 1:] = Q + np.eye(q, dtype=np.int64)
    assert (H @ H.T == (q + 1) * np.eye(q + 1, dtype=np.int64)).all()
    return H


def sylvester(k):
    H = np.array([[1]], dtype=np.int64)
    for _ in range(k):
        H = np.block([[H, H], [H, -H]])
    return H


def pg_complement(d, q):
    """Complement of the point-hyperplane design of PG(d,q), q prime."""
    pts = []
    for v in itertools.product(range(q), repeat=d + 1):
        nz = [x for x in v if x]
        if nz and nz[0] == 1:
            pts.append(v)
    P = np.array(pts, dtype=np.int64)
    N = ((P @ P.T) % q == 0).astype(np.int64)  # incidence point-hyperplane
    v = len(pts)
    k = (q**d - 1) // (q - 1)
    assert (N.sum(axis=1) == k).all()
    return 1 - N


def paley_design_complement(q):
    """Complement of the quadratic-residue (q,(q-1)/2,(q-3)/4) difference set design."""
    sq = {(x * x) % q for x in range(1, q)}
    return np.array([[0 if ((j - i) % q) in sq else 1 for j in range(q)] for i in range(q)], dtype=np.int64)


def design_params(N):
    v = N.shape[0]
    k = int(N.sum(axis=1)[0])
    G = N @ N.T
    lam = int(G[0, 1])
    assert (N.sum(axis=1) == k).all() and (N.sum(axis=0) == k).all()
    assert (G == (k - lam) * np.eye(v, dtype=np.int64) + lam).all()
    return v, k, lam


def normalize(H):
    H = H * H[:, :1]
    H = H * H[:1, :]
    return H


def splice(H1, N):
    """[[core(H1), J], [J, 2N - J]] for normalized H1."""
    C = normalize(H1)[1:, 1:]
    a, v = C.shape[0], N.shape[0]
    top = np.hstack([C, np.ones((a, v), dtype=np.int64)])
    bot = np.hstack([np.ones((v, a), dtype=np.int64), 2 * N - 1])
    return np.vstack([top, bot])


def is_mh(H, m):
    n = H.shape[0]
    Hf = H.astype(np.float64)
    G = np.rint(Hf @ Hf.T).astype(np.int64)
    return bool(((G - n * np.eye(n, dtype=np.int64)) % m == 0).all())


def check(name, H, m):
    assert set(np.unique(H)) <= {-1, 1}
    ok = is_mh(H, m)
    bad = H.copy()
    bad[1, 2] *= -1
    ctrl = not is_mh(bad, m)
    print(f"{name}: order {H.shape[0]}, mod {m}: {'PASS' if ok else 'FAIL'}; negative control {'PASS' if ctrl else 'FAIL'}")
    return ok and ctrl


def main():
    results = []
    # m = 7, PG(2,13) complement (183,169,156), class 3: H24 -> 206 -> 388
    D13 = pg_complement(2, 13)
    print("PG(2,13)^c params", design_params(D13))
    H = paley(23)
    H = splice(H, D13); results.append(check("m=7 PG(2,13)^c x1", H, 7))
    H = splice(H, D13); results.append(check("m=7 PG(2,13)^c x2", H, 7))
    # m = 7, PG(6,3) complement (1093,729,486), class 6: H20 -> 1112
    D3 = pg_complement(6, 3)
    print("PG(6,3)^c params", design_params(D3))
    results.append(check("m=7 PG(6,3)^c", splice(paley(19), D3), 7))
    # m = 11, (23,12,6), class 2: H24 -> 46 -> 68
    P23 = paley_design_complement(23)
    print("(23,12,6) params", design_params(P23))
    H = splice(paley(23), P23); results.append(check("m=11 (23,12,6) x1", H, 11))
    H = splice(H, P23); results.append(check("m=11 (23,12,6) x2", H, 11))
    # m = 11, PG(5,3) complement (364,243,162), class 5: H16 -> 379
    D53 = pg_complement(5, 3)
    print("PG(5,3)^c params", design_params(D53))
    results.append(check("m=11 PG(5,3)^c", splice(sylvester(4), D53), 11))
    # m = 140 class 5: MH(121,7) = (J11-2I)^(x2), PG(3,2)^c (15,8,4) -> MH(135,7); then H20 (x)
    J11 = np.ones((11, 11), dtype=np.int64) - 2 * np.eye(11, dtype=np.int64)
    M121 = np.kron(J11, J11)
    results.append(check("m=7 (J11-2I)^(x2)", M121, 7))
    D32 = pg_complement(3, 2)
    print("PG(3,2)^c params", design_params(D32))
    M135 = splice(M121, D32)
    results.append(check("m=7 PG(3,2)^c", M135, 7))
    H20 = paley(19)
    G = np.kron(M135 @ M135.T, H20 @ H20.T)  # Gram of M135 (x) H20 by the mixed-product rule
    n = 135 * 20
    ok140 = bool(((G - n * np.eye(n, dtype=np.int64)) % 140 == 0).all())
    print(f"m=140 H20 (x) MH(135,7): order {n}, mod 140: {'PASS' if ok140 else 'FAIL'}")
    results.append(ok140)
    print("ALL PASS" if all(results) else "SOME FAILED")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
