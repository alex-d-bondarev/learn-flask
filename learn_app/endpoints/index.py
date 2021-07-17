"""
Index Page
"""

from learn_app.main import app


@app.route("/")
def index():
    """Default url
    :return:
    """
    return "Index Page"
