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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'pyqgis'
copyright = '2024, https://creativecommons.org/licenses/by-nc-sa/4.0/'
author = 'Marie-Dominique Van Damme'

# The full version, including alpha/beta/rc tags
release = '1.0'


html_logo = "_static/ENSG_GEOMATIQUE.png"

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
#    project_name = "Développer en python sous QGis 3.x",
#    logo = "img/miro.png",
#    logo_alt = "PyQGIS",
#    logo_height = 59,
    #logo_url = "/",
#    logo_width = 45,
#    header_links = "Top 1|http://example.com/one, Top 2|http://example.com/two",
#    footer_links = ",".join([
#       "About Us|http://example.com/",
#        "Contact|http://example.com/contact",
#        "Legal|http://example.com/dev/null",
#    ]),
#copyright = "2021, My Company Inc."
#html_show_copyright = True
)

#html_last_updated_fmt = "%b %d, %Y"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# 
# "sphinx_wagtail_theme"
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "nbsphinx",
    "autodocsumm",
    "IPython.sphinxext.ipython_console_highlighting"
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#  alabaster
#html_theme = 'sphinx_wagtail_theme'
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_css_files = ["custom.css"]


# Add any relative paths that contain templates.
#templates_path = ["_templates"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names. "**" will apply the templates to all pages.
# The theme default is just searchbox and globaltoc.
html_sidebars = {"**": [
    "searchbox.html",
    "globaltoc.html",
#    "custom.html",    # Your template here
]}


