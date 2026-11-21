# Verification record

## Environment of the pinned run (2026-11-21)

- macOS, x86_64, one core, run under `nice`, BLAS limited to one thread.
- Python 3 with NumPy, in an isolated virtual environment.
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2021).

The program needs no network. Its SHA-256 hash is in
[MANIFEST.sha256](MANIFEST.sha256).

## Commands

```sh
make verify PY=/path/to/python
make paper
```

`make verify` runs [code/instance_checks.py](code/instance_checks.py), writes
`build/instance-checks.txt` and compares it byte for byte with
[evidence/instance-checks.txt](evidence/instance-checks.txt). It takes a few
seconds.

## What the instance checks cover

Each check builds a matrix with entries $\pm1$ and verifies
$HH^{\mathsf T}\equiv nI\pmod m$ exactly. A copy with one flipped entry must
fail. Design parameters are recomputed from the incidence matrices.

| Design (Lemma or Theorem) | Instance | Modulus |
|---|---|---|
| complement of PG(2,13), $(183,169,156)$ (Theorem A) | $H_{24}\to206\to388$ | 7 |
| complement of PG(6,3), $(1093,729,486)$ (Theorem A) | $H_{20}\to1112$ | 7 |
| $(23,12,6)$ (Theorem B) | $H_{24}\to46\to68$ | 11 |
| complement of PG(5,3), $(364,243,162)$ (Theorem B) | $H_{16}\to379$ | 11 |
| $(J_{11}-2I)^{\otimes2}$, then complement of PG(3,2), $(15,8,4)$ | $121\to135$ | 7 |
| $H_{20}\otimes\mathrm{MH}(135,7)$, Gram by the mixed-product rule | order 2700 | 140 |

These are finite checks of the splice algebra; the theorems rest on the proofs
in the paper. Brouwer's designs and the McFarland and biplane designs used in
Theorem B were not instance-checked.

## Paper

`make paper` builds [paper/main.pdf](paper/main.pdf) in three passes with
`SOURCE_DATE_EPOCH` fixed. Two builds give identical bytes.

PDF SHA-256: `d31409b435ca1bcae4c7f7ab7684d80b1fd9e65d616233039aab6c4c59877923`

The PDF in the tagged `v0.1.0` archive has SHA-256
`45a9e387e31c0246b0980df1465a37b76af474886cdf0d55e5fc44c6bb123192`; the living
copy differs only in its title-page line, which now carries the version DOI.
