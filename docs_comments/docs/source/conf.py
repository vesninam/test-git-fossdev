# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

project = 'sales'
copyright = '2026, Artem Vesnin'
author = 'Artem Vesnin'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# `myst_parser` добавляет поддержку Markdown. 
# `autodoc` вытягивает документацию из docstring. 
# `napoleon` позволяет писать docstring в привычных стилях Google или NumPy. 
# `autosummary` помогает генерировать обзорные страницы для API. 
# `viewcode` добавляет ссылки на исходный код, что делает API-справку полезнее при чтении.

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext"
}

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
