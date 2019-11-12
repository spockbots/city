simple: html
	make clean
	make -f Makefile view


html:
	mkdir -p docs-source/source/src
	# cd lego; sphinx-apidoc  -f -o ../docs-source/source/ .
	# rm -rf docs/html
	cd docs-source; make html

pdf:
	cd docs-source; make latexpdf
	mv docs/latex/spockbots.pdf docs
	rm -rf docs/latex

publish: html pdf
	git commit -m "documentation update" docs/spockbots.pdf docs/html
	git push



pdfview:
	open -a skim docs/spockbots.pdf


view:
	open docs/html/index.html

clean:
	rm -rf code/spockbots.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf docs-source/build

real-clean:
	rm -rf docs

