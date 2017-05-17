LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex whitepaper.tex
	bibtex whitepaper
	latex whitepaper.tex
	latex whitepaper.tex
	dvips -R -Poutline -t letter whitepaper.dvi -o whitepaper.ps
	ps2pdf whitepaper.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf