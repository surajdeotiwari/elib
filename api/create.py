from flask_restful import Resource
from db.db import db, User, Author, Books, BLOB
from flask import make_response,request,redirect,url_for,flash
from werkzeug.utils import secure_filename
import base64
from werkzeug.security import generate_password_hash 
import time
class CreateBook(Resource):
    def post(self):
        book_name = request.form["book_name"]
        author_id = request.form["author_id"]
        book_pdf = request.files["book_pdf"]
        publisher = request.form["publisher"]
        year = request.form["year"]
        topic = request.form["topic"]
        # photo = request.files["photo"]
        file =request.files["photo"]
        abstract = request.form["abstract"]
        # photo_filename = secure_filename(photo.filename)
        book_pdf_filename = secure_filename(book_pdf.filename)
        book_pdf_data = book_pdf.read()
        file_data = file.read()
        file_path = secure_filename(file.filename)
        mimetype = file.mimetype
        book = Books(
            book_name=book_name,
            author_id=author_id,
            book_pdf=book_pdf_data,
            book_mimetype=book_pdf.mimetype,
            publisher=publisher,
            year=year,
            topic=topic,
            photo=file.read(),
            file=file_path,
            mimetype=mimetype,
            abstract=abstract
        )
        db.session.add(book)
        db.session.commit()

        return flash("Book Created Successfully")

class CreateUser(Resource):
    def post(self):
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        user_type = request.form["user_type"]
        phone = request.form["phone"]
        photo = request.files["photo"]
        filename = secure_filename(photo.filename)
        mimetype = photo.mimetype
        photo_data = photo.read()
        user = User(
            name=name,
            email=email,
            password=password,
            user_type=user_type,
            phone=phone,
            photo=photo_data,
            file=filename,
            mimetype=mimetype
        )
        db.session.add(user)
        db.session.commit()
        if user_type == "Admin":
            flash("User Has Been Created, Now you are redirected to login page")
            time.sleep(5)
            return redirect(url_for('login.return_admin_login_page'))
        else:
            return redirect(url_for('login.return_user_login_page'))
class CreateAuthor(Resource):
    def post(self):
        name = request.form["name"]
        bio = request.form["bio"]
        file =request.files["photo"]
        file_path = secure_filename(file.filename)
        mimetype = file.mimetype
        author = Author(name=name,bio=bio,photo=file.read(),file=file_path,mimetype=mimetype)
        print(file)
        db.session.add(author)
        db.session.commit()
        return {"message": "Author created Successfully"}, 201
    
class RemoveAuthor(Resource):
    def post(self):
        author = Author.query.filter_by(id=id).first()
        db.session.delete(author)
        db.session.commit()
class RemoveBook(Resource):
    def post(self):
        book = Books.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit()

class RemoveUser(Resource):
    def post(self):
        user = User.query.filter_by(id=id).first()
        if user.user_type == 'User':
            db.session.delete(user)
            db.session.commit()