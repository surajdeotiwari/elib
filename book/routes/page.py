from flask import Blueprint,render_template,request,Response,flash,redirect,url_for
from jinja2 import TemplateNotFound
import requests
from flask_login import login_required, logout_user, current_user
from db.db import Books,Author,Issue
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
    # ap_book = f'{scheme}://{host}/approvebook'
    # ap_book = requests.get(url).json()
    
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
@login_required
def dashboard():
    books = Books.query.all()
    authors = Author.query.all()
    query = Issue.query.filter_by   (status="Approved")
    lst = []
    for q in query:
        lst.append({
            "assigned_to": q.assigned_to,
            "id": q.book_id
            })
    return render_template("dashboard.html", title="Elib - Book Upload", books=len(books),authors=len(authors),lst=lst)
@page.route('/book_uploads', methods=['GET','POST'])
@login_required
def book_uploads():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getAuthors'
    response = requests.get(url)
    section_url = f'{scheme}://{host}/getSections'
    section = requests.get(section_url)
    return render_template("upload_book.html", title="Elib - Book Upload", authors=response.json(), sections=section.json())
@page.route('/add_author', methods=['GET','POST'])
@login_required
def author_uploads():
    return render_template("upload_authors.html", title="Elib - Add Author")
@page.route('/changepassword', methods=['GET','POST'])
@login_required
def changePassword():
    return render_template("changePassword.html", title="Elib - Change Password")
@page.route('editBook', methods=['GET','POST'])
@login_required
def editBook():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getBooks'
    response = requests.get(url)
    author_url = f'{scheme}://{host}/getAuthors'
    authors = requests.get(author_url)
    section_url = f'{scheme}://{host}/getSections'
    section = requests.get(section_url)
    return render_template("editBook.html", title="Elib - Edit Book",books=response.json(),authors=authors.json(),sections=section.json())
@page.route('addsection', methods=['GET','POST'])
@login_required
def addSection():
    return render_template("section.html", title="Elib - Add Section")
@page.route('bookDelete', methods=['GET','POST'])
@login_required
def deleteBook():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getBooks'
    response = requests.get(url)
    return render_template("deleteBook.html", title="Elib - Delete Book", books=response.json())

# getAuthors
@page.route('authorDelete', methods=['GET','POST'])
@login_required
def deleteAuthor():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getAuthors'
    response = requests.get(url)
    return render_template("deleteAuthor.html", title="Elib - Delete Author", authors=response.json())

@page.route('sectionDelete', methods=['GET','POST'])
@login_required
def deleteSection():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getSections'
    response = requests.get(url)
    return render_template("deleteSection.html", title="Elib - Delete Section", sections=response.json())

@page.route('editAuthor', methods=['GET','POST'])
@login_required
def editAuthor():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getAuthors'
    response = requests.get(url)
    return render_template("editAuthor.html", title="Elib - Edit Author", authors=response.json())

@page.route('requestBook', methods=['GET','POST'])
@login_required
def requestBook():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/getBooks'
    response = requests.get(url)
    return render_template("reqBook.html", title="Elib - Request Book", books=response.json())

@page.route('approveBook', methods=['GET','POST'])
@login_required
def approveBook():
    scheme = request.scheme
    host = request.host
    url = f'{scheme}://{host}/approvebook'
    response = requests.get(url).json()
    return render_template("approveBook.html",title="Elib - Approve Book", reqs = response["requests"])
@page.route('userdashboard', methods=['GET','POST'])
@login_required
def userdashboard():
    lst = list()
    if current_user.is_authenticated:
        user_id = current_user.email
        print(user_id)
        issues = Issue.query.filter_by(assigned_to=user_id, status="Approved")
        for issue in issues:
            book = Books.query.filter_by(id=issue.book_id).first()
            lst.append({
                "id": book.id,
                "name": book.book_name,
                "topic": book.topic,
                "publisher": book.publisher,
                "year":book.year,
                "url":"http://localhost:5000/getPdfOfBook?id="+str(book.id)
            })
    print(lst)
    return render_template("userDash.html",title="Elib - Approve Book", books = lst)

@page.route('logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("Logout Successully")
    return redirect(url_for('login.return_user_login_page'))




