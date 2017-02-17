LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex midterm_revisions.tex
	bibtex midterm_revisions
	latex midterm_revisions.tex
	latex midterm_revisions.tex
	dvips -R -Poutline -t letter midterm_revisions.dvi -o midterm_revisions.ps
	ps2pdf midterm_revisions.ps

clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf
