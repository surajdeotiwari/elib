from flask_restful import Resource
class GetUserList(Resource):
    def get(self):
        return "this returns the user records."
class GetBookList(Resource):
    def get(self):
        return "this returns all the books records"
class GetAuthorList(Resource):
    def get(self):
        return "this returns all the authors lists"
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