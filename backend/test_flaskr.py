import os
import unittest
import json

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

# from flaskr import create_app
# from flaskr.models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        # self.app = create_app({
        #     "SQLALCHEMY_DATABASE_URI": self.database_path
        # })

        # self.app = create_app()
        app = Flask(__name__)
        self.app = app
        # self.base_url = 'http://localhost:5000'
        # self.client = self.base_url
        self.client = self.app.test_client()
        # self.test_url_base = 'http://localhost:5000'

        database_name = 'trivia'
        database_path = 'postgresql://postgres:postgres@{}/{}'.format('localhost:5432', database_name)
        db = SQLAlchemy()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = database_path
        print( " database_path " ,  database_path)
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        print( " app.root_path  ", self.app.root_path)
        db.app = self.app
        db.init_app(self.app)
        CORS(self.app)
    
    def tearDown(self):
        """Executed after reach test"""
        print("Tear down method invoked after all tests ") 
        print("to destroy resources created for test")
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        """Test for get Categories """
        response = self.client.get('/categories')

        print (" Response " , response.status_code)

        print (" Response JSON" , response.get_json)

        self.assertEqual(response.status_code, 404)

        # data =  json.loads(response.data)
        # self.assertTrue(data['question'])
        

# Make the tests conveniently executable
if __name__ == "__main__":
    print ( " inside main " )
    unittest.main()
