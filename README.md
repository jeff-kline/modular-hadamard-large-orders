# Modular Hadamard matrices at large orders

Jeffery Kline

**Status: draft.** This repository is being prepared for release under the
project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html).
No version has been released and no DOI exists yet.

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## Introduction

A Hadamard matrix is a square matrix of 1s and −1s whose rows are pairwise
orthogonal. Such matrices are conjectured to exist in every size divisible
by 4. A modular Hadamard matrix asks for less: its rows need only be
orthogonal modulo a fixed number $m$. For a few small values of $m$ these are
known to exist in every size divisible by 4, and Kuperberg showed that for
$m=7$ and $m=11$ they exist in all large enough sizes.

New in this paper: 7-modular Hadamard matrices exist in every size divisible
by 4. This answers a question in a 2026 survey. The same holds for $m=11$
and $m=13$. For every other $m$, the paper shows that they exist in all large
enough sizes, though for some $m$ only when the size is divisible by a higher
power of 2.

The matrices are built by a known method: attaching a block design to a
smaller matrix. What is new is the choice of designs.

## What is new

Earlier work settled the $m$-modular Hadamard conjecture, existence at every
order divisible by 4, for $m=5$, 12 and 32 and their divisors (Lee–Szőllősi;
Marrero–Butson; Eliahou–Kervaire). Kuperberg proved the cases $m=7$ and
$m=11$ at all sufficiently large orders. Eliahou constructed 64-modular
matrices at every order $4\ell$ with $\ell\equiv3\pmod{16}$ or
$\ell\equiv7\pmod{32}$. New here:

1. **Principal result: 7-modular Hadamard matrices at every order divisible
   by 4** (Theorem A), answering Problem 11 of the 2026 survey. The proof uses
   only Hadamard matrices known before 2026.
2. **11- and 13-modular Hadamard matrices at every order divisible by 4**
   (Theorem B). Each proof uses one Hadamard matrix announced in 2026:
   order 1132 for $m=11$ and order 1244 for $m=13$, each needed only at that
   order.
3. **All large orders divisible by 4** for every odd prime (Theorem C), every
   power of 2 (Theorem E), and every modulus of the form $4p^a$ or $4pq$
   (Theorem F), with effective thresholds.
4. **Every modulus** at all large orders divisible by a power of 2 that depends
   on $m$ (Theorem G), and every modulus at large orders that are 0 or 4
   modulo each odd prime dividing $m$ (Theorem H).
5. **Kuperberg's Conjecture 5.1** for every prime $p\not\equiv1\pmod 8$, read
   with 0 counted as a square (Theorem D). Read literally, the conjecture
   fails at odd multiples of $p$.
6. **A negative remark on Problem 10:** a natural splicing gadget of order 129
   that would settle the 128-modular case cannot exist for one of the needed
   classes.

Not new: the direct-sum lemma (Lee–Szőllősi; Kuperberg), the projective and
Brouwer designs, Paley's matrices, and the use of
$(J-2I)\otimes(\text{Hadamard})$ starting matrices (Kuperberg). The
skew-conference assembly used for composite moduli is of a classical block
form and is not claimed as new.

These statements rest on a bounded comparison recorded in
[audit/PRIOR-ART.md](audit/PRIOR-ART.md). We found no earlier proof of
Theorems A–H in the sources examined. The full text of Eliahou's 2026 paper
was not openly accessible at the time of writing. This is not a claim of
global priority.

## Earlier work

- **Marrero and Butson (1972, 1973)**: definition of $m$-modular Hadamard
  matrices; the case $m=12$.
- **Lee and Szőllősi (2014)**, *Hadamard matrices modulo 5*: the case $m=5$
  and the direct-sum lemma.
- **Eliahou and Kervaire (2001)**: the case $m=32$.
- **Kuperberg (2016)**, *Hadamard matrices modulo p and small modular
  Hadamard matrices*: $m=7$ and $m=11$ at all sufficiently large orders, the
  iterated direct sum, and Conjecture 5.1.
- **Eliahou (2025, 2026)**: a 64-modular matrix of order 668, and 64-modular
  matrices in two progressions of orders.
- **Tseng (2026)**, Zenodo dataset: explicit 128- and 500-modular matrices of
  order 668.
- **Brouwer (1983)**, *An infinite series of symmetric designs*: the designs
  used for Theorems F and H.
- **Egan, Kotsireas, London and Ó Catháin (2026)**, *Recent progress in the
  construction of Hadamard matrices*: Problems 10 and 11.

## Evidence and limits

| Claim | Status |
|---|---|
| Theorem A ($m=7$) | proved on paper; audited by process-separated AI reviews, not human peer review; instance checks of both designs |
| Theorem B ($m=11$, 13) | proved on paper; audited as above; uses real Hadamard matrices of orders 1132 and 1244 announced in 2026; instance checks of two $m=11$ designs |
| Theorems C–E | proved on paper; audited as above |
| Theorems F–H, Proposition 15 | proved on paper; audited as above; one instance check at $m=140$ |
| Priority | bounded search; see [audit/PRIOR-ART.md](audit/PRIOR-ART.md) |

The instance checks build one matrix per design type and verify
$HH^{\mathsf T}\equiv nI\pmod m$ exactly, each with a negative control. They
check the splice algebra on finite instances; they do not replace the proofs.
Brouwer's designs and the McFarland and biplane designs in Theorem B were not
instance-checked. Thresholds in Theorems C and E–H are effective but were not
evaluated, apart from one example at $m=128$ in Section 6 of the paper.

## Reproduce

The checks need Python 3 with NumPy; the paper needs pdfLaTeX.

```sh
make verify PY=/path/to/python   # a few seconds on one core
make paper
```

`make verify` builds the instances, checks them, and compares the output with
its pinned copy in `evidence/`.

## Role of AI

AI assisted the derivations, the computer checks, the literature search and
the exposition under the author's direction. The constructions for $m=140$ and
the composite-modulus results (Theorems F–H, Proposition 15) were found by a
different AI system (Codex) working under the author's direction. Process-
separated AI reviews checked the proofs; they are not independent expert peer
review, and no independent human expert has examined the proofs. The audits
and their dispositions are in [audit/LEDGER.md](audit/LEDGER.md).

## License

GPL-3.0-only. See [LICENSE](LICENSE).
