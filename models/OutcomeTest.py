"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class OutcomeTest(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    sectionTime          = Column(Text(length=10000))
    taskSession          = Column(Text(length=10000))
    taskSessionTry       = Column(Text(length=10000))
    trialTime            = Column(Text(length=10000))
    trialNum             = Column(Text(length=10000))
    trialPicIndx        = Column(Text(length=10000))
    trialPicWord         = Column(Text(length=10000))
    trialPicNum          = Column(Text(length=10000))
    trialPicValue        = Column(Text(length=10000))
    trialPicAns          = Column(Text(length=10000))
    trialRT              = Column(Text(length=10000))
    trialKeypress        = Column(Text(length=10000))
    trialCor             = Column(Text(length=10000))
    trialScore           = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_sectionTime(self):
        return str(self.sectionTime)

    def get_task_session(self):
        return str(self.taskSession)

    def get_task_session_try(self):
        return str(self.taskSessionTry)

    def get_trialTime(self):
        return str(self.trialTime)

    def get_trialNum(self):
        return str(self.trialNum)

    def get_trialPicIndx(self):
        return str(self.trialPicIndx)

    def get_trialPicWord(self):
        return str(self.trialPicWord)

    def get_trialPicNum(self):
        return str(self.trialPicNum)

    def get_trialPicValue(self):
        return str(self.trialPicValue)

    def get_trialPicAns(self):
        return str(self.trialPicAns)

    def get_trialRT(self):
        return str(self.trialRT)

    def get_trialKeypress(self):
        return str(self.trialKeypress)

    def get_trialCor(self):
        return str(self.trialCor)

    def get_trialScore(self):
        return str(self.trialScore)

    def errors(self):
        errors = super(OutcomeTest, self).errors()
        return errors
