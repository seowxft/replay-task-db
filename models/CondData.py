"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class CondData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID              = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    sessionTime          = Column(Text(length=10000))
    trialTime          = Column(Text(length=10000))
    taskSession         = Column(Text(length=10000))
    taskSessionTry      = Column(Text(length=10000))
    structNum      = Column(Text(length=10000))
    outcomeWord          = Column(Text(length=10000))
    outcomeVal           = Column(Text(length=10000))
    outcomeIndx          = Column(Text(length=10000))
    stateWord          = Column(Text(length=10000))
    stateIndx           = Column(Text(length=10000))
    pathOne          = Column(Text(length=10000))
    pathTwo          = Column(Text(length=10000))
    pathThree          = Column(Text(length=10000))
    tutForcedPaths          = Column(Text(length=10000))
    tutSafePathOutcome           = Column(Text(length=10000))
    tutRiskyPathOutcome1          = Column(Text(length=10000))
    tutRiskyPathOutcome2          = Column(Text(length=10000))
    tutSafePathProb          = Column(Text(length=10000))
    tutRiskyPathProb1          = Column(Text(length=10000))
    tutRiskyPathProb2          = Column(Text(length=10000))
    tutOptChoice          = Column(Text(length=10000))
    tutForceChoice          = Column(Text(length=10000))
    taskSafePathOutcome           = Column(Text(length=10000))
    taskRiskyPathOutcome1          = Column(Text(length=10000))
    taskRiskyPathOutcome2          = Column(Text(length=10000))
    taskSafePathProb          = Column(Text(length=10000))
    taskRiskyPathProb1          = Column(Text(length=10000))
    taskRiskyPathProb2          = Column(Text(length=10000))
    taskOptChoice          = Column(Text(length=10000))
    taskForceChoice          = Column(Text(length=10000))

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

    def get_trialTime(self):
        return str(self.trialTime)

    def get_startTime(self):
        return str(self.taskSession)

    def get_restartTime(self):
        return str(self.taskSessionTry)

    def get_structNum(self):
        return str(self.structNum)

    def get_outcomeWord(self):
        return str(self.outcomeWord)

    def get_outcomeVal(self):
        return str(self.outcomeVal)

    def get_outcomeIndx(self):
        return str(self.outcomeIndx)

    def get_stateWord(self):
        return str(self.stateWord)

    def get_stateIndx(self):
        return str(self.stateIndx)

    def get_pathOne(self):
        return str(self.pathOne)

    def get_pathTwo(self):
        return str(self.pathTwo)

    def get_pathThree(self):
        return str(self.pathThree)

    def get_tutForcedPaths(self):
        return str(self.tutForcedPaths)

    def get_tutSafePathOutcome(self):
        return str(self.tutSafePathOutcome)

    def get_tutRiskyPathOutcome1(self):
        return str(self.tutRiskyPathOutcome1)

    def get_tutRiskyPathOutcome2(self):
        return str(self.tutRiskyPathOutcome2)

    def get_tutSafePathProb(self):
        return str(self.tutSafePathProb)

    def get_tutRiskyPathProb1(self):
        return str(self.tutRiskyPathProb1)

    def get_tutRiskyPathProb2(self):
        return str(self.tutRiskyPathProb2)

    def get_tutOptChoice(self):
        return str(self.tutOptChoice)

    def get_tutForceChoice(self):
        return str(self.tutForceChoice)

    def get_taskSafePathOutcome(self):
        return str(self.taskSafePathOutcome)

    def get_taskRiskyPathOutcome1(self):
        return str(self.taskRiskyPathOutcome1)

    def get_taskRiskyPathOutcome2(self):
        return str(self.taskRiskyPathOutcome2)

    def get_taskSafePathProb(self):
        return str(self.taskSafePathProb)

    def get_taskRiskyPathProb1(self):
        return str(self.taskRiskyPathProb1)

    def get_taskRiskyPathProb2(self):
        return str(self.taskRiskyPathProb2)

    def get_taskOptChoice(self):
        return str(self.taskOptChoice)

    def get_taskForceChoice(self):
        return str(self.taskForceChoice)

    def errors(self):
        errors = super(CondData, self).errors()
        return errors
