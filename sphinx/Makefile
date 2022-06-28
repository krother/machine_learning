# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = spiced_datascience
SOURCEDIR     = .
BUILDDIR      = _build

# path to find quiz extension
export PYTHONPATH=$PYTHONPATH:.

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.ONESHELL:
# publishes the documentation on pythonanywhere
deploy:
	sphinx-build -b html -j4 -D group=students -D todo_include_todos=0 . _build/html
	scp -r _build/html/* krspiced@ssh.pythonanywhere.com:datascience/

teach:
	sphinx-build -b html -j4 -D group=teachers . _build/html_teachers

dockerbuild:
	docker build -t ds_source .
	docker run -v $(CURDIR):/usr/src/app -itd --name ds_source ds_source
	docker exec -it ds_source make teach
	docker stop ds_source && docker rm ds_source

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
