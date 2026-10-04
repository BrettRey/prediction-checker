# Makefile for LaTeX paper compilation

# Configuration
# pdfLaTeX, not the house XeLaTeX: the EJW class's XeLaTeX path needs Microsoft
# Garamond, which isn't installed here; its pdfLaTeX path uses EB Garamond (DECISIONS.md, 2026-10-04).
LATEX = pdflatex
# The EJW class files live in ejw/ (gitignored; download link in README.md).
export TEXINPUTS := ./ejw//:$(TEXINPUTS)
BIBER = biber
MAIN = tv-unbundling-forecast-check
PDF_BASENAME ?= $(MAIN)
SUBMISSION_PDF = $(PDF_BASENAME).pdf
OUTDIR = .

# Targets
.PHONY: all quick refresh-submission-pdf clean distclean view help test

# Default target: build the PDF
all: $(MAIN).pdf

# Full build sequence with bibliography
$(MAIN).pdf: $(MAIN).tex references.bib references-local.bib $(wildcard sections/*.tex) $(wildcard figures/*.pdf) $(wildcard ejw/*.cls)
	@echo "==> First LaTeX pass..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Running Biber..."
	$(BIBER) $(MAIN)
	@echo "==> Second LaTeX pass..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Third LaTeX pass (finalizing)..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Build complete: $(MAIN).pdf"

refresh-submission-pdf:
	@if [ "$(SUBMISSION_PDF)" != "$(MAIN).pdf" ]; then \
		cp -f "$(MAIN).pdf" "$(SUBMISSION_PDF)"; \
	fi
	@echo "==> Submission/preprint PDF ready: $(SUBMISSION_PDF)"

# Quick build (single pass, no bibliography update)
quick: $(MAIN).tex
	@echo "==> Quick build (single pass)..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@$(MAKE) --no-print-directory refresh-submission-pdf

# Use LuaLaTeX instead of XeLaTeX (not recommended - breaks PDF text layer)
lualatex: LATEX = lualatex
lualatex: all

# Clean build artifacts (keep PDF)
clean:
	@echo "==> Cleaning build artifacts..."
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg $(MAIN).log
	rm -f $(MAIN).out $(MAIN).run.xml $(MAIN).toc $(MAIN).fdb_latexmk
	rm -f $(MAIN).fls $(MAIN).synctex.gz
	@echo "==> Clean complete"

# Clean everything including PDF
distclean: clean
	@echo "==> Removing PDF..."
	rm -f "$(MAIN).pdf"
	@if [ "$(SUBMISSION_PDF)" != "$(MAIN).pdf" ]; then \
		rm -f "$(SUBMISSION_PDF)"; \
	fi
	@echo "==> Deep clean complete"

# Open named submission/preprint PDF viewer (macOS)
view: $(SUBMISSION_PDF)
	@echo "==> Opening PDF..."
	open "$(SUBMISSION_PDF)"

# Test the Python specification
test:
	@echo "==> Tests"
	@echo "No tests yet."

# Show available targets
help:
	@echo "Available targets:"
	@echo "  make          - Build the PDF"
	@echo "  make quick    - Quick build (single pass) and refresh named PDF"
	@echo "  make lualatex - Build using LuaLaTeX (not recommended)"
	@echo "  make clean    - Remove build artifacts (keep PDF)"
	@echo "  make distclean- Remove everything including PDF"
	@echo "  make view     - Open named submission/preprint PDF (macOS only)"
	@echo "  make test     - Run Python specification tests"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "Configuration:"
	@echo "  PDF_BASENAME  - File-safe basename for upload PDF (default: project directory)"
