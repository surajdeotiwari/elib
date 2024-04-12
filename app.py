from flask import Flask
from routes.login import login_page
from routes.register import register_page
from routes.auth import auth
from db.db import db
from api.getters import *
from api.setters import *
from api.deleters import *
from api.updaters import *
# from api.setters import 
from flask_restful import Api
app = Flask(__name__) 
# API intialization
api = Api(app)
# Database Initialization
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)
with app.app_context():
    db.create_all()
# DB ends
# Registration of BluePrints
app.register_blueprint(login_page)
app.register_blueprint(register_page)
app.register_blueprint(auth)
# Adding the api's
# Getters
api.add_resource(GetUserList, '/getUsers')
api.add_resource(GetBookList, '/getBooks')
api.add_resource(GetAuthorList, '/getAuthors')
api.add_resource(GetBooksOfAuthor, '/getBooksByAuthor')
api.add_resource(GetIssuedBookByUser, '/getIssuedBooksByUser')
api.add_resource(GetNumberOfBookIssuedByUser, '/getTotalIssuedBooksByUser')
api.add_resource(GetAllIssuedBookByUser, '/getAllIssuedBooksByUser')
api.add_resource(GetImagesOfUser, '/getUserImage')
api.add_resource(GetImageOfBook, '/getBookImage')
api.add_resource(GetStatisticsOfUser, '/getUserStatistics')
api.add_resource(GetPdfOfBook, '/getBookPdf')
api.add_resource(GetBookByTopic,'/getBookTopic')
api.add_resource(GetBookInformation,'/getBookInfo')
# Setters
api.add_resource(ChangeUserName, '/changeUserName')
api.add_resource(ChangeBookName, '/changeBookName')
api.add_resource(ChangeAuthorName, '/changeAuthorName')
# Updaters
api.add_resource(UpdateBook, '/updateBook')
api.add_resource(UpdateUser, '/updateUser')
api.add_resource(UpdateAuthor, '/updateAuthor')
# Deleters
api.add_resource(DeleteBook, '/deleteBook')
api.add_resource(DeleteUser, '/deleteUser')
api.add_resource(DeleteAuthor, '/deleteAuthor')
if __name__ == '__main__':
    app.run(debug=True)