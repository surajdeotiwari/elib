from flask import Blueprint,render_template
from jinja2 import TemplateNotFound

home = Blueprint("home",__name__,template_folder="templates",url_prefix="/")

@home.route('home')
def home_render():
    return render_template("base.html")