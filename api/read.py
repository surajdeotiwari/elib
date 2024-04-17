from flask_restful import Resource
from db.db import User, Books, Author
from flask import request,Response,jsonify
import requests

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
            author = Author.query.filter_by(id=book.author_id).first()
            book_list.append({
                "id": book.id,
                "name": book.book_name,
                "topic": book.topic,
                "publisher": book.publisher,
                "author": author.name,
                "year":book.year,
                "url":"http://127.0.0.1:5000/getPdfOfBook?id="+str(book.id)
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
                "name": author.name,
                "bio":author.bio
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
                "name": book.name,
                
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

class GetAuthorImage(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            if not id:
                return {"error": "Author ID is missing"}, 400

            author = Author.query.filter_by(id=id).first()
            if not author:
                return {"error": "Author not found"}, 404

            return Response(author.photo, mimetype=author.mimetype)
        except Exception as e:
            return {"error": str(e)}, 500
class GetAuthorNameById(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            if not id:
                return {"error": "Author ID is missing"}, 400

            author = Author.query.filter_by(id=id).first()
            if not author:
                return {"error": "Author not found"}, 404

            return {"name":author.name}
        except Exception as e:
            return {"error": str(e)}, 500

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
        try:
            id = request.args['id']
            book = Books.query.filter_by(id=id).all()[0]
            book_pdfs = book.book_pdf
            return Response(book_pdfs,mimetype=book.book_mimetype)
        except:
            return "there has been an error"
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