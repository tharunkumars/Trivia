import os
import random

from flask import (
    Flask, 
    jsonify,
    app,
    abort,
    request,
    Response
)

from flask_cors import CORS, cross_origin

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    delete,
    select,
    and_
)

from models import setup_db, Question, Category , return_db

# QUESTIONS_PER_PAGE = 10

# app = Flask(__name__)

# def create_app(test_config=None):
#     print ( " inside create_app " )
#     # create and configure the app
#     # app = Flask(__name__)

#     print ( " inside create_app, after app creation " )
#     if test_config is None:
#         print ( " app name " , app.name)
#         setup_db(app)
#     else:
#         database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
#         setup_db(app, database_path=database_path)
#     CORS(app)
    
#     """
#     @TODO: Set up CORS. Allow '*' for origins. 
#     Delete the sample route after completing the TODOs
#     """

#     """@TODO: Use the after_request decorator to set Access-Control-Allow
#     """
#     @app.after_request
#     def after_request(response):
#         response.headers.add(
#             "Access-Control-Allow-Headers", "Content-Type, Authorization"
#         )
#         response.headers.add(
#             "Access-Control-Allow-Headers", "GET, POST, PATCH, DELETE, OPTION"
#         )
#         return response
#     return app


if __name__ == '__main__':
    print ( " inside main " )
    # create_app(None)
    # app.run(debug=True)