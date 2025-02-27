import os
import sys

sys.path.insert(0, os.path.abspath("../../src/switchai"))

project = "SwitchAI"

html_theme = "furo"

html_title = "SwitchAI Docs"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    # Adds a convenient copy button to code blocks.
    "sphinx_copybutton",
    # Automagically adds Open Graph meta tags.
    "sphinxext.opengraph",
    "myst_parser",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence"]

# Show only class names.
add_module_names = False

# Keep the type hints outside the function signature, moving them to the
# descriptions of the relevant function/methods.
autodoc_typehints = "description"

html_static_path = ["_static"]
html_css_files = ["custom.css"]
