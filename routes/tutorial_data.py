"""users routes"""
from flask import current_app as app, jsonify, request
from models import TutorialData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/tutorial_data/<user_id>', methods=['POST', 'GET'])
def create_tutorial_data(user_id):
    content = request.json
    tutorial_data = TutorialData()
    tutorial_data.userID      = str(content['userID'])
    tutorial_data.date        = str(content['date'])
    tutorial_data.startTime   = str(content['startTime'])
    tutorial_data.sectionTime    = str(content['sectionTime'])
    tutorial_data.taskSession    = str(content['taskSession'])
    tutorial_data.taskSessionTry = str(content['taskSessionTry'])
    tutorial_data.trialTime  = str(content['trialTime'])
    tutorial_data.trialNum   = str(content['trialNum'])
    tutorial_data.trialForced    = str(content['trialForced'])
    tutorial_data.trialShuttleWord = str(content['trialShuttleWord'])
    tutorial_data.trialShuttle  = str(content['trialShuttle'])
    tutorial_data.trialShuttlePos = str(content['trialShuttlePos'])
    tutorial_data.trialShuttleProb     = str(content['trialShuttleProb'])
    tutorial_data.trialLastStatePic    = str(content['trialLastStatePic'])
    tutorial_data.trialOutcomePic  = str(content['trialOutcomePic'])
    tutorial_data.trialOutcomeVal     = str(content['trialOutcomeVal'])
    tutorial_data.trialSafePath  = str(content['trialSafePath'])
    tutorial_data.trialRiskyPath1 = str(content['trialRiskyPath1'])
    tutorial_data.trialRiskyPath2  = str(content['trialRiskyPath2'])
    tutorial_data.trialSafeProb    = str(content['trialSafeProb'])
    tutorial_data.trialRiskyProb1 = str(content['trialRiskyProb1'])
    tutorial_data.trialRiskyProb2  = str(content['trialRiskyProb2'])
    tutorial_data.trialSafeValue = str(content['trialSafeValue'])
    tutorial_data.trialRiskyValue1     = str(content['trialRiskyValue1'])
    tutorial_data.trialRiskyValue2    = str(content['trialRiskyValue2'])
    tutorial_data.trialSafePathEV  = str(content['trialSafePathEV'])
    tutorial_data.trialRiskyPathEV1     = str(content['trialRiskyPathEV1'])
    tutorial_data.trialRiskyPathEV2  = str(content['trialRiskyPathEV2'])
    tutorial_data.trialGambleEV = str(content['trialGambleEV'])
    tutorial_data.trialChoiceEV  = str(content['trialChoiceEV'])
    tutorial_data.trialPlan  = str(content['trialPlan'])
    tutorial_data.trialPlanRT       = str(content['trialPlanRT'])
    tutorial_data.trialPlanChoice       = str(content['trialPlanChoice'])
    tutorial_data.trialPlanChoiceWords = str(content['trialPlanChoiceWords'])
    tutorial_data.trialPlanPathChosen = str(content['trialPlanPathChosen'])
    tutorial_data.trialPlanCor  = str(content['trialPlanCor'])
    tutorial_data.trialPathProb  = str(content['trialPathProb'])
    tutorial_data.trialRT       = str(content['trialRT'])
    tutorial_data.trialKeypress       = str(content['trialKeypress'])
    tutorial_data.trialGambleChoice = str(content['trialGambleChoice'])
    tutorial_data.trialPathProbChosen  = str(content['trialPathProbChosen'])
    tutorial_data.trialPath     = str(content['trialPath'])
    tutorial_data.trialPathPicWord  = str(content['trialPathPicWord'])
    tutorial_data.trialPathIndx = str(content['trialPathIndx'])
    tutorial_data.trialOutcomePicWord  = str(content['trialOutcomePicWord'])
    tutorial_data.trialOutcomeIndx       = str(content['trialOutcomeIndx'])
    tutorial_data.trialOutcomeValence       = str(content['trialOutcomeValence'])
    tutorial_data.trialGambleChoice = str(content['trialGambleChoice'])
    tutorial_data.trialOutcomeMag       = str(content['trialOutcomeMag'])
    tutorial_data.trialOutcomeValue       = str(content['trialOutcomeValue'])
    tutorial_data.trialOptimalChoice       = str(content['trialOptimalChoice'])
    tutorial_data.trialCoins = str(content['trialCoins'])

    BaseObject.check_and_save(tutorial_data)
    result = dict({"success": "yes"})
    return jsonify(result)
