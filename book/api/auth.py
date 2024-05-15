from flask_restful import Resource
from db.db import db, User, Author, Books, BLOB, Issue
from flask import make_response,request
from werkzeug.utils import secure_filename
import base64
from flask_wtf.file import FileField
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager
from flask_login import UserMixin,login_user,login_required,current_user,logout_user,LoginManager
from flask import redirect, url_for, flash
from time import sleep
from datetime import datetime, timedelta
import requests
class AuthUser(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password) and user.user_type=='User':
            login_user(user)
            flash("User has been authenticated, you are free to use this website.")
            sleep(2)
            return redirect(url_for('base.home_render'))
        else:
            flash("Credential are invalid, try again...")
            return redirect(url_for('login.return_user_login_page'))
class AuthAdmin(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password) and user.user_type=='Admin':
            login_user(user)
            flash("User has been authenticated, you are free to use this website.")
            sleep(2)
            return redirect(url_for('base.home_render'))
        else:
            flash("Credential are invalid, try again...")
            return redirect(url_for('login.return_admin_login_page'))
        
class RequestBook(Resource):
    def post(self):
        # try:
        assigned_to = current_user.email
        book_id = request.form["book_id"]
        issue_date = datetime.now()
        deadline = datetime.now() + timedelta(days=5)
        # issue_books = Issue.query.filter_by(assigned_to=assigned_to)
        # if book not in issue_books:
        # if len(issue_books) < 5:
        issue = Issue(book_id=book_id,assigned_to=assigned_to,issue_date=issue_date,deadline=deadline)
        db.session.add(issue)
        db.session.commit()
        flash("Request is successful, wait for approval.")
        return redirect(url_for("base.requestBook"))
            # else:
                # flash("Request is successful, wait for approval.")
                # return redirect(url_for("base.requestBook"))
        # except:
        #     flash("You've exceeded the capacity of books to download, Kindly remove some books.")
        # else:
        #     flash("You've exceeded the capacity of books to download, Kindly remove some books.")
        
        
        
class ApproveBook(Resource):
    def get(self):
        issues = Issue.query.all()
        issues_list = list()
        for issue in issues:
            book_name = requests.get("http://localhost:5000/getBookName?id="+str(issue.book_id)).json()
            username = requests.get("http://localhost:5000/getUserName?id="+str(issue.assigned_to)).json()
            issues_list.append({
                "book_id": issue.book_id,
                "book_name": book_name["name"],
                "user_id": issue.assigned_to,
                "username": username["name"],
                "status": issue.status
            })
        return {"requests": issues_list}
class ApproveBookById(Resource):
    def post(self):
        book_id = request.form["book_id"]
        user_id = request.form["user_id"]
        issue_books = Issue.query.filter_by(book_id=book_id,assigned_to=user_id).first()
        issue_books.status = "Approved"
        db.session.commit()
        flash("Book is Approved")
        return redirect(url_for("base.approveBook"))
class ReturnBook(Resource):
    def post(self):
        pass