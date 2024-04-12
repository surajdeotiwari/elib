from flask import Blueprint
from jinja2 import TemplateNotFound

login_page = Blueprint('login',__name__,template_folder='templates',url_prefix='/login')
""" Admin login and User login page consist of Username, Password and Login Button"""
@login_page.route('/admin')
def return_admin_login_page():
    return "This is admin login page"
@login_page.route('/user')
def return_user_login_page():
    return "This is user login page"
@login_page.route('guest')
def return_guest_login_page():
    return "This is guest page"