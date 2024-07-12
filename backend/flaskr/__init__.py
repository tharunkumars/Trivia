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
from flask_cors import CORS, cross_origin
from sqlalchemy import (
    delete,
    select,
    and_
)
import random

from models import setup_db, Question, Category , return_db

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
    CORS(app)
    
    """
    @TODO: Set up CORS. Allow '*' for origins. 
    Delete the sample route after completing the TODOs
    """

    """@TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Headers", "GET, POST, PATCH, DELETE, OPTION"
        )
        return response
    return app

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello, World! , Hello , God'
    #return jsonify({'message':'Hello, World!'})

"""@TODO:Create an endpoint to handle GET requests
for all available categories.
"""
@app.route('/categories', methods=['GET'])
@cross_origin()
def get_categories():
    print( " inside GET categories ")

    result_Categories = Category.query.all()
    list_Categories = [Category.format_display() for Category in result_Categories]
    no_of_Categories = len(list_Categories)

    print( "length of Categories " , no_of_Categories)
    print( "List  of Categories " , list_Categories)

    # for holder in list_Question:
    #     print( " value of holder ",holder)

    return jsonify({
        'success': True,
        'categories':list_Categories[0:no_of_Categories]
        })



"""# @TODO:Create an endpoint to handle GET requests for questions,
including pagination (every 10 questions).
This endpoint should return a list of questions,
number of total questions, current category, categories. 
"""
"""
TEST: At this point, when you start the application
you should see questions and categories generated,
ten questions per page and pagination at the bottom of the screen for three pages.
Clicking on the page numbers should update the questions.
"""
@app.route('/questions', methods=['GET'])
@cross_origin()
def get_Questions_Pagewise():
    print( " inside GET questions ")
    pageNum = request.args.get('page', 1, type=int)
    print( "pageNum " , pageNum)

    start = (pageNum - 1) * QUESTIONS_PER_PAGE
    end = start + 10

    result_Questions = Question.query.all()
    list_Question = [Question.format_display() for Question in result_Questions]
    no_of_Questions =len(list_Question)

    result_Categories = Category.query.all()
    list_Categories = [Category.format_display() for Category in result_Categories]
    no_of_Categories = len(list_Categories)

    print( "length of question " , no_of_Questions)
    print( "List  of question " , list_Question)
    print( "length of Categories " , no_of_Categories)
    print( "List  of Categories " , list_Categories)

    # for holder in list_Question:
    #     print( " value of holder ",holder)

    return jsonify({
        'success': True,
        'questions':list_Question[start:end],
        'total_questions':no_of_Questions,
        'categories':list_Categories[0:no_of_Categories]
        })
    #     return 'Hello, World! , Hello , God'


"""@TODO:Create an endpoint to POST a new question,
which will require the question and answer text,
category, and difficulty score.
"""
"""
TEST: When you submit a question on the "Add" tab,
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.
"""
@app.route('/questions', methods=['POST'])
@cross_origin()
def add_Questions():
    print( " inside ADD questions ")
    
    form_question = request.json.get('question')
    form_answer = request.json.get('answer')
    form_difficulty = request.json.get('difficulty')
    form_category = request.json.get('category')

    print( "  form_question " , form_question)
    print( "  form_answer " , form_answer)
    print( "  form_difficulty " , form_difficulty)
    print( "  form_category " , form_category)

    objQuestion = Question(form_question,form_answer,form_category,form_difficulty)

    db = return_db()
    db.session.add(objQuestion)  
    db.session.commit()

    return jsonify({
        'success': True,
        })
    #     return 'Hello, World! , Hello , God'









    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

""" @TODO: Create an endpoint to DELETE question using a question ID.

TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page.
"""
@app.route('/questions/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_Questions(id):
    print( " inside DELETE questions ")

    question_id = id
    
    db = return_db()
    query = delete(Question).filter_by(id=question_id)
    db.session.execute(query)
    db.session.commit()

    return jsonify({
        'success': True,
        })

""" @TODO: Create a POST endpoint to get questions based on a search term.
It should return any questions for whom the search term
is a substring of the question.

TEST: Search by any phrase. The questions list will update to include
only question that include that string within their question.
Try using the word "title" to start.
"""
@app.route('/questionsearch', methods=['POST'])
@cross_origin()
def get_Questions_SearchString():
    print( " inside SearchString Question ")

    val_searchTerm = request.json.get('searchTerm')

    db = return_db()
    formedquery = db.session.query(Question)
    questions_retrieved = formedquery.filter(Question.question.ilike("%"+val_searchTerm+"%")).all()
    list_Question = [Question.format_display() for Question in questions_retrieved]
    total_questions = len(list_Question)

    print( "No of questions " , total_questions)

    return jsonify({
        'success': True,
        'questions': list_Question[0:total_questions],
        'totalQuestions' : total_questions,
        'currentCategory' : 'Science'
        })    

""" @TODO: Create a GET endpoint to get questions based on category.
TEST: In the "List" tab / main screen, clicking on one of the
categories in the left column will cause only questions of that
category to be shown.
"""
@app.route('/categories/<int:id>/questions', methods=['GET'])
@cross_origin()
def get_Questions_forCategories(id):

    print( " inside get_Questions_forCategories ")
    print( " id from param" , id)

    category_id = id+1   
    print( " category_id " , category_id ) 

    db = return_db()
    formedquery_question = db.session.query(Question)
    questions_retrieved = formedquery_question.filter_by(category = category_id).all()

    print( "No of questions retrieved" , len(questions_retrieved))

    list_Question = [Question.format_display() for Question in questions_retrieved]
    total_questions = len(list_Question)
    print( "No of questions " , total_questions)

    category_retrieved = Category.query.filter_by(id = category_id).first()
    list_Category = [Category.format_display(category_retrieved)]

    total_Category = len(list_Category)    
    print( "No of Categories " , total_Category)

    return jsonify({
        'success': True,
        'questions': list_Question[0:total_questions],
        'totalQuestions' : total_questions,
        'currentCategory' : list_Category[0]
        })   

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
@app.route('/quizzes', methods=['POST'])
@cross_origin()
def get_Questions_Quiz():
    print( " inside QUIZ Question ")

    val_quizCategory = request.json.get('quiz_category')
    type_Category = val_quizCategory.get('type', '')
    id_Category = val_quizCategory.get('id', 0)
    print( "  type_Category " , type_Category)
    print( " id_Category " , id_Category)

    previousQuestions = request.json.get('previousQuestions')
    print( "  previousQuestions  " , previousQuestions)

    db = return_db()  

    if(id_Category == 0):
        list_Question = get_Quiz_AllQuestions(db)
    else:
        list_Question = get_Quiz_CategoryQuestions(db,id_Category)

    total_questions = len(list_Question) 
    random_int = random.randint(0, total_questions-1)
    print( " random_int " , random_int) 
    current_Question = list_Question[random_int]
  
    print( " current_Question " , current_Question ) 
    # if(previousQuestions == None):
    #     list_Question = get_Quiz_FirstQuestions(db,type_Category)  

    return jsonify({
        'success': True,
        'question': current_Question,
        'previousQuestions': previousQuestions
        })  

def get_Quiz_AllQuestions(db):
        # questions_query = select(Question)
        # questions_retrieved = db.session.execute(questions_query).all() 

        formedquery_question = db.session.query(Question)
        questions_retrieved = formedquery_question.all()

        list_Question = [Question.format_display() for Question in questions_retrieved]
        total_questions = len(list_Question)
        print( "No of questions " , total_questions)
        print( "List of questions " , list_Question)
        return list_Question

def get_Quiz_CategoryQuestions(db,id_Category):
        # questions_query = select(Question).where(Question.category == id_Category)
        # questions_retrieved = db.session.execute(questions_query).all()         

        formedquery = db.session.query(Question)
        questions_retrieved = formedquery.filter(Question.category == id_Category).all()
    
        print( "No of questions retrieved" , len(questions_retrieved))

        list_Question = [Question.format_display() for Question in questions_retrieved]
        total_questions = len(list_Question)
        print( "No of questions " , total_questions)
        print( "List of questions " , list_Question)
        return list_Question



if __name__ == '__main__':
    print ( " inside main " )
    create_app(None)
    app.run(debug=True)