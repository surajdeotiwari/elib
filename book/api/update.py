from flask_restful import Resource
from flask import request, make_response
from db.db import db, User, Books, Author
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from flask import flash,redirect, url_for
from flask_login import current_user
class ChangePassword(Resource):
    def post(self):
        email = current_user.email
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, old_password):
            flash("Password has been changed successfully")
            user.password = generate_password_hash(new_password)
            db.session.commit()
            return redirect(url_for('base.changePassword'))
        else:
            flash("Entered password is incorrect. Please enter the correct password.")
            return redirect(url_for('base.changePassword'))
class ChangeBookName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        book_pdf = request.files["book_pdf"]
        author_id = request.form["author_id"]
        publisher = request.form["publisher"]
        year = request.form["year"]
        topic = request.form["topic"]
        photo = request.files["photo"]
        abstract = request.form["abstract"]
        book = Books.query.filter_by(id=id).first()
        book.book_name = name
        book.book_pdf = book_pdf.read()
        book.author_id = author_id
        book.publisher = publisher
        book.year = year
        book.topic = topic
        book.photo = photo.read()
        book.abstract = abstract
        db.session.commit()
        flash("Book details are updated successfully")
        return redirect(url_for('base.editBook'))
class ChangeAuthorName(Resource):
    def post(self):
        id = request.form['id']
        name = request.form['name']
        bio = request.form['bio']
        file =request.files["photo"]
        file_path = secure_filename(file.filename)
        mimetype = file.mimetype
        author = Author.query.filter_by(id=id).first()
        author.name = name
        author.bio = bio
        author.photo = file.read()
        author.file = file_path
        author.mimetype = mimetype
        db.session.commit()
        flash("Author name has been edited")
        return redirect(url_for('base.editAuthor'))