from learn_app.main import app


@app.route("/do_something_private", methods=["POST"])
def do_something_private():
    """Simulate some processing on backend

    :return:
    """
    return app.response_class(status=400)
