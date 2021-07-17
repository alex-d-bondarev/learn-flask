from flask import request

from learn_app.main import app, db
from learn_app.test_flow.models.account import Account


@app.route("/account", methods=["POST", "PUT"])
def account():
    """Account CRUD"""
    req_form = request.form

    if request.method == "POST":
        return create_new_account(req_form)
    else:
        return update_existing_account(req_form)


def update_existing_account(req_form):
    """Self evident

    :param req_form:
    :return:
    """
    updated_account = Account.query.filter_by(name=req_form.get("name")).first()
    updated_account.number = req_form.get("number")
    db.session.commit()
    return app.response_class(status=204)


def create_new_account(req_form):
    """Self evident

    :param req_form:
    :return:
    """
    new_account = Account(name=req_form.get("name"), number=req_form.get("number"))
    db.session.add(new_account)
    return app.response_class(status=201)
