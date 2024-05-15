from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, BLOB, LargeBinary, Date
from sqlalchemy.orm import DeclarativeBase,relationship
from flask_login import UserMixin
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    user_type = Column(String)
    phone = Column(Integer)
    photo = Column(LargeBinary)
    file = Column(String)
    mimetype = Column(String)
    is_active = Column(db.Boolean, default=True)
    is_authenticated = Column(db.Boolean, default=True)
    def is_active(self):
        return self.is_active
    def get_id(self):
        return self.id
    def is_authenticated(self):
        return self.is_authenticated
class Author(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    bio = Column(String)
    photo = Column(LargeBinary)
    file = Column(String)
    mimetype = Column(String)

class Books(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author")
    book_pdf = Column(LargeBinary)
    book_mimetype = Column(String)
    publisher = Column(String)
    year = Column(String)
    topic = Column(String)
    photo = Column(LargeBinary)
    file = Column(String)
    mimetype = Column(String)
    abstract = Column(String)

class Section(db.Model):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    section_name = Column(String)
    description = Column(String)

class Reasons_For_Delete(db.Model):
    __tablename__ = 'reasons'
    id = Column(Integer, primary_key=True)
    operated_on = Column(String)
    operation = Column(String)
    description = Column(String)
class Issue(db.Model):
    __tablename__ = 'issues'
    reqid = Column(Integer, primary_key=True,autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Books")
    assigned_to = Column(String, ForeignKey('users.email'))
    user = relationship("User")
    issue_date = Column(Date)
    deadline = Column(Date)
    status = Column(String, default="Not Approved")
