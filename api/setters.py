from flask_restful import Resource
from flask import request, make_response
from db.db import db, User, Books, Author
class ChangeUserName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        user = db.get_or_404(User,id)
        user.name = name
        db.session.commit()
        return make_response("Name name has been edited",200)
class ChangeBookName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        book = db.get_or_404(Books,id)
        book.name = name
        db.session.commit()
        return make_response("Book name has been edited",200)
class ChangeAuthorName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        author = db.get_or_404(author,id)
        author.name = name
        db.session.commit()
        return make_response("Author name has been edited",200)
