from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import jsonify
from flask import abort
import extra.auth as auth
from models import Books

books_parser = reqparse.RequestParser()
books_parser.add_argument('title', required=True)
books_parser.add_argument('content', required=True)


class BooksListApi(Resource):
    def __init__(self, auth):
        super(BooksListApi, self).__init__()
        self._auth = auth

    def get(self):
        books = Books.query.all()
        return jsonify(books=[i.serialize for i in books])

    def post(self):
        if not self._auth.is_authorized():
            abort(401)
        args = books_parser.parse_args()
        books = Books.add(args['title'], args['content'], self._auth.get_user())
        return jsonify(books.serialize)


class BooksApi(Resource):

    def __init__(self, auth):
        super(BooksApi, self).__init__()
        self._auth = auth

    def get(self, id):
        books = Books.query.filter_by(id=id).first()
        if not books:
            abort(404)
        return jsonify(books.serialize)

    def delete(self, id):
        if not self._auth.is_authorized():
            abort(401)
        books = Books.query.filter_by(id=id).first()
        if books.user_id != self._auth.get_user().id:
            abort(403)
        Books.delete(books)
        return jsonify({"deleted": True})
