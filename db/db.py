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

class Issue(db.Model):
    __tablename__ = 'issues'

    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    book = relationship("Books")
    assigned_to = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    issue_date = Column(Date)
    return_date = Column(Date)
    deadline = Column(Date)
