"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PathTest(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    sectionTime          = Column(Text(length=10000))
    taskSession          = Column(Text(length=10000))
    taskSessionTry       = Column(Text(length=10000))
    taskSection          = Column(Text(length=10000))
    trialTime            = Column(Text(length=10000))
    trialNum             = Column(Text(length=10000))
    trialPart            = Column(Text(length=10000))
    trialPicIndx         = Column(Text(length=10000))
    trialPicWord         = Column(Text(length=10000))
    trialQn               = Column(Text(length=10000))
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

    def get_taskSession(self):
        return str(self.taskSession)

    def get_taskSessionTry(self):
        return str(self.taskSessionTry)

    def get_taskSection(self):
        return str(self.taskSection)

    def get_trialTime(self):
        return str(self.trialTime)

    def get_trialPart(self):
        return str(self.trialPart)

    def get_trialPicIndx(self):
        return str(self.trialPicIndx)

    def get_trialPicWord(self):
        return str(self.trialPicWord)

    def get_trialQn(self):
        return str(self.trialQn)

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
        errors = super(PathTest, self).errors()
        return errors
