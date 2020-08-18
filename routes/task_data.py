"""users routes"""
from flask import current_app as app, jsonify, request
from models import TaskData, BaseObject


@app.route('/task_data/<user_id>/', methods=['POST', 'GET'])

def create_dataframe(user_id):

    content     = request.json
    task_data   = TaskData()

    task_data.userID            = int(user_id)
    task_data.trialTime         = str(content['trialTime'])
    task_data.taskSessionTry    = str(content['taskSessionTry'])
    task_data.trialNum          = str(content['trialNum'])
    task_data.blockNum          = str(content['blockNum'])
    task_data.trialinBlockNum   = str(content['trialinBlockNum'])
    task_data.devaluedBlock     = str(content['devaluedBlock'])
    task_data.attenIndex        = str(content['attenIndex'])
    task_data.attenCheckKey     = str(content['attenCheckKey'])
    task_data.attenCheckTime    = str(content['attenCheckTime'])
    task_data.stimIndex         = str(content['stimIndex'])
    task_data.fbProbTrack       = str(content['fbProbOri'])
    task_data.randProb          = str(content['randProb'])
    task_data.responseKey       = str(content['responseKey'])
    task_data.reactionTime      = str(content['reactionTime'])
    task_data.playFbSound       = str(content['trialinBlockNum'])


    BaseObject.check_and_save(task_data)

    result = dict({"success": "yes"})

    return jsonify(result)
