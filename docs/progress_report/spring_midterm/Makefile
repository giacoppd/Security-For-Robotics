LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex spring_midterm.tex
	bibtex spring_midterm
	latex spring_midterm.tex
	latex spring_midterm.tex
	dvips -R -Poutline -t letter spring_midterm.dvi -o spring_midterm.ps
	ps2pdf spring_midterm.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf