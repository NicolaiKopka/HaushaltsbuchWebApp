from budget_book_app.models import Entries, BankAccountStatus
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

    date_string = "2022-08-12"
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

    date_string = "2022-05-10"
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

def add_test_bank_status():
    date_string = "2022-05-13"
    date = datetime.date(int(date_string.split("-")[0]),
                         int(date_string.split("-")[1]),
                         int(date_string.split("-")[2]))
    current_bank_balance = 3454.35
    current_salary = 2213.45
    data = BankAccountStatus(date=date,
                             current_salary=current_salary,
                             current_bank_balance=current_bank_balance)
    db.session.add(data)
    db.session.commit()