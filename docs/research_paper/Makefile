LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex research.tex
	bibtex research
	latex research.tex
	latex research.tex
	dvips -R -Poutline -t letter research.dvi -o research.ps
	ps2pdf research.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.p