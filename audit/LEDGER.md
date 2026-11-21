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
| 2026-11-21 | release audit: claims consistency | PARTIAL, fixed | abstract consistent with the theorems; README overstated general $m$ (error, fixed); instance checks described as covering every design type (error, fixed); Theorem H stated without $4\mid n$ in README and ADMISSION (missing hypothesis, fixed); Conjecture 5.1 stated without "0 counted as a square" in ADMISSION (missing hypothesis, fixed); Eliahou's announced 64-modular results and the known cases $2^A\le32$ not credited (error, credit added; Theorem E new only for $A\ge7$); "settles none of the open orders up to $10^4$" lacked an argument and needed restating, since $J-2I$ is 128-modular at the open order 5892 (gap, restated with a proof in the remark on size); unreproduced $m=140$ thresholds removed (documentation); "independent" wording in the AI disclosure (documentation) |
| 2026-11-21 | release audit: citations | PASS | all 24 entries cited; metadata checked against Crossref, arXiv, Zenodo and publisher pages; Ionin–Trung pages confirmed from the handbook's table of contents; AVR26 names and date confirmed from the survey's bibliography |
| 2026-11-21 | release audit: reproducibility | PASS | clean extraction rebuilds the PDF byte for byte, twice; `make verify` matches; manifest, fonts, hygiene and Zenodo route clean |
