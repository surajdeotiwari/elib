from flask_restful import Resource
from db.db import User, Books, Author
from flask import request

class GetUserList(Resource):
    # API endpoint /getUsers
    def get(self):
        users = User.query.all()
        user_list = list()
        for user in users:
            user_list.append({
                "id": user.id,
                "name": user.name
            })
        return {"users": user_list}

class GetBookList(Resource):
    # API endpoint /getBooks
    def get(self):
        books = Books.query.all()
        book_list = list()
        for book in books:
            book_list.append({
                "id": book.id,
                "name": book.name
            })
        return {"books": book_list}

class GetAuthorList(Resource):
    # API endpoint /getAuthors
    def get(self):
        authors = Author.query.all()
        author_list = list()
        for author in authors:
            author_list.append({
                "id": author.id,
                "name": author.name
            })
        return {"authors": author_list}

class GetBooksOfAuthor(Resource):
    # API endpoint /getBooksOfAuthor
    def get(self):
        name = request.args['id']
        books = Books.query.filter_by(author=name).all()
        book_list = list()
        for book in books:
            book_list.append({
                "id": book.id,
                "name": book.name
            })
        return {"books": book_list}

class GetIssuedBookByUser(Resource):
    # API endpoint /getIssuedBooksByUser
    def get(self):
        ids = request.args['id']
        books = Books.query.filter_by(assigned=ids).all()
        book_list = list()
        for book in books:
            book_list.append({
                "id": book.id,
                "name": book.name
            })
        return {"books": book_list}

class GetNumberOfBookIssuedByUser(Resource):
    # API endpoint /getNumberOfBooksIssuedByUser
    def get(self):
        ids = request.args['id']
        books = Books.query.filter_by(assigned=ids).all()
        return {"number of books issued": len(books)}

class GetParticularBookInformation(Resource):
    # API endpoint /getParticularBookInformation
    def get(self):
        ids = request.args['id']
        books = Books.query.filter_by(id=ids).all()
        book_info = list()
        for book in books:
            book_info.append({
                "id": book.id,
                "name": book.name,
                "bio": book.bio
            })
        return {"books": book_info}

class GetImagesOfUser(Resource):
    # API endpoint /getImagesOfUser
    def get(self):
        uname = request.args['username']
        pics = Author.query.filter_by(username=uname).all()
        picture_list = list()
        for picture in pics:
            picture_list.append(picture.photo)
        return {uname: picture_list[0]}

class GetImageOfBook(Resource):
    # API endpoint /getImageOfBook
    def get(self):
        pics = Books.query.all()
        picture_list = list()
        for picture in pics:
            picture_list.append(picture.photo)
        return {"Books": picture_list}

class GetImageOfParticularBook(Resource):
    # API endpoint /getImageOfParticularBook
    def get(self):
        name = request.args['bname']
        pics = Books.query.filter_by(name=name).all()
        picture_list = list()
        for picture in pics:
            picture_list.append(picture.photo)
        return {"Books": picture_list[0]}

class GetStatisticsOfUser(Resource):
    # API endpoint /getStatisticsOfUser
    def get(self):
        return "this returns all information about user reading pattern such as most referred books, authors, subjects, etc"

class GetPdfOfBook(Resource):
    # API endpoint /getPdfOfBook
    def get(self):
        name = request.args['bname']
        book = Books.query.filter_by(name=name).all()
        book_pdfs = list()
        for pdfs in book:
            book_pdfs.append(pdfs.pdf)
        return {"Books": book_pdfs}

class GetBookByTopic(Resource):
    # API endpoint /getBookByTopic
    def get(self):
        topic = request.args['topic']
        books = Books.query.filter_by(topic=topic).all()
        book_name = list()
        for book in books:
            book_name.append(book.name)
        return {"Names": book_name}

class GetBookInformation(Resource):
    # API endpoint /getBookInformation
    def get(self):
        name = request.args['bname']
        books = Books.query.filter_by(name=name).all()
        book_info = list()
        for book in books:
            book_info.append(book.bio)
        return {"Information": book_info}
