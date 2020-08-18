"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuestionsBehaviour, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/tutorial_quiz/<user_id>', methods=['POST', 'GET'])

def create_tutorial_quiz(user_id):

    content                          = request.json
    tutorial_quiz                    = TutorialQuiz()

    tutorial_quiz.userID             = int(user_id)
    tutorial_quiz.quizTime          = str(content['quizTime'])
    tutorial_quiz.tutorialSession    = str(content['tutorialSession'])
    tutorial_quiz.tutorialSessionTry = str(content['tutorialSessionTry'])
    tutorial_quiz.quizSession        = str(content['quizSession'])
    tutorial_quiz.quizQnNum          = str(content['quizQnNum'])
    tutorial_quiz.quizKeypress       = str(content['quizKeypress'])
    tutorial_quiz.quizQnRT           = str(content['quizQnRT'])
    tutorial_quiz.quizKeypress       = str(content['quizKeypress'])
    tutorial_quiz.quizQnRT           = str(content['quizQnRT'])
    tutorial_quiz.quizScoreCor       = str(content['quizScoreCor'])

    BaseObject.check_and_save(tutorial_quiz)

    result = dict({"success": "yes"})

    return jsonify(result)
