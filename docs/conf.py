
project = "Chronicles of Hope"
author = "Ron Georgia"
version = "0.0.1"
copyright = "2025, Ronverbs, LLC"
show_authors = True

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxnotes.strike",
    "sphinx_design",
    "sphinx_collapse",
    "myst_parser",
]
myst_enable_extensions = ["colon_fence"]
python_maximum_signature_line_length = 60

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_css_files = [
    "style.css",
]

html_static_path = ["_static"]
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# Consider using alabaster
html_theme = "alabaster"
html_theme_options = {
    "description": "",
    "page_width": "95%",
    "body_max_width": "auto",
    "fixed_sidebar": "false",
    "sidebar_collapse": "true",
}
