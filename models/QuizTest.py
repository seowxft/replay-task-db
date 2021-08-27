"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class QuizTest(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID              = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    sectionTime          = Column(Text(length=10000))
    trialTime          = Column(Text(length=10000))
    taskSession         = Column(Text(length=10000))
    taskSessionTry      = Column(Text(length=10000))
    trialSection        =  Column(Text(length=10000))
    trialNum         = Column(Text(length=10000))
    trialRT          = Column(Text(length=10000))
    trialKeypress    = Column(Text(length=10000))
    trialPicIndx     = Column(Text(length=10000))
    trialPicWord     = Column(Text(length=10000))
    trialPicAns      = Column(Text(length=10000))
    trialPlanAns     = Column(Text(length=10000))
    trialPlanRT      = Column(Text(length=10000))
    trialPlanChoice  = Column(Text(length=10000))
    trialPlanChoiceWords= Column(Text(length=10000))
    trialPlanPathChosen= Column(Text(length=10000))
    trialCor         = Column(Text(length=10000))
    trialScore      = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_sessionTime(self):
        return str(self.sectionTime)

    def get_trialTime(self):
        return str(self.trialTime)

    def get_taskSession(self):
        return str(self.taskSession)

    def get_taskSessionTry(self):
        return str(self.taskSessionTry)

    def get_trialSection(self):
        return str(self.trialSection)

    def get_trialNum(self):
        return str(self.trialNum)

    def get_trialRT(self):
        return str(self.trialRT)

    def get_trialKeypress(self):
        return str(self.trialKeypress)

    def get_trialPicIndx(self):
        return str(self.trialPicIndx)

    def get_trialPicWord(self):
        return str(self.trialPicWord)

    def get_trialPicAns(self):
        return str(self.trialPicAns)

    def get_trialPlanAns(self):
        return str(self.trialPlanAns)

    def get_trialplanRT(self):
        return str(self.trialPlanRT)

    def get_trialPlanChoice(self):
        return str(self.trialPlanChoice)

    def get_trialPlanChoiceWords(self):
        return str(self.trialPlanChoiceWords)

    def get_trialPlanPathChosen(self):
        return str(self.trialPlanPathChosen)

    def get_trialCor(self):
        return str(self.trialCor)

    def get_trialScore(self):
        return str(self.trialScore)

    def errors(self):
        errors = super(QuizTest, self).errors()
        return errors
