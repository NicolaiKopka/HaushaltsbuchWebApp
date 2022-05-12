from budget_book_app.models import Entries
from budget_book_app import db
import datetime

def add_test_entries():
    date_string = "2022-03-12"
    debit_date = datetime.date(int(date_string.split("-")[0]),
                               int(date_string.split("-")[1]),
                               int(date_string.split("-")[2]))
    data = Entries(category="Kategorie 1",
                   name="HVV",
                   debit_date=debit_date,
                   amount=12.45,
                   payment_interval="yearly")
    db.session.add(data)

    date_string = "2022-05-12"
    debit_date = datetime.date(int(date_string.split("-")[0]),
                               int(date_string.split("-")[1]),
                               int(date_string.split("-")[2]))
    data = Entries(category="Kategorie 1",
                   name="BVG",
                   debit_date=debit_date,
                   amount=16.45,
                   payment_interval="yearly")
    db.session.add(data)

    date_string = "2022-05-24"
    debit_date = datetime.date(int(date_string.split("-")[0]),
                               int(date_string.split("-")[1]),
                               int(date_string.split("-")[2]))
    data = Entries(category="Kategorie 2",
                   name="Essen",
                   debit_date=debit_date,
                   amount=200.45,
                   payment_interval="yearly")
    db.session.add(data)

    date_string = "2021-05-10"
    debit_date = datetime.date(int(date_string.split("-")[0]),
                               int(date_string.split("-")[1]),
                               int(date_string.split("-")[2]))
    data = Entries(category="Kategorie 1",
                   name="Trinken",
                   debit_date=debit_date,
                   amount=20.45,
                   payment_interval="yearly")
    db.session.add(data)
    db.session.commit()