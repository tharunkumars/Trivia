import os
from flask import Flask, request, abort, jsonify,app

from flask import (
    Flask, 
    jsonify,
    app,
    abort,
    request,
    Response
)

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

app = Flask(__name__)

def create_app(test_config=None):
    print ( " inside create_app " )
    # create and configure the app
    # app = Flask(__name__)

    print ( " inside create_app, after app creation " )
    if test_config is None:
        print ( " app name " , app.name)
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    return app
    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
@app.route('/')
def hello_world():
    return 'Hello, World! , Hello , God'
    #return jsonify({'message':'Hello, World!'})



    """
    # @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories. """

@app.route('/questions', methods=['GET'])
def get_Questions_Pagewise():
    print( " inside GET questions ")
    pageNum = request.args.get('page', 1, type=int)
    print( "pageNum " , pageNum)

    start = (pageNum - 1) * QUESTIONS_PER_PAGE
    end = start + 10

    result_Questions = Question.query.all()
    list_Question = [Question.format() for Question in result_Questions]

    print( "length of question " , len(list_Question))
    # for holder in list_Question:
    #     print( " value of holder ",holder)

    return jsonify({
        'success': True,
        'plants':list_Question[start:end],
        'total_plants':len(list_Question)
        })
    #     return 'Hello, World! , Hello , God'

    """
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

if __name__ == '__main__':
    print ( " inside main " )
    create_app(None)
    app.run(debug=True)