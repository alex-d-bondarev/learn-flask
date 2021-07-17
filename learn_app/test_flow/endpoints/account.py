from flask import request

from learn_app.main import app, db
from learn_app.test_flow.models.account import Account


@app.route("/account", methods=["POST"])
def account():
    """Account CRUD"""
    # if request.method == "POST":
    req_form = request.form
    new_account = Account(name=req_form.get("name"), number=req_form.get("number"))
    db.session.add(new_account)
    return app.response_class(status=201)
