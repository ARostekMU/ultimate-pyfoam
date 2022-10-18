"""Sphinx configuration."""
project = "Ultimate PyFoam"
author = "Andrej Rostek"
copyright = "2022, Andrej Rostek"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
    "autoapi.extension",
]
autodoc_typehints = "description"
html_theme = "furo"
autoapi_dirs = ["../src"]
