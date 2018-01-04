#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# esp8266dev documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 17 08:54:52 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
# import sys
# sys.path.insert(0, os.path.abspath('.'))


regexp = re.compile(r'.*__version__ = [\'\"](.*?)[\'\"]', re.S)
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
init_file = os.path.join(repo_root, 'src', '{{cookiecutter.package_name}}', '__init__.py')
with open(init_file, 'r') as f:
    module_content = f.read()
    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find __version__ in {}'.format(init_file))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = '{{cookiecutter.package_display_name}}'
copyright = '{{cookiecutter.year}}, {{cookiecutter.full_name}}'
author = '{{cookiecutter.full_name}}'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = False

# Suppress nonlocal image warnings
suppress_warnings = ['image.nonlocal_uri']


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'description': '{{cookiecutter.package_short_description}}',
    'show_powered_by': False,
    # 'logo': 'my-logo.png',
    'logo_name': False,
    'page_width': '80%',
}

# Custom sidebar templates, maps document names to template names.
#
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
