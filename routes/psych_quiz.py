"""users routes"""
from flask import current_app as app, jsonify, request
from models import PsychQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/psych_quiz/<user_id>', methods=['POST', 'GET'])
def create_psych_data(user_id):
    content = request.json
    psych_quiz = PsychQuiz()
    psych_quiz.userID = str(content['userID'])
    psych_quiz.date = str(content['date'])
    psych_quiz.startTime = str(content['startTime'])
    psych_quiz.sectionTime = str(content['sectionTime'])
    psych_quiz.qnTimeStart = str(content['qnTimeStart'])
    psych_quiz.qnTimeEnd = str(content['qnTimeEnd'])
    psych_quiz.PgFinish_demo = str(content['PgFinish_demo'])
    psych_quiz.PgFinish_OCIR = str(content['PgFinish_OCIR'])
    psych_quiz.PgFinish_STAI_Y1 = str(content['PgFinish_STAI_Y1'])
    psych_quiz.PgFinish_STAI_Y2 = str(content['PgFinish_STAI_Y2'])
    psych_quiz.PgFinish_BIS11 = str(content['PgFinish_BIS11'])
    psych_quiz.PgFinish_SDS = str(content['PgFinish_SDS'])
    psych_quiz.PgRT_demo = str(content['PgRT_demo'])
    psych_quiz.PgRT_OCIR = str(content['PgRT_OCIR'])
    psych_quiz.PgRT_STAI_Y1 = str(content['PgRT_STAI_Y1'])
    psych_quiz.PgRT_STAI_Y2 = str(content['PgRT_STAI_Y2'])
    psych_quiz.PgRT_BIS11= str(content['PgRT_BIS11'])
    psych_quiz.PgRT_SDS = str(content['PgRT_SDS'])
    psych_quiz.age = str(content['age'])
    psych_quiz.gender = str(content['gender'])
    psych_quiz.OCIR = str(content['OCIR'])
    psych_quiz.STAI_Y1= str(content['STAI_Y1'])
    psych_quiz.STAI_Y2= str(content['STAI_Y2'])
    psych_quiz.BIS11= str(content['BIS11'])
    psych_quiz.SDS= str(content['SDS'])

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
