from flask import request
from flask_restx import Namespace, Resource

from setup_db import db
from models import Review

review_ns = Namespace('reviews')


@review_ns.route('/')
class ReviewsView(Resource):

    def get(self):
        reviews = db.session.query(Review).all()
        res = []
        for r in reviews:
            data = r.__dict__
            del data['_sa_instance_state']
            res.append(data)
        return res, 200

    def post(self):
        data = request.json

        new_review = Review(**data)

        db.session.add(new_review)
        db.session.commit()
        return '', 201


@review_ns.route('/<int:rid>')
class ReviewView(Resource):

    def get(self, rid):
        review = db.session.query(Review).get_or_404(rid)
        res = review.__dict__
        del res['_sa_instance_state']
        return res, 200

    def put(self, rid):
        review = db.session.query(Review).get_or_404(rid)
        data = request.json

        review.user = data.get('user')
        review.rating = data.get('rating')
        review.book_id = data.get('book_id')

        db.session.add(review)
        db.session.commit()
        return '', 204

    def delete(self, rid):
        review = db.session.query(Review).get_or_404(rid)

        db.session.delete(review)
        db.session.commit()
        return '', 204
