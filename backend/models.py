import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
                            
database_name = 'trivia'
database_path = 'postgresql://postgres:postgres@{}/{}'.format('localhost:5432', database_name)
db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
# def setup_db(app, database_path=database_path):    
def setup_db(app):     
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    print( " database_path " ,  database_path)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    print( " app.root_path below ")
    print( " app.root_path  ", app.root_path)
    # db = SQLAlchemy(app)
    db.app = app
    db.init_app(app)
    print("after db init")
    # db.create_all()
    # if app.app_context():        
    #     print("after db create_all")
    # # print("after db init" , db.create_all())

def return_db():  
    return db

"""
Question

"""
class Question(db.Model):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format_display(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
            }

"""
Category

"""
class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def format_display(self):
        return {
            'id': self.id,
            'type': self.type  
            }
    def format_display_id(self):
        return {
            'id': self.id,
            }
