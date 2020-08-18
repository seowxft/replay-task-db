"""users routes"""
from flask import current_app as app, jsonify, request
from models import TrainingBehaviour, BaseObject


@app.route('/tutorial_data/<user_id>', methods=['POST', 'GET'])

def create_tutorial_data(user_id):

    content                         = request.json
    tutorial_data                   = TutorialData()

    tutorial_data.userID                = int(user_id)
    tutorial_data.tutorialSession       = str(content['tutorialSession'])
    tutorial_data.tutorialSessionTry    = str(content['tutorialSessionTry'])
    tutorial_data.trialNum              = str(content['trialNum'])
    tutorial_data.trialTime             = str(content['trialTime'])
    tutorial_data.fixTime               = str(content['fixTime'])
    tutorial_data.attenIndex            = str(content['attenIndex'])
    tutorial_data.attenCheckKey         = str(content['attenCheckKey'])
    tutorial_data.attenCheckTime        = str(content['attenCheckTime'])
    tutorial_data.stimTime              = str(content['stimTime'])
    tutorial_data.stimIndex             = str(content['stimIndex'])
    tutorial_data.fbProbTrack           = str(content['fbProbTrack'])
    tutorial_data.randProb              = str(content['randProb'])
    tutorial_data.responseKey           = str(content['responseKey'])
    tutorial_data.reactionTime          = str(content['reactionTime'])
    tutorial_data.responseAvoid         = str(content['responseAvoid'])
    tutorial_data.playFbSound           = str(content['playFbSound'])
    tutorial_data.fbTime                = str(content['fbTime'])

    BaseObject.check_and_save(tutorial_data)

    result = dict({"success": "yes"})

    return jsonify(result)
