# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'learning_transformer'
copyright = '2024, Colin'
author = 'Colin'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
#	'sphinx.ext.mathjax',
    'myst_parser',
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.mermaid",
	]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

source_suffix = {'.rst': 'restructuredtext', 
                 '.md': 'markdown', 
                 '.MD': 'markdown',
                 }
                 

#source_parsers = {
#    '.md' : 'recommonmark.parser.CommonMarkParser',
#    '.MD' : 'recommonmark.parser.CommonMarkParser',
#}
