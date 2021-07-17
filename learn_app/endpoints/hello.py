"""
'Hello, World!' Page
"""

from learn_app.main import app


@app.route("/hello")
def hello():
    """Self evident

    :return:
    """
    return "Hello, World!"
