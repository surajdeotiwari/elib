from flask import Blueprint,render_template,request,Response,redirect,url_for
from jinja2 import TemplateNotFound
import requests
from flask_login import login_required, logout_user
from db.db import Books,Author
page = Blueprint("base",__name__,template_folder="templates",url_prefix="/")
@page.route('/')
def home_render():
    return render_template("base.html",title="Elib - Home")
@page.route('/books')

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
@page.route('/search', methods=['GET', 'POST'])
def search_render():
    search = request.form["query"]
    books = Books.query.filter(Books.book_name.ilike(f"%{search}%")).all()
    authors = Author.query.filter(Author.name.ilike(f"%{search}%")).all()
    return render_template("result.html", title="Elib - Search",books=books,authors=authors)
@page.route('/dashboard', methods=['GET','POST'])
def dashboard():
    books = Books.query.all()
    authors = Author.query.all()
    return render_template("dashboard.html", title="Elib - Book Upload", books=len(books),authors=len(authors))
@page.route('/book_uploads', methods=['GET','POST'])
def book_uploads():
    return render_template("upload_book.html", title="Elib - Book Upload")
@page.route('/add_author', methods=['GET','POST'])
def author_uploads():
    return render_template("upload_authors.html", title="Elib - Add Author")
@page.route('/changePassword', methods=['GET','POST'])
def changePassword():
    return render_template("changePassword.html", title="Elib - Change Password")
@page.route('editBook', methods=['GET','POST'])
def editBook():
    return render_template("editBook.html", title="Elib - Edit Book")
@page.route('logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login.return_user_login_page'))




