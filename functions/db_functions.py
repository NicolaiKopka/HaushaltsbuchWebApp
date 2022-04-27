import datetime
from budget_book_app.models import Entries
from budget_book_app import db
from flask import request


def add_entry():
    name = request.form["payee"]
    date_string = request.form["debit-date"]
    debit_date = datetime.date( int(date_string.split("-")[0]),
                                int(date_string.split("-")[1]),
                                int(date_string.split("-")[2]) )
    amount_string = request.form["fee"]
    amount = float(amount_string.replace(".", "").replace(",", "."))
    payment_interval = request.form["payment-interval"]
    data = Entries( name=name,
                    debit_date=debit_date,
                    amount=amount,
                    payment_interval=payment_interval)
    db.session.add(data)
    db.session.commit()


def update_entry(entry):
    entry.name = request.form["payee"]
    date_string = request.form["debit-date"]
    entry.debit_date = datetime.date( int(date_string.split("-")[0]),
                                      int(date_string.split("-")[1]),
                                      int(date_string.split("-")[2]) )
    amount_string = request.form["fee"]
    entry.amount = float(amount_string.replace(".", "").replace(",", "."))
    entry.payment_interval = request.form["payment-interval"]
    db.session.commit()


def delete_entry(entry):
    db.session.delete(entry)
    db.session.commit()


def get_formatted_data():
    data = Entries.query.all()
    page_settings = "de"
    if page_settings == "de":
        for elm in data:
            format_data_germany(elm)
    return data


def get_entry_by_id(entry_id):
    data = Entries.query.get(entry_id)

    amount_str = str(data.amount)
    formatted_amount = amount_str.replace(".", ",")
    data.amount = formatted_amount

    return data


def format_data_germany(elm):

    name = elm.payment_interval
    # match name:
    #     case "annual":
    #         elm.payment_interval = "Jährlich"
    #     case "half-yearly":
    #         elm.payment_interval = "Halbjährlich"
    #     case "quarterly":
    #         elm.payment_interval = "Vierteljährlich"
    #     case "monthly":
    #         elm.payment_interval = "Monatlich"

    formatted_date = elm.debit_date.strftime("%d.%m.%Y")
    elm.debit_date = formatted_date

    amount_str = str(elm.amount)
    amount_cent = amount_str.split(".")[1]
    amount = amount_str.split(".")[0]
    amount_list = list(amount)
    amount_list.reverse()
    new_amount_list = []
    for number in range(len(amount_list)):
        if number % 3 == 0 and number != 0:
            new_amount_list.append(amount_list[number] + ".")
        else:
            new_amount_list.append(amount_list[number])
    new_amount_list.reverse()
    formatted_amount = "".join([str(item) for item in new_amount_list])
    elm.amount = formatted_amount + "," + amount_cent



