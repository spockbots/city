# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import guzzle_sphinx_theme

sys.path.insert(0, os.path.abspath('../../lego/.'))
sys.path.insert(0, os.path.abspath('../../dummy/.'))


# -- Project information -----------------------------------------------------

project = 'Spockbots'
copyright = '2019, Spockbots'
author = 'Spockbots'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.todo',
        'sphinx.ext.githubpages',
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

if False:
    html_theme_path = guzzle_sphinx_theme.html_theme_path()
    html_theme = 'guzzle_sphinx_theme'
    html_theme_options = {
        # Set the name of the project to appear in the sidebar
        "project_nav_name": "Spockbots",
    }

#html_theme = 'sphinx_rtd_theme'

#html_theme = 'agogo'

html_theme = 'alabaster'
#html_theme = 'sphinxdoc'
#html_theme = 'scrolls'

#html_theme = 'haiku'

#html_theme = 'nature'

#html_theme = 'traditional'




# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}