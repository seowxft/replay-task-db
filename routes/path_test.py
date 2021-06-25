"""users routes"""
from flask import current_app as app, jsonify, request
from models import PathTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/path_test/<user_id>', methods=['POST', 'GET'])
def create_path_test(user_id):
    content = request.json
    path_test = PathTest()
    path_test.userID = str(content['userID'])
    path_test.date        = str(content['date'])
    path_test.startTime   = str(content['startTime'])
    path_test.sectionTime = str(content['sectionTime'])
    path_test.taskSession = str(content['taskSession'])
    path_test.taskSessionTry = str(content['taskSessionTry'])
    path_test.taskSection = str(content['taskSection'])
    path_test.trialTime = str(content['trialTime'])
    path_test.trialNum = str(content['trialNum'])
    path_test.trialPart = str(content['trialPart'])
    path_test.trialPicIndx = str(content['trialPicIndx'])
    path_test.trialPicWord = str(content['trialPicWord'])
    path_test.trialQn = str(content['trialQn'])
    path_test.trialPicAns = str(content['trialPicAns'])
    path_test.trialRT = str(content['trialRT'])
    path_test.trialKeypress = str(content['trialKeypress'])
    path_test.trialCor = str(content['trialCor'])
    path_test.trialScore = str(content['trialScore'])

    BaseObject.check_and_save(path_test)
    result = dict({"success": "yes"})
    return jsonify(result)
