from flask import request
from flask_restx import Namespace, Resource

from setup_db import db
from models import Book

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):

    def get(self):
        books = db.session.query(Book).all()
        res = []
        for b in books:
            data = b.__dict__
            del data['_sa_instance_state']
            res.append(data)
        return res, 200

    def post(self):
        data = request.json

        new_book = Book(**data)

        db.session.add(new_book)
        db.session.commit()
        return '', 201


@book_ns.route('/<int:bid>')
class BookView(Resource):

    def get(self, bid):
        book = db.session.query(Book).get_or_404(bid)
        res = book.__dict__
        del res['_sa_instance_state']
        return res, 200

    def put(self, bid):
        book = db.session.query(Book).get_or_404(bid)
        data = request.json

        book.name = data.get('name')
        book.author = data.get('author')
        book.year = data.get('year')
        book.pages = data.get('pages')

        db.session.add(book)
        db.session.commit()
        return '', 204

    def delete(self, bid):
        book = db.session.query(Book).get_or_404(bid)

        db.session.delete(book)
        db.session.commit()
        return '', 204
