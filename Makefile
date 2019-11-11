all:
	mkdir -p docs-source/source/src
	# cd lego; sphinx-apidoc  -f -o ../docs-source/source/ .
	rm -rf docs
	cd docs-source; make html
	make clean
	make -f Makefile view


pdf:
	cd docs-source; make latexpdf

pdfview:
	open -a skim docs/latex/spockbots.pdf


view:
	open docs/html/index.html

clean:
	rm -rf code/spockbots.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf docs-source/build

real-clean:
	rm -rf docs

