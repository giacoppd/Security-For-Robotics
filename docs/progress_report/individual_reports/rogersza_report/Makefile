LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF	= dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

all: pdf

pdf:
	latex winter_report.tex
	bibtex winter_report
	latex winter_report.tex
	latex winter_report.tex
	dvips -R -Poutline -t letter winter_report.dvi -o winter_report.ps
	ps2pdf winter_report.ps

clean:
	rm -f *.dvi *.out *.aux *.log *.bbl *.blg *.ps *.pdf
