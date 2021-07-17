"""
print <text> endpoint
Shows a page with "Given text <text>"
"""

from markupsafe import escape

from learn_app.main import app


@app.route("/print/<text>")
def print_text(text):
    """Print given text

    :return:
    """
    return "Given text %s" % escape(text)
