from flask_restful import Resource
class DeleteBook(Resource):
    def get(self):
        return "deletes the book"
class DeleteUser(Resource):
    def get(self):
        return "deletes the user"
class DeleteAuthor(Resource):
    def get(self):
        return "deletes the author"
    