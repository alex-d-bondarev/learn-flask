"""
translate endpoint
Shows a page with given http code and corresponding http code name
"""
from learn_app.http_code_response import make_http_code_translation
from learn_app.main import app


@app.route("/translate")
def translate_http_code():
    """Print given code

    :return:
    """
    return make_http_code_translation(app)
