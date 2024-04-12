from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id = Column(Integer, primary_key=True)
    photo_path = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    type = Column(String)
    branch = Column(String)
    phone = Column(Integer, unique=True)
    fine = Column(Float)

class Books(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    publisher = Column(String)
    publish_date = Column(DateTime)
    file_path = Column(String)
    reservation = Column(Boolean)
    issue_date = Column(DateTime)
    deadline = Column(DateTime)

class Author(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bio = Column(String)
    photo_path = Column(String)

class Logs(db.Model):
    serial = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    login_time = Column(DateTime)
    username = Column(String)
    logout_time = Column(DateTime)
