#use "make report" to create pdf, "make clean" to clean
DOCNAME=main

all: report

.PHONY: clean

dereport:
	xelatex $(DOCNAME).tex
	bibtex $(DOCNAME).aux


	xelatex $(DOCNAME).tex
	xelatex $(DOCNAME).tex




report:
	pdflatex $(DOCNAME).tex
	bibtex $(DOCNAME).aux


	pdflatex $(DOCNAME).tex
	pdflatex $(DOCNAME).tex

view: report
	open $(DOCNAME).pdf

clean:
	rm *.blg *.bbl *.aux *.log