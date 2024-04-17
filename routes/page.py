from flask import Blueprint,render_template,request,Response
from jinja2 import TemplateNotFound
import requests
from flask_login import login_required

page = Blueprint("base",__name__,template_folder="templates",url_prefix="/")

@page.route('/')
def home_render():
    return render_template("base.html",title="Elib - Home")
@page.route('/books')
# @login_required
def book_render():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getBooks'
    response = requests.get(url)
    return render_template("books.html", title="Elib - Books", books=response.json())
@page.route('/authors')

def author_render():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getAuthors'
    response = requests.get(url)
    return render_template("authors.html", title="Elib - Authors",authors=response.json())
@page.route('/search')
def search_render():
    return render_template("search.html", title="Elib - Search")
@page.route('/policy')
def policy():
    return render_template("policy.html", title="Elib - Policy")
@page.route('/test', methods=['GET','POST'])
def exit():
    return render_template("uploads.html")