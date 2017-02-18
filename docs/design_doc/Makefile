LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex design_doc.tex
	bibtex design_doc
	latex design_doc.tex
	latex design_doc.tex
	dvips -R -Poutline -t letter design_doc.dvi -o design_doc.ps
	ps2pdf design_doc.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf