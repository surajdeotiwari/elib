from flask_restful import Resource
from db.db import db, User, Author, Books, BLOB
from flask import make_response,request
from werkzeug.utils import secure_filename
import base64
from flask_wtf.file import FileField
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager
login_manager = LoginManager()

class AuthUser(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password) and user.user_type=='User':
            return {"message": True, "user": user.name}
        else:
            return {"message": "False"}, 400
class AuthAdmin(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password) and user.user_type=='Admin':
            return {"message": True, "user": user.name}, 200
        else:
            return {"message": False}, 400
