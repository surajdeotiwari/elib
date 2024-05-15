from flask import Blueprint
from jinja2 import TemplateNotFound

search = Blueprint("search",__name__,template_folder="templates",url_prefix="/auth")

@search.route('admin')
def return_auth_response_admin_login():
    return "Response for admin"
@search.route('user')
def auth_response_user_login():
    return "Response for user"
