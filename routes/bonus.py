"""users routes"""
from flask import current_app as app, jsonify, request
from models import Bonus, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/bonus_data/<user_id>', methods=['POST', 'GET'])
def create_bonus_data(user_id):
    content = request.json
    bonus_data = Bonus()
    bonus_data.userID = str(content['userID'])
    bonus_data.date        = str(content['date'])
    bonus_data.startTime   = str(content['startTime'])
    bonus_data.sectionTime = str(content['sectionTime'])
    bonus_data.taskSession = str(content['taskSession'])
    bonus_data.taskSessionTry = str(content['taskSessionTry'])
    bonus_data.taskCoins = str(content['taskCoins'])
    bonus_data.taskBonus = str(content['taskBonus'])
    bonus_data.structNum = str(content['structNum'])
    bonus_data.maxCoins = str(content['maxCoins'])

    BaseObject.check_and_save(bonus_data)
    result = dict({"success": "yes"})
    return jsonify(result)
