LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex srs_template.tex
	bibtex srs_template
	latex srs_template.tex
	latex srs_template.tex
	dvips -R -Poutline -t letter srs_template.dvi -o srs_template.ps
	ps2pdf srs_template.ps

clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf
