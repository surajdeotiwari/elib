from flask_restful import Resource

class UpdateBook(Resource):
    def get(self):
        return "this will update the book name, author, year, etc"
class UpdateUser(Resource):
    def get(self):
        return "this will update the user record"
class UpdateAuthor(Resource):
    def get(self):
        return "this will update the Author record"
