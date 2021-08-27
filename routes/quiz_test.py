"""users routes"""
from flask import current_app as app, jsonify, request
from models import QuizTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/quiz_test/<user_id>', methods=['POST', 'GET'])
def create_quiz_test(user_id):
    content = request.json
    quiz_test = QuizTest()
    quiz_test.userID      = str(content['userID'])
    quiz_test.date        = str(content['date'])
    quiz_test.startTime   = str(content['startTime'])
    quiz_test.sectionTime   = str(content['sectionTime'])
    quiz_test.trialTime   = str(content['trialTime'])
    quiz_test.taskSession   = str(content['taskSession'])
    quiz_test.taskSessionTry = str(content['taskSessionTry'])
    quiz_test.trialSection = str(content['trialSection'])
    quiz_test.trialNum = str(content['trialNum'])
    quiz_test.trialRT = str(content['trialRT'])
    quiz_test.trialKeypress = str(content['trialKeypress'])
    quiz_test.trialPicIndx = str(content['trialPicIndx'])
    quiz_test.trialPicWord = str(content['trialPicWord'])
    quiz_test.trialPicAns = str(content['trialPicAns'])
    quiz_test.trialPlanAns  = str(content['trialPlanAns'])
    quiz_test.trialPlanRT       = str(content['trialPlanRT'])
    quiz_test.trialPlanChoice       = str(content['trialPlanChoice'])
    quiz_test.trialPlanChoiceWords = str(content['trialPlanChoiceWords'])
    quiz_test.trialPlanPathChosen = str(content['trialPlanPathChosen'])
    quiz_test.trialCor  = str(content['trialCor'])
    quiz_test.trialScore  = str(content['trialScore'])

    BaseObject.check_and_save(quiz_test)
    result = dict({"success": "yes"})
    return jsonify(result)
