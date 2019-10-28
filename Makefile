all:
	cd code; pip install .
#	mkdir -p docs-source/source/src
	cd code; sphinx-apidoc -f -o ../docs-source/source/ .
	cd docs-source; make html
	make -f Makefile view

view:
	open docs/html/index.html

clean:
	rm -rf code/spockbots.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf docs
	rm -rf docs-source/build

