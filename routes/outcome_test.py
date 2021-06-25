"""users routes"""
from flask import current_app as app, jsonify, request
from models import OutcomeTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/outcome_test/<user_id>', methods=['POST', 'GET'])
def create_outcome_test(user_id):
    content = request.json
    outcome_test = OutcomeTest()
    outcome_test.userID = str(content['userID'])
    outcome_test.date        = str(content['date'])
    outcome_test.startTime   = str(content['startTime'])
    outcome_test.sectionTime   = str(content['sectionTime'])
    outcome_test.taskSession = str(content['taskSession'])
    outcome_test.taskSessionTry = str(content['taskSessionTry'])
    outcome_test.trialTime = str(content['trialTime'])
    outcome_test.trialNum = str(content['trialNum'])
    outcome_test.trialPicIndx = str(content['trialPicIndx'])
    outcome_test.trialPicWord = str(content['trialPicWord'])
    outcome_test.trialPicNum = str(content['trialPicNum'])
    outcome_test.trialPicValue = str(content['trialPicValue'])
    outcome_test.trialPicAns = str(content['trialPicAns'])
    outcome_test.trialRT = str(content['trialRT'])
    outcome_test.trialKeypress = str(content['trialKeypress'])
    outcome_test.trialCor = str(content['trialCor'])
    outcome_test.trialScore = str(content['trialScore'])
    BaseObject.check_and_save(outcome_test)
    result = dict({"success": "yes"})
    return jsonify(result)
