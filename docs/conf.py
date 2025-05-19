# Configuration file for the Sphinx documentation builder.

import os
import sys
import pathlib

# -- Path setup ----------------------------------------------------------------

# Make _extensions importable
sys.path.insert(0, os.path.abspath("_extensions"))

# -- Conditional Extension Loading --------------------------------------------

# Load notebook_gallery_generator only when building the central docs/ page
if pathlib.Path(__file__).parent.resolve().name == "docs":
    extensions = [
        "sphinx.ext.githubpages",
        "myst_nb",
        "sphinx_design",
        "notebook_gallery_generator",
    ]
else:
    extensions = [
        "sphinx.ext.githubpages",
        "myst_nb",
        "sphinx_design",
    ]

# -- Project information -------------------------------------------------------
project = 'Jupyter Notebook Gallery'
copyright = '2024, Destination Earth Data Lake'
author = 'Christoph Reimer <christoph.reimer@eodc.eu>'

# -- General configuration -----------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "html_image",
    "dollarmath",
]

myst_url_schemes = ["http", "https", "mailto"]
myst_heading_anchors = 3
nb_execution_mode = 'off'

source_suffix = {
    ".ipynb": "myst-nb",
    ".myst": "myst-nb",
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "**/.git", ".pixi**"]

# -- HTML output configuration -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_logo = "https://hda.data.destination-earth.eu/ui/images/destination_earth_logo_W.svg"
html_favicon = "https://hda.data.destination-earth.eu/ui/images/favicon.svg"
html_title = "DEDL Notebook Gallery"

html_theme_options = {
    "logo": {
        "image_light": html_logo,
        "image_dark": html_logo,
        "link": "https://destination-earth.eu/",
        "alt_text": "Destination Earth",
    },
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/destination-earth",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
}

# -- Entry point for Sphinx ----------------------------------------------------
master_doc = 'index'

