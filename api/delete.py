from flask_restful import Resource
from db.db import db, User, Author, Books
from flask import make_response,request
class DeleteBook(Resource):
    def post(self):
        book_id = request.form["id"]
        book = db.get_or_404(Books,book_id)
        db.session.delete(book)
        db.session.commit()
        return make_response("Book has been deleted",200)
class DeleteUser(Resource):
    def post(self):
        user_name = request.form["username"]
        user = db.get_or_404(User,user_name)
        db.session.delete(user)
        db.session.commit()
        return make_response("User has been deleted",200)
class DeleteAuthor(Resource):
    def post(self):
        author_id = request.form["id"]
        author = db.get_or_404(Author,author_id)
        db.session.delete(author)
        db.session.commit()
        return make_response("Success",200)
