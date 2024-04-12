from flask_restful import Resource

class ChangeUserName(Resource):
    def get(self):
        return "this returns changed user name of a user"
class ChangeBookName(Resource):
    def get(self):
        return "changes the book name"
class ChangeAuthorName(Resource):
    def get(self):
        return "changes the author name"
