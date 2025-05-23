
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
html_theme = "furo"
# html_theme = "alabaster"
"""
html_theme_options = {
    "description": "",
    "page_width": "95%",
    "body_max_width": "auto",
    "fixed_sidebar": "false",
    "sidebar_collapse": "true",
}
"""
html_theme_options = {
    "light_logo": "logo-light-mode.png",
    "dark_logo": "logo-dark-mode.png",
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "github",
    "style_nav_header_background": "white",
    "flyout_display": "hidden",
    "version_selector": True,
    "language_selector": True,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False
}

