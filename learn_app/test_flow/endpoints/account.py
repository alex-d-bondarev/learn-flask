from learn_app.main import app


@app.route("/account", methods=["POST"])
def account():
    """Account CRUD"""
    # if request.method == "POST":
    return app.response_class(status=201)
