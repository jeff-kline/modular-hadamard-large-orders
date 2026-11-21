# Prior-art record

Bounded comparison for Theorems A–H. Searches ran on 20 and 21 November 2026.
No personal data was sent; services that asked for an email were skipped and
are logged as NOT PERFORMED. A failed or rate-limited search is NOT PERFORMED,
never "no hits". This record bounds novelty to the corpus below; it is not a
claim of global priority.

## Closest sources and what they contain

| Source | Content | Relation |
|---|---|---|
| Kuperberg, *Hadamard matrices modulo p and small modular Hadamard matrices*, J. Combin. Des. 24 (2016); arXiv 1409.0148 (read in full) | $m=7$, 11 at all sufficiently large orders; iterated direct sum (Lemmas 3.5, 4.4); Conjecture 5.1, proved for $p=3,5,7,11$ and conditionally for $p\equiv3\pmod4$ with 2 primitive | Theorem A closes $m=7$ at every order divisible by 4; Theorem D proves Conjecture 5.1 for $p\not\equiv1\pmod8$ |
| Lee and Szőllősi, *Hadamard matrices modulo 5*, J. Combin. Des. 22 (2014); arXiv 1307.1981 (read in full) | $m=5$; direct-sum lemma; complement of a projective plane of order 9 | the lemma used throughout |
| Egan, Kotsireas, London and Ó Catháin, arXiv 2610.27175 v2 (read) | §5.4: Problems 10 and 11; status of the conjecture | Theorem A answers Problem 11 |
| Eliahou, *An update on modular Hadamard matrices*, J. Algebraic Combin. 64 (2026), art. 1 | abstract only: conjecture solved for $m=5,12,32$ and divisors; 64-modular at every $4\ell$ with $\ell\equiv3\pmod{16}$ or $\ell\equiv7\pmod{32}$ | **full text not openly accessible at the time of writing** (Springer bot check; HAL record without file; ACM DL 403) |
| Eliahou, Australas. J. Combin. 93 (2025) 422–427 (read) | a 64-modular matrix of order 668 | credited |
| Tseng, Zenodo 10.5281/zenodo.20267606 (May 2026; description read) | explicit 128- and 500-modular matrices of order 668 | credited; no overlap with the theorems |
| Brouwer, report ZW 202/83 (1983) (read) | symmetric designs $(1+2QS_d, Q^d, Q^{d-1}(Q-1)/2)$ | used in Theorems F, H |
| Hasani, Nellore and Ward, aiXiv 2611.02032 (Nov 2026); Alpöge, Voinov and Reynolds-Haertle, announcement (Aug 2026) | real Hadamard matrices of orders 1132, 1244 among twelve | used in Theorem B; cited neutrally |

## Search log

### 20 November 2026 (Theorems A–E)

- **Eliahou 2026 full text**: OpenAlex, Crossref, Semantic Scholar metadata
  (no open copy); Springer and ACM DL NOT ACCESSED; HAL record hal-05755172 is
  a notice without file; CORE 403, NOT PERFORMED; ResearchGate and Unpaywall
  NOT PERFORMED.
- **Forward citations** (OpenAlex): 4 works cite Kuperberg (Eliahou 2026, the
  survey, a watermarking paper, arXiv 2506.20778); citers of Lee–Szőllősi
  include Kuperberg, Eliahou 2026 and Borissov's Hadamard-modulo-prime papers
  (a different notion). None claims $m=7$ at all orders.
- **arXiv API** (https): "modular Hadamard", "Hadamard matrices modulo",
  "64-modular", "128-modular", "7-modular", "Golay quadruples", Butson +
  modular: only 1409.0148, 1307.1981, 2609.25543 (32-modular half-flip family).
- **aiXiv API** (positive control "Hadamard" returns Mark 2611.00465: PASS):
  modular Hadamard, 7-modular, 128-modular, Kuperberg, Eliahou, Hadamard
  modulo, projective design: no modular Hadamard paper.
- **GitHub** (positive control `gh search repos HadamardBound` →
  L-iet/HadamardBound: PASS): repos "modular hadamard", "7-modular hadamard",
  "Hadamard modulo", "kuperberg hadamard": none relevant; code "modular
  hadamard", "7-modular", "m-modular Hadamard": only a bounty page restating
  the survey (elder-plinius/V3R1T4S). teorth/optimizationproblems tree call
  failed: NOT PERFORMED for that repository.
- **Web search**: "7-modular Hadamard" every order; modular Hadamard
  conjecture + projective geometry; "Hadamard matrices modulo 7" complete
  proof; p-modular all large orders; "128-modular" sufficiently large: no
  claim of these results.

### 21 November 2026 (Theorems F–H, Proposition 15)

See [search-log-2026-11-21.txt](search-log-2026-11-21.txt): arXiv API (11
queries), aiXiv (control PASS; 10 queries), GitHub (5 repo, 6 code searches),
OpenAlex citers of Kuperberg (unchanged), web (3 queries). No composite-modulus
or every-modulus result found.

- **Zenodo API** (positive control: "symmetric Hadamard matrix of order 8740"
  returns that record: PASS): "modular Hadamard" → 3 records: Tseng (above);
  Kulhandjian, reproducibility code for the 32-modular half-flip family;
  Fathi, *Entry bounds and spectral saturation in the Hadamard problem*
  (rounding and repair criteria for real Hadamard matrices; no modular
  existence theorem). "Hadamard matrices modulo" → 0.

## Not examined

- The full text of Eliahou 2026 (not openly accessible).
- Eliahou–Kervaire (2001, 2005) and Marrero–Butson (1972, 1973) full texts
  (paywalled); cited for their known results only.
- Goldberg and Seberry Wallis–Whiteman on core-plus-conference block forms; the
  skew-conference assembly is not claimed as new.
- The Ionin–Trung handbook chapter (cited for standard design families).

The scan must be repeated within 7 days before tagging.
