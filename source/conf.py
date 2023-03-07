# Configuration file for the Sphinx documentation builder.
project = 'DevOps'
copyright = '2023, skillab'
author = 'skillab'
release = '1'

extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx.ext.duration', #  will see a short durations report at the end of the console output
    'sphinx.ext.todo', 
    ]

pygments_style = 'sphinx'

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['venv']

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

html_theme_options = {
    "navigation_depth": -1
}

html_logo = "_static/Logo.jpg"

html_css_files = ['max_width.css']
