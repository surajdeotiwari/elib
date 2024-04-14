from flask import Blueprint,render_template
from jinja2 import TemplateNotFound

login_page = Blueprint('login',__name__,template_folder='templates',url_prefix='/login')
""" Admin login and User login page consist of Username, Password and Login Button"""
@login_page.route('/admin')
def return_admin_login_page():
    return render_template("adminLogin.html")
@login_page.route('/user')
def return_user_login_page():
    return render_template("userLogin.html")
@login_page.route('guest')
def return_guest_login_page():
    return render_template("guestLogin.html")