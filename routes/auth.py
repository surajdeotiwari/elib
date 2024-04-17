from flask import Blueprint
from jinja2 import TemplateNotFound
from werkzeug.security import check_password_hash
auth = Blueprint("authenticate",__name__,template_folder="templates",url_prefix="/auth")

@auth.route('admin')
def return_auth_response_admin_login():
    return "Response for admin"
@auth.route('user')
def auth_response_user_login():
    return "Response for user"
