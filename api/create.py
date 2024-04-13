from flask_restful import Resource
from db.db import db, User, Author, Books
from flask import make_response,request
class CreateBook(Resource):
    def post(self):
        data = request.json
        new_book = Books(**data)
        db.session.add(new_book)
        db.session.commit()
        return make_response("Book has been created",200)
class CreateUser(Resource):
    def post(self):
        data = request.json
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return make_response("User has been created",200)
class CreateAuthor(Resource):
    def post(self):
        data = request.json
        new_author = Author(**data)
        db.session.add(new_author)
        db.session.commit()
        return make_response("Author has been created",200)