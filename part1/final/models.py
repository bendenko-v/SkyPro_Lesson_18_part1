# текст задания находится в файле app.py
from setup_db import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    author = db.Column(db.String(200))
    year = db.Column(db.Integer)
    pages = db.Column(db.Integer)


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
