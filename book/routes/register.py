from flask import Blueprint
from jinja2 import TemplateNotFound

register_page = Blueprint('register',__name__,template_folder='templates',url_prefix='/register')
""" Admin Registration Page and User Registration page are separate"""
@register_page.route('/admin')
def return_admin_registration_page():
    return "This is admin registration page"
@register_page.route('/user')
def return_user_registration_page():
    return "This is user registration page"