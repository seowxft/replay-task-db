"""users routes"""
from flask import current_app as app, jsonify, request
from models import Feedback, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/feedback/<user_id>', methods=['POST', 'GET'])
def create_feedback(user_id):
    content = request.json
    feedback = Feedback()
    feedback.userID     = str(content['userID'])
    feedback.date        = str(content['date'])
    feedback.startTime   = str(content['startTime'])
    feedback.feedback    = str(content['feedback'])

    BaseObject.check_and_save(feedback)
    result = dict({"success": "yes"})
    return jsonify(result)
