LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex requirements_formatting.tex
	bibtex requirements_formatting
	latex requirements_formatting.tex
	latex requirements_formatting.tex
	dvips -R -Poutline -t letter requirements_formatting.dvi -o requirements_formatting.ps
	ps2pdf requirements_formatting.ps

clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf
