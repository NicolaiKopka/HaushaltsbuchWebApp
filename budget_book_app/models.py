from budget_book_app import db


class Entries(db.Model):
    # __tablename__ = "Kategorie1"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    debit_date = db.Column(db.Date, unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    payment_interval = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '<Entries %r>' % self.name