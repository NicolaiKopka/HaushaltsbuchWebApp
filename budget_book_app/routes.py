from budget_book_app import app, test
from flask import render_template, request, url_for
from functions import db_functions


@app.route("/")
def index():
    db_functions.create_category_list()
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_page():
    category_list = db_functions.CATEGORY_LIST
    if request.method == "POST":
        db_functions.add_entry()
        return render_template("index.html")
    else:
        return render_template("form.html", data=None, categories=category_list)


@app.route("/overview")
def overview_page():
    #test.add_test_entries()
    data = db_functions.get_formatted_data()
    return render_template("overview.html", data=data)


@app.route("/edit/<entry_id>", methods=["GET", "POST"])
def edit_page(entry_id):
    entry = db_functions.get_entry_by_id(entry_id)
    category_list = db_functions.CATEGORY_LIST
    if request.method == "POST":
        db_functions.update_entry(entry)
        return overview_page()
    else:
        return render_template("form.html", data=entry, categories=category_list)


@app.route("/delete/<entry_id>")
def delete_entry(entry_id):
    entry = db_functions.get_entry_by_id(entry_id)
    db_functions.delete_entry(entry)
    return overview_page()







