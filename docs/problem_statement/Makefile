LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex ProblemStatement.tex
	bibtex ProblemStatement
	latex ProblemStatement.tex
	latex ProblemStatement.tex
	dvips -R -Poutline -t letter ProblemStatement.dvi -o ProblemStatement.ps
	ps2pdf ProblemStatement.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf
