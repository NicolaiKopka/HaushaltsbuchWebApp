import datetime
from budget_book_app.models import Entries, WorkingData
from budget_book_app import db
from dateutil.relativedelta import relativedelta

# following are the functions to repeat every entry in db, for the interval that is set respectively
# the entries are repeated for this year and the following only
# triggers when db_functions.add_entry is called


def repeats_yearly(data):
    current_date = data.debit_date
    months_to_increase = 0
    for repetition in range(1):
        new_date = current_date + relativedelta(months=months_to_increase)
        add_to_working_data(data, new_date)
        months_to_increase += 12


def repeats_half_yearly(data):
    current_date = data.debit_date
    months_to_increase = 0
    for repetition in range(2):
        new_date = current_date + relativedelta(months=months_to_increase)
        add_to_working_data(data, new_date)
        months_to_increase += 6


def repeats_quarterly(data):
    current_date = data.debit_date
    months_to_increase = 0
    for repetition in range(6):
        new_date = current_date + relativedelta(months=months_to_increase)
        add_to_working_data(data, new_date)
        months_to_increase += 3


def repeats_monthly(data):
    current_date = data.debit_date
    months_to_increase = 0
    for repetition in range(12):
        new_date = current_date + relativedelta(months=months_to_increase)
        add_to_working_data(data, new_date)
        months_to_increase += 1


def add_to_working_data(data, new_date):
    debit_date = new_date
    category = data.category
    name = data.name
    amount = data.amount
    payment_interval = data.payment_interval
    repeat_data = WorkingData(category=category,
                              name=name,
                              debit_date=debit_date,
                              amount=amount,
                              payment_interval=payment_interval)
    db.session.add(repeat_data)
    db.session.commit()
