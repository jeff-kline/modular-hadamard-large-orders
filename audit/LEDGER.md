# Review ledger

All reviews below were process-separated AI reviews (fresh contexts, hand
arithmetic, no code unless stated). They are not independent expert peer
review. Each defect is labelled error, gap, missing hypothesis, sharpening or
documentation.

| Date | Scope | Verdict | Dispositions |
|---|---|---|---|
| 2026-11-20 | Theorem A (isolated attack and proof audit) | VERIFIED | splice "iff" needs $n_1\ge3$, $v\ge2$ (documentation); dependence on a 2026 matrix of order 668 removed by the complement of PG(2,13) (sharpening); typo in Kuperberg's paper noted (documentation) |
| 2026-11-20 | novelty of Theorem A and the general statements | not found in searched corpus | see [PRIOR-ART.md](PRIOR-ART.md) |
| 2026-11-21 | Theorems C, D, E | VERIFIED | Conjecture 5.1 must be read with 0 counted as a square (missing hypothesis in the source's wording); 2-adic repairs in the power-of-2 argument (gap, repaired); coverage remark for $p\equiv1\pmod8$ narrowed (sharpening) |
| 2026-11-21 | Theorem B tables ($p=11$, 13) | VERIFIED, conditional on $H(1132)$, $H(1244)$ | $H(1244)$ needed only at order 1244 (sharpening); missing parameter checks added (documentation); citation for the 2026 matrices corrected (documentation) |
| 2026-11-21 | $m=140$ constructions | VERIFIED | one-line gaps (row parity; dependence statement) fixed (documentation) |
| 2026-11-21 | Theorems F, G, H, Proposition 15 | VERIFIED | five wording errata applied (documentation) |
| 2026-11-21 | full manuscript, first cold read | READY AFTER FIXES | description of Kuperberg's threshold for $4\mid n$ corrected (error); "reduces Problem 10" (error, see below); "iff $4\mid n$" restricted to $A\ge2$ (error); 13 further items (sharpening, documentation) |
| 2026-11-21 | full manuscript, second cold read | READY AFTER FIXES | a remark wrongly said the $m=140$ thresholds use Theorem A (error); skew-conference assembly no longer claimed as new (sharpening); further wording items |
| 2026-11-21 | reading by a separate AI system | — | the conditional statement that fifteen order-129 matrices would settle Problem 10 was vacuous: such a matrix cannot exist for one class (error, statement removed; the impossibility is kept as a remark); a seed hypothesis in Proposition 6 tightened to $h\equiv4\pmod8$ (missing hypothesis); a better explicit 128-modular threshold (sharpening) |
| 2026-11-21 | exact instance checks | ALL PASS | see [VERIFICATION.md](../VERIFICATION.md) |
