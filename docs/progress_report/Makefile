LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex progress_report.tex
	bibtex progress_report
	latex progress_report.tex
	latex progress_report.tex
	dvips -R -Poutline -t letter progress_report.dvi -o progress_report.ps
	ps2pdf progress_report.ps
 
clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf