SHELL := /bin/sh
PY ?= python3

PDFLATEX ?= pdflatex
export SOURCE_DATE_EPOCH := 1795219200
export FORCE_SOURCE_DATE := 1
export OPENBLAS_NUM_THREADS := 1
export OMP_NUM_THREADS := 1
export VECLIB_MAXIMUM_THREADS := 1
export MKL_NUM_THREADS := 1

.PHONY: paper verify

# Three passes from a clean extraction; no inherited auxiliaries are required.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	@! grep -E 'Warning:|Overfull|undefined references|undefined citations' paper/main.log
	@echo "paper built: paper/main.pdf"

# Build one instance per gadget type and check H H^T = n I (mod m) exactly
# (a few seconds on one core; needs Python 3 with NumPy), then compare the
# output with the pinned copy in evidence/.
verify:
	@mkdir -p build
	@$(PY) code/instance_checks.py > build/instance-checks.txt
	@if cmp -s evidence/instance-checks.txt build/instance-checks.txt; then echo "MATCH instance-checks.txt"; \
	  else echo "MISMATCH instance-checks.txt"; exit 1; fi
	@echo "verify: instance checks match evidence/"
