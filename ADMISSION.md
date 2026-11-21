# Admission record

**Current state:** ADMITTED

Current verdict: ADMITTED (2026-11-21)

**Version:** 0.1.0

**Tag:** `v0.1.0` → `6cc836f93f338324024024f6de0a8858395ea8cc`

**Version DOI:** [`10.5281/zenodo.24421216`](https://doi.org/10.5281/zenodo.24421216) · **Concept DOI:** `10.5281/zenodo.24421215` · **Record:** <https://zenodo.org/records/24421216>

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** The author approved the paper's abstract and
introduction on 2026-11-21.

## Principal claims

1. 7-modular Hadamard matrices exist at every order divisible by 4 (Theorem A),
   answering Problem 11 of arXiv 2610.27175.
2. 11- and 13-modular Hadamard matrices exist at every order divisible by 4
   (Theorem B), using real Hadamard matrices of orders 1132 and 1244 announced
   in 2026, each needed only at that order.
3. Asymptotic existence at all large orders divisible by 4 for every odd prime,
   every power of 2, and every $m$ of the form $4p^a$ or $4pq$ (Theorems C, E,
   F); every $m$ at large orders divisible by $2^{L(m)}$ (Theorem G) or
   divisible by 4 and congruent to 0 or 4 modulo each odd prime dividing $m$
   (Theorem H); Kuperberg's Conjecture 5.1, with 0 counted as a square, for
   $p\not\equiv1\pmod8$ (Theorem D). New for odd primes from 13 on and for
   powers of 2 from 128 on; smaller cases were known or announced.

## Gates

| Gate | Status | Evidence or residual |
|---|---|---|
| P1 prior work and credit | PARTIAL, residual accepted | [audit/PRIOR-ART.md](audit/PRIOR-ART.md) and the search log; scans of 20–21 Nov 2026, within 7 days of the tag. Residual: the full text of Eliahou 2026 was not openly accessible at the time of writing; its abstract, Eliahou 2025 and the survey's report of Eliahou's announcements are credited. The author accepted this residual on 2026-11-21, before the tag |
| A1 claim and artifact consistency | PASS | proof audits and two cold reads before release; claims, citation and reproducibility audits of 2026-11-21, findings fixed and re-checked; dispositions in [audit/LEDGER.md](audit/LEDGER.md) |
| R1 release and stewardship | PASS | See below |

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction | PASS | fresh `git archive` extraction: `make verify` MATCH; deterministic `make paper`, byte-identical to the committed PDF |
| Artifact integrity | PASS | `MANIFEST.sha256` covers every tracked file |
| Hygiene | PASS | README math rendered by GitHub, every span recognized; no private paths or emails |
| Stewardship | PASS | [CORRECTIONS.md](CORRECTIONS.md) |
| Immutable semantic tag | PASS | annotated `v0.1.0` (object `76d1b77`) → `6cc836f`; tagger is the GitHub noreply identity |
| Public permanent archive with provider byte identity | PASS | the pinned GitHub `zipball/v0.1.0` (downloaded twice, identical) and the Zenodo file are byte-identical: 508732 bytes, SHA-256 `a6bdf8750dbcf6a0ce8da182b74d805b917fd45614648d51be1aaf5a6da77345`; Zenodo MD5 `ed09fef1a8ed6a87a1b694f07cb86e62` |
| DOI resolves; living repository identifies the version | PASS | `doi.org/10.5281/zenodo.24421216` redirects to the Zenodo record; README, `CITATION.cff` and the living paper carry the version DOI |
| Archive metadata matches repository | PASS | title, creator Kline, Jeffery, version v0.1.0, publication date 2026-11-21, license `gpl-3.0` |
| Machine-readable citation | PASS | `CITATION.cff` with version DOI, concept DOI and `date-released: 2026-11-21` |

**Admission verdict:** ADMITTED (2026-11-21). The P1 residual and the limits
stated in the README remain. No independent human expert has reviewed the
paper.

## Archive verification

- Route: Zenodo GitHub integration; no manual deposit.
- Pinned before the GitHub Release: GitHub API `zipball/v0.1.0`, downloaded
  twice, identical, 508732 bytes, SHA-256
  `a6bdf8750dbcf6a0ce8da182b74d805b917fd45614648d51be1aaf5a6da77345`.
- Zenodo file `jeff-kline/modular-hadamard-large-orders-v0.1.0.zip`: identical
  to the pinned zipball.
- Separate determinism check: `git archive --format=zip v0.1.0`, generated
  twice, identical, 508186 bytes, SHA-256
  `5991c2bd5fe669190f884cf1570375a44ff1781376af19193d9f73e4da82dcd3`; a
  different file from the provider zipball, not compared with it.
- Mechanical audit at the archived state, on the unchanged tagged tree:
  11 pass, 0 warnings, 0 fail.

## External actions and owners

| Action | Owner | Status |
|---|---|---|
| Private GitHub repository and push | author authorization | done 2026-11-21 |
| Public visibility, secret scanning and push protection | author authorization | done 2026-11-21 |
| Zenodo enablement before the Release | author, in the Zenodo portal | done 2026-11-21 |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | done 2026-11-21 14:58 UTC: Release "Version 0.1.0" |
| Public-site listing | author authorization | landing entry at <https://jeff-kline.github.io/>; Pages build and live HTML checked for title, blurb, repository link and version DOI before this record was pushed |
