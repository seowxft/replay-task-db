"""users routes"""
from flask import current_app as app, jsonify, request
from models import CondData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/cond_data/<user_id>', methods=['POST', 'GET'])
def create_cond_data(user_id):
    content = request.json
    cond_data = CondData()
    cond_data.userID      = str(content['userID'])
    cond_data.date        = str(content['date'])
    cond_data.startTime   = str(content['startTime'])
    cond_data.sectionTime   = str(content['sectionTime'])
    cond_data.trialTime   = str(content['trialTime'])
    cond_data.taskSession   = str(content['taskSession'])
    cond_data.taskSessionTry = str(content['taskSessionTry'])
    cond_data.structNum = str(content['structNum'])
    cond_data.outcomeWord = str(content['outcomeWord'])
    cond_data.outcomeVal = str(content['outcomeVal'])
    cond_data.outcomeIndx = str(content['outcomeIndx'])
    cond_data.stateWord   = str(content['stateWord'])
    cond_data.stateIndx = str(content['stateIndx'])
    cond_data.pathOne = str(content['pathOne'])
    cond_data.pathTwo = str(content['pathTwo'])
    cond_data.pathThree = str(content['pathThree'])
    cond_data.tutForcedPaths = str(content['tutForcedPaths'])
    cond_data.tutSafePathOutcome = str(content['tutSafePathOutcome'])
    cond_data.tutRiskyPathOutcome1 = str(content['tutRiskyPathOutcome1'])
    cond_data.tutRiskyPathOutcome2   = str(content['tutRiskyPathOutcome2'])
    cond_data.tutSafePathProb = str(content['tutSafePathProb'])
    cond_data.tutRiskyPathProb1 = str(content['tutRiskyPathProb1'])
    cond_data.tutRiskyPathProb2 = str(content['tutRiskyPathProb2'])
    cond_data.tutOptChoice = str(content['tutOptChoice'])
    cond_data.tutForceChoice = str(content['tutForceChoice'])
    cond_data.tutPlanChoice = str(content['tutPlanChoice'])
    cond_data.tutOutcomeStruct = str(content['tutOutcomeStruct'])
    cond_data.tutShowPath = str(content['tutShowPath'])
    cond_data.taskSafePathOutcome = str(content['taskSafePathOutcome'])
    cond_data.taskRiskyPathOutcome1 = str(content['taskRiskyPathOutcome1'])
    cond_data.taskRiskyPathOutcome2   = str(content['taskRiskyPathOutcome2'])
    cond_data.taskSafePathProb = str(content['taskSafePathProb'])
    cond_data.taskRiskyPathProb1 = str(content['taskRiskyPathProb1'])
    cond_data.taskRiskyPathProb2 = str(content['taskRiskyPathProb2'])
    cond_data.taskOptChoice = str(content['taskOptChoice'])
    cond_data.taskForceChoice = str(content['taskForceChoice'])
    cond_data.taskPlanChoice = str(content['taskPlanChoice'])
    cond_data.taskShowPath = str(content['taskShowPath'])
    cond_data.taskOutcomeStruct = str(content['taskOutcomeStruct'])
    BaseObject.check_and_save(cond_data)
    result = dict({"success": "yes"})
    return jsonify(result)
