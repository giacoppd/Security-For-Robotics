LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex $(x).tex
	dvips -R -Poutline -t letter $(x).dvi -o $(x).ps
	ps2pdf $(x).ps
	mv $(x).pdf pdfs/
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf
