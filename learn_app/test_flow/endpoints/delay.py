from learn_app.main import app


@app.route("/delay")
def get_delay():
    """Get processing delay

    :return:
    """
    return app.response_class(
        status=200
    )
