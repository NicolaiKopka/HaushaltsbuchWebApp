from budget_book_app import db


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=False, nullable=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    debit_date = db.Column(db.Date, unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    payment_interval = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '<Entries %r>' % self.name


class WorkingData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=False, nullable=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    debit_date = db.Column(db.Date, unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    payment_interval = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '<WorkingData %r>' % self.name


class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debit_date = db.Column(db.Date, unique=False, nullable=False)
    category = db.Column(db.String(80), unique=False, nullable=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    payment_interval = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '<Archive %r>' % self.name


class BankAccountStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    current_bank_balance = db.Column(db.Float, unique=False, nullable=False)
    current_salary = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<Bank_Account_Status %r>' % self.name