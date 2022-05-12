import sqlite3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

from budget_book_app import routes

if not os.path.exists("test.db"):
    db.create_all()
