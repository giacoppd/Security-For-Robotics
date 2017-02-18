LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex midterm_progress.tex
	bibtex midterm_progress
	latex midterm_progress.tex
	latex midterm_progress.tex
	dvips -R -Poutline -t letter midterm_progress.dvi -o midterm_progress.ps
	ps2pdf midterm_progress.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf