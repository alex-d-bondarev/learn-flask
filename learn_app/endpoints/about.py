"""
About Page
"""

from learn_app.main import app


@app.route("/about")
def about():
    """Self evident

    :return:
    """
    return "The about page"
