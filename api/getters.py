from flask_restful import Resource
from db.db import User,Books,Author
class GetUserList(Resource):
    # API endpoint /getUsers
    def get(self):
        users = User.query.all()
        user_list = list()
        for user in users:
            user_list.append({
                user.id,
                user.name
            })
        return {"users":user_list}
class GetBookList(Resource):
    # API endpoint /getBooks
    def get(self):
        books = Books.query().all()
        book_list = list()
        for book in books:
            book_list.append({
                book.id,
                book.name
            })
        return {"users":book_list}
class GetAuthorList(Resource):
    def get(self):
        authors = Author.query().all()
        author_list = list()
        for author in authors:
            author_list.append({
                author.id,
                author.name
            })
        return {"authors":author_list}
class GetBooksOfAuthor(Resource):
    def get(self):
        return "this returns specific author books"
class GetIssuedBookByUser(Resource):
    def get(self):
        return "this returns books issued by an user"
class GetNumberOfBookIssuedByUser(Resource):
    def get(self):
        return "this returns number of books issued by user"
class GetAllIssuedBookByUser(Resource):
    def get(self):
        return "this returns all issued books by users"
class GetImagesOfUser(Resource):
    def get(self):
        return "this returns image of user"
class GetImageOfBook(Resource):
    def get(self):
        return "This returns image of book by id"
class GetStatisticsOfUser(Resource):
    def get(self):
        return "this returns all information about user reading pattern such as most referred books, authors, subjects, etc"
class GetPdfOfBook(Resource):
    def get(self):
        return "this returns the pdf of book asked through id"
class GetBookByTopic(Resource):
    def get(self):
        return "this returns book of particular topic"
class GetBookInformation(Resource):
    def get(self):
        return "this returns the particular book information"