from budget_book_app import db


class Entries(db.Model):
    #__tablename__ = "All_Entries"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=False, nullable=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    debit_date = db.Column(db.Date, unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    payment_interval = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '<Entries %r>' % self.name