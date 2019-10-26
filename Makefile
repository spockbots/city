all:
	cd docs-source; sphinx-apidoc -f -o source/ ../../city
	cd docs-source; make html
	make -f Makefile view

view:
	open docs/html/index.html
