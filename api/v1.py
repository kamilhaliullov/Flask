
from api.books_api import *


def init(app, auth):
    api = Api(app)
    api.add_resource(BooksListApi, '/api/v1/books', resource_class_args=[auth])
    api.add_resource(BooksApi, '/api/v1/books/<int:id>', resource_class_args=[auth])
