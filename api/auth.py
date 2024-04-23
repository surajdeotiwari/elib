from flask_restful import Resource
from db.db import db, User, Author, Books, BLOB
from flask import make_response,request
from werkzeug.utils import secure_filename
import base64
from flask_wtf.file import FileField
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager
from flask_login import UserMixin,login_user,login_required,current_user,logout_user,LoginManager
from flask import redirect, url_for
class AuthUser(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password) and user.user_type=='User':
            login_user(user)
            return redirect(url_for('base.home_render'))
        elif user and check_password_hash(user.password, password) and user.user_type=='Admin':
            login_user(user)
            return redirect(url_for('base.home_render'))
        else:
            return {"message": "False"}, 400
class AuthAdmin(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password) and user.user_type=='Admin':
            return redirect(url_for('base.home_render'))
        else:
            return {"message": False}, 400
