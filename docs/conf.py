
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
# html_theme = "alabaster"
html_theme = "furo"

match html_theme:
    case "alabaster":
        html_theme_options = {
            "description": "",
            "page_width": "95%",
            "body_max_width": "auto",
            "fixed_sidebar": "false",
            "sidebar_collapse": "true",
        }
    case "furo":
        html_theme_options = {
                "light_css_variables": {
                    "color-brand-content": "#CC3333",
                    "color-background-primary": "#f8f9fb",
                    },
                "sidebar_hide_name": True,
                "announcement": "Because I can't remember squat",
                "source_view_link": "https://github.com/rgeorgia/chronicle-my-brain.git",
                "source_branch": "main",
                "source_directory": "docs/",
        }
    case "sphinx_rtd_theme":
        html_theme_options = {
            "logo_only": False,
            "body_max_width": "auto",
            "prev_next_buttons_location": "bottom",
            "style_external_links": False,
            "vcs_pageview_mode": "display_github",
            "style_nav_header_background": "white",
            "flyout_display": "hidden",
            "version_selector": True,
            "collapse_navigation": True,
            "sticky_navigation": True,
            "navigation_depth": 4,
            "includehidden": True,
            "titles_only": False,
        }

