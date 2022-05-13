import datetime
from budget_book_app.models import Entries, Archive
from budget_book_app import db


def add_entries_by_current_month():
    current_month_entries = get_current_month_entries()
    for entry in current_month_entries:
        category = entry.category
        name = entry.name
        debit_date = entry.debit_date
        amount = entry.amount
        payment_interval = entry.payment_interval
        data = Archive (category=category,
                        name=name,
                        debit_date=debit_date,
                        amount=amount,
                        payment_interval=payment_interval)
        db.session.add(data)
        db.session.commit()


def get_current_month_entries():
    current_date = datetime.datetime.now()
    current_month = current_date.month
    data = Entries.query.all()
    current_month_entries = [elm for elm in data if elm.debit_date.month == current_month]
    return current_month_entries
