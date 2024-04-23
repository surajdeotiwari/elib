from flask_restful import Resource
from flask import request, make_response
from db.db import db, User, Books, Author
from werkzeug.security import generate_password_hash
from flask import flash
class ChangePassword(Resource):
    def post(self):
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        user = User.query.filter_by(email=email)
        user.password = password
        db.session.commit()
        return flash("Password has been change")
class ChangeBookName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        book_pdf = request.files["book_pdf"]
        book = Books.query.filter_by(id=id).first()
        book.book_name = name
        book.book_pdf = book_pdf
        db.session.commit()
        return flash("Book name has been edited")
class ChangeAuthorName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        bio = request.form['bio']
        file =request.files["photo"]
        author = Author.query.filter_by(id=id).first()
        author.name = name
        author.bio = bio
        author.photo = file.read()
        db.session.commit()
        return flash("Author name has been edited")
