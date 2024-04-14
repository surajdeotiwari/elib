from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id = Column(Integer, primary_key=True)
    photo = Column(String, nullable=False)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    type = Column(String, nullable=False)
    phone = Column(Integer, unique=True)
    fine = Column(Float, nullable=False)

class Books(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    book_id = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    assigned = Column(Integer,ForeignKey(User.id),nullable=False)
    publish_date = Column(DateTime, nullable=False)
    photo = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    reservation = Column(Boolean, nullable=False)
    issue_date = Column(DateTime, nullable=False)
    deadline = Column(DateTime, nullable=False)
    topic = Column(String, nullable=False)
    bio = Column(String, nullable=False)

class Author(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    author_id = Column(String, nullable=False, unique=True)
    photo_path = Column(String, nullable=False)

class Logs(db.Model):
    serial = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    login_time = Column(DateTime)
    username = Column(String)
    logout_time = Column(DateTime)
