# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BIO120'
copyright = '2025, Sharon Long, Naima Sharaf, Jonas Cremer'
author = 'Sharon Long, Naima Sharaf, Jonas Cremer'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'nbsphinx', 'sphinx.ext.coverage',
              'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# html_logo = "_static/logo_horizontal-02.png"
html_theme_options = {
    "logo_only": True,
    "sticky_navigation": True,
    "collapse_navigation": True,
    "style_nav_header_background": "#0f4d70",
}

html_logo = "_static/bio120_logo.png"
html_css_files = ['css/custom.css']
html_theme_options = {
     "logo": {
         "image_dark": '_static/bio120_logo.png',
         "image_light": '_static/bio120_logo.png',
     } #,
     #"navbar_end": ["navbar-icon-links"]
     }
html_context = {"default_mode": "light"}


# html_css_files = [
#     'css/custom.css',
# ]
