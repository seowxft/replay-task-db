u"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TutorialQuiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Integer)
    quizTime            = Column(Text(length=10000))
    tutorialSession      = Column(Text(length=10000))
    tutorialSessionTry   = Column(Text(length=10000))
    quizSession          = Column(Text(length=10000))
    quizQnNum            = Column(Text(length=10000))
    quizKeypress         = Column(Text(length=10000))
    quizQnRT             = Column(Text(length=10000))
    quizKeypress         = Column(Text(length=10000))
    quizQnRT             = Column(Text(length=10000))
    quizScoreCor         = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_trial_time(self):
        return str(self.quizTime)

    def get_tutorial_session(self):
        return str(self.tutorialSession)

    def get_tutorial_session_try(self):
        return str(self.tutorialSessionTry)

    def get_quiz_session(self):
        return str(self.quizSession)

    def get_quiz_question_no(self):
        return str(self.quizQnNum)

    def get_quiz_key_press(self):
        return str(self.quizKeypress)

    def get_quiz_rt(self):
        return str(self.quizQnRT)

    def get_quiz_correct(self):
        return str(self.quizScoreCor)

    def errors(self):
        errors = super(TutorialQuiz, self).errors()
        return errors
