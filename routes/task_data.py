"""users routes"""
from flask import current_app as app, jsonify, request
from models import TaskData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/task_data/<user_id>', methods=['POST', 'GET'])
def create_task_data(user_id):
    content = request.json
    task_data = TaskData()
    task_data.userID      = str(content['userID'])
    task_data.date        = str(content['date'])
    task_data.startTime   = str(content['startTime'])
    task_data.sectionTime    = str(content['sectionTime'])
    task_data.taskSession    = str(content['taskSession'])
    task_data.taskSessionTry = str(content['taskSessionTry'])
    task_data.trialTime  = str(content['trialTime'])
    task_data.trialNum   = str(content['trialNum'])
    task_data.trialBlock  = str(content['trialBlock'])
    task_data.trialNumInBlock   = str(content['trialNumInBlock'])
    task_data.trialForced    = str(content['trialForced'])
    task_data.trialShuttleWord = str(content['trialShuttleWord'])
    task_data.trialShuttle  = str(content['trialShuttle'])
    task_data.trialShuttlePos = str(content['trialShuttlePos'])
    task_data.trialShuttleProb     = str(content['trialShuttleProb'])
    task_data.trialLastStatePic    = str(content['trialLastStatePic'])
    task_data.trialOutcomePic  = str(content['trialOutcomePic'])
    task_data.trialOutcomeVal     = str(content['trialOutcomeVal'])
    task_data.trialSafePath  = str(content['trialSafePath'])
    task_data.trialRiskyPath1 = str(content['trialRiskyPath1'])
    task_data.trialRiskyPath2  = str(content['trialRiskyPath2'])

    task_data.trialSafeProb    = str(content['trialSafeProb'])
    task_data.trialRiskyProb1 = str(content['trialRiskyProb1'])
    task_data.trialRiskyProb2  = str(content['trialRiskyProb2'])
    task_data.trialSafeValue = str(content['trialSafeValue'])
    task_data.trialRiskyValue1     = str(content['trialRiskyValue1'])
    task_data.trialRiskyValue2    = str(content['trialRiskyValue2'])
    task_data.trialSafePathEV  = str(content['trialSafePathEV'])
    task_data.trialRiskyPathEV1     = str(content['trialRiskyPathEV1'])
    task_data.trialRiskyPathEV2  = str(content['trialRiskyPathEV2'])
    task_data.trialGambleEV = str(content['trialGambleEV'])
    task_data.trialChoiceEV  = str(content['trialChoiceEV'])

    task_data.trialPlan  = str(content['trialPlan'])
    task_data.trialPlanRT       = str(content['trialPlanRT'])
    task_data.trialPlanChoice       = str(content['trialPlanChoice'])
    task_data.trialPlanChoiceWords = str(content['trialPlanChoiceWords'])
    task_data.trialPlanPathChosen = str(content['trialPlanPathChosen'])
    task_data.trialPlanCor  = str(content['trialPlanCor'])

    task_data.trialPathProb  = str(content['trialPathProb'])
    task_data.trialRT       = str(content['trialRT'])
    task_data.trialKeypress       = str(content['trialKeypress'])
    task_data.trialGambleChoice = str(content['trialGambleChoice'])
    task_data.trialPathProbChosen  = str(content['trialPathProbChosen'])
    task_data.trialPath     = str(content['trialPath'])
    task_data.trialPathPicWord  = str(content['trialPathPicWord'])
    task_data.trialPathIndx = str(content['trialPathIndx'])
    task_data.trialOutcomePicWord  = str(content['trialOutcomePicWord'])
    task_data.trialOutcomeIndx       = str(content['trialOutcomeIndx'])
    task_data.trialOutcomeValence       = str(content['trialOutcomeValence'])
    task_data.trialGambleChoice = str(content['trialGambleChoice'])
    task_data.trialOutcomeMag       = str(content['trialOutcomeMag'])
    task_data.trialOutcomeValue       = str(content['trialOutcomeValue'])
    task_data.trialOptimalChoice       = str(content['trialOptimalChoice'])
    task_data.trialCoins = str(content['trialCoins'])

    BaseObject.check_and_save(task_data)
    result = dict({"success": "yes"})
    return jsonify(result)
