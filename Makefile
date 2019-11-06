all:
	mkdir -p docs-source/source/src
	# cd lego; sphinx-apidoc  -f -o ../docs-source/source/ .
	cd docs-source; make html
	make -f Makefile view
	cd docs-source; make latexpdf

view:
	open docs/html/index.html

clean:
	rm -rf code/spockbots.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf docs
	rm -rf docs-source/build

