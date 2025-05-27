import os
import sys
import pathlib

# -- Path setup ----------------------------------------------------------------
sys.path.insert(0, os.path.abspath("_extensions"))

# -- Conditional Extension Loading --------------------------------------------
if pathlib.Path(__file__).parent.resolve().name == "docs":
    extensions = [
        "sphinx.ext.githubpages",
        "myst_nb",
        "myst_parser",  # <--- HIER ergänzt
        "sphinx_design",
        "notebook_gallery_generator",
    ]
else:
    extensions = [
        "sphinx.ext.githubpages",
        "myst_nb",
        "myst_parser",  # <--- HIER ergänzt
        "sphinx_design",
    ]
# -- Project information -------------------------------------------------------
project = 'DestinE DataLake Lab'
copyright = '2024, Destination Earth Data Lake'
author = 'DestinE Data Lake Team'

# -- General configuration -----------------------------------------------------
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "**/.git", ".pixi**", "book/**"]

source_suffix = {
    ".ipynb": "myst-nb",
    ".myst": "myst-nb",
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
]

myst_url_schemes = ["http", "https", "mailto"]
myst_heading_anchors = 3
nb_execution_mode = 'off'
nb_execution_timeout = 3600
nb_execution_allow_errors = False

# -- HTML output configuration -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_title = "DestinE DataLake Lab"
html_logo = "https://hda.data.destination-earth.eu/ui/images/destination_earth_logo_W.svg"
html_favicon = "https://hda.data.destination-earth.eu/ui/images/favicon.svg"
html_static_path = ['_static']
html_css_files = ['custom.css']

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
    "collapse_navigation": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/destination-earth/DestinE-DataLake-Lab",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
}

# -- Launch button config (Binder/JupyterHub) ----------------------------------
launch_buttons = {
    "notebook_interface": "jupyterlab",
    "binderhub_url": "https://binder-217-71-193-124.nip.io",
    # "jupyterhub_url": "https://jupyter.central.data.destination-earth.eu/",
}

# -- Repository link in nav ----------------------------------------------------
repository = {
    "url": "https://github.com/destination-earth/DestinE-DataLake-Lab",
    "branch": "notebook-gallery",
    # "path_to_book": "book",
}

# -- Entry point ---------------------------------------------------------------
master_doc = 'index'
