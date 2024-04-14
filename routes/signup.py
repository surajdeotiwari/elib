from flask import Blueprint,render_template
from jinja2 import TemplateNotFound

signup_page = Blueprint('signup',__name__,template_folder='templates',url_prefix='/signup')
""" Admin login and User login page consist of Username, Password and Login Button"""
@signup_page.route('/admin')
def return_admin_login_page():
    return render_template("adminSignup.html")
@signup_page.route('/user')
def return_user_login_page():
    return render_template("userSignup.html")