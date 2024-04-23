from flask import Flask
from routes.login import login_page
from routes.register import register_page
from routes.auth import auth
from routes.page import page
from routes.signup_template import signup_page
from db.db import db
from api.read import *
from api.update import *
from api.create import *
from api.delete import *
from api.read import *
from api.update import *
from api.auth import *
from flask_login import LoginManager
from flask import session
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv 
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 
# from api.setters import 
app = Flask(__name__) 
load_dotenv()
# API intialization
api = Api(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
# Database Initialization
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.secret_key = os.getenv("SECRET_KEY")
migrate = Migrate(app, db)

db.init_app(app)
with app.app_context():
    db.create_all()
# DB ends
login_manager = LoginManager()

# Registration of BluePrints
app.register_blueprint(login_page)
app.register_blueprint(register_page)
app.register_blueprint(auth)
app.register_blueprint(page)
app.register_blueprint(signup_page)
# Adding the api's
# Getters
api.add_resource(GetUserList, '/getUsers')
api.add_resource(GetBookList, '/getBooks')
api.add_resource(GetAuthorList, '/getAuthors')
api.add_resource(GetAuthorImage,'/getAuthorPhoto')
api.add_resource(GetAuthorNameById,'/getAuthorName')
api.add_resource(GetBooksOfAuthor, '/getBooksOfAuthor')
api.add_resource(GetIssuedBookByUser, '/getIssuedBooksByUser')
api.add_resource(GetNumberOfBookIssuedByUser, '/getNumberOfBooksIssuedByUser')
api.add_resource(GetParticularBookInformation, '/getParticularBookInformation')
api.add_resource(GetImagesOfUser, '/getImagesOfUser')
api.add_resource(GetImageOfBook, '/getImageOfBook')
api.add_resource(GetImageOfParticularBook, '/getImageOfParticularBook')
api.add_resource(GetStatisticsOfUser, '/getStatisticsOfUser')
api.add_resource(GetPdfOfBook, '/getPdfOfBook')
api.add_resource(GetBookByTopic, '/getBookByTopic')
api.add_resource(GetBookInformation, '/getBookInformation')
# Setters
api.add_resource(ChangePassword, '/changePassword')
api.add_resource(ChangeBookName, '/changeBookName')
api.add_resource(ChangeAuthorName, '/changeAuthorName')
# creators
api.add_resource(CreateBook, '/createBook')
api.add_resource(CreateUser, '/createUser')
api.add_resource(CreateAuthor, '/createAuthor')
# Deleters
api.add_resource(DeleteBook, '/deleteBook')
api.add_resource(DeleteUser, '/deleteUser')
api.add_resource(DeleteAuthor, '/deleteAuthor')
# Middlewares
api.add_resource(AuthUser, '/authUser')
api.add_resource(AuthAdmin, '/authAdmin')

if __name__ == '__main__':
    app.run(debug=True)