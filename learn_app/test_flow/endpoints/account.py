from flask import request

from learn_app.main import app, db
from learn_app.test_flow.models.account import Account


@app.route("/account", methods=["DELETE", "POST", "PUT"])
def account():
    """Account CRUD"""
    req_form = request.form

    if request.method == "DELETE":
        return delete_account(req_form)
    elif request.method == "POST":
        return create_new_account(req_form)
    else:
        return update_existing_account(req_form)


def delete_account(req_form):
    """Self evident

    :param req_form:
    :return:
    """
    Account.query.filter_by(name=req_form.get("name")).delete()
    return make_record_change()


def make_record_change():
    """Save change to DB and return 204 code

    :return:
    """
    db.session.commit()
    return app.response_class(status=204)


def update_existing_account(req_form):
    """Self evident

    :param req_form:
    :return:
    """
    updated_account = Account.query.filter_by(name=req_form.get("name")).first()
    updated_account.number = req_form.get("number")
    return make_record_change()


def create_new_account(req_form):
    """Self evident

    :param req_form:
    :return:
    """
    new_account = Account(name=req_form.get("name"), number=req_form.get("number"))
    db.session.add(new_account)
    return app.response_class(status=201)
