"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TutorialData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID              = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    sectionTime         = Column(Text(length=10000))
    taskSession         = Column(Text(length=10000))
    taskSessionTry      = Column(Text(length=10000))
    trialTime            = Column(Text(length=10000))
    trialNum            = Column(Text(length=10000))
    trialForced         = Column(Text(length=10000))
    trialShuttleWord     = Column(Text(length=10000))
    trialShuttle        = Column(Text(length=10000))
    trialShuttlePos     = Column(Text(length=10000))
    trialShuttleProb     = Column(Text(length=10000))
    trialLastStatePic   = Column(Text(length=10000))
    trialOutcomePic      = Column(Text(length=10000))
    trialOutcomeVal      = Column(Text(length=10000))
    trialSafePath       = Column(Text(length=10000))
    trialRiskyPath1     = Column(Text(length=10000))
    trialRiskyPath2     = Column(Text(length=10000))
    trialSafeProb         = Column(Text(length=10000))
    trialRiskyProb1     = Column(Text(length=10000))
    trialRiskyProb2        = Column(Text(length=10000))
    trialSafeValue     = Column(Text(length=10000))
    trialRiskyValue1     = Column(Text(length=10000))
    trialRiskyValue2   = Column(Text(length=10000))
    trialSafePathEV      = Column(Text(length=10000))
    trialRiskyPathEV1      = Column(Text(length=10000))
    trialRiskyPathEV2       = Column(Text(length=10000))
    trialGambleEV     = Column(Text(length=10000))
    trialChoiceEV     = Column(Text(length=10000))
    trialPlan     = Column(Text(length=10000))
    trialPlanRT              = Column(Text(length=10000))
    trialPlanChoice        = Column(Text(length=10000))
    trialPlanChoiceWords   = Column(Text(length=10000))
    trialPlanPathChosen      = Column(Text(length=10000))
    trialPlanCor        = Column(Text(length=10000))
    trialPathProb     = Column(Text(length=10000))
    trialRT              = Column(Text(length=10000))
    trialKeypress        = Column(Text(length=10000))
    trialGambleChoice   = Column(Text(length=10000))
    trialPathProbChosen        = Column(Text(length=10000))
    trialPath           = Column(Text(length=10000))
    trialPathPicWord    = Column(Text(length=10000))
    trialPathIndx        = Column(Text(length=10000))
    trialOutcomePicWord = Column(Text(length=10000))
    trialOutcomeIndx     = Column(Text(length=10000))
    trialOutcomeValence = Column(Text(length=10000))
    trialOutcomeMag      = Column(Text(length=10000))
    trialOutcomeValue   = Column(Text(length=10000))
    trialOptimalChoice   = Column(Text(length=10000))
    trialCoins          = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_userID(self):
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

    def get_trial_time(self):
        return str(self.trialTime)

    def get_trialNum(self):
        return str(self.trialNum)

    def get_trialForced(self):
        return str(self.trialForced)

    def get_trialShuttleWord(self):
        return str(self.trialShuttleWord)

    def get_trialShuttle(self):
        return str(self.trialShuttle)

    def get_trialShuttlePos(self):
        return str(self.trialShuttlePos)

    def get_trialShuttleProb(self):
        return str(self.trialShuttleProb)

    def get_trialLastStatePic(self):
        return str(self.trialLastStatePic)

    def get_trialOutcomePic(self):
        return str(self.trialOutcomePic)

    def get_trialOutcomeVal(self):
        return str(self.trialOutcomeVal)

    def get_trialSafePath(self):
        return str(self.trialSafePath)

    def get_trialRiskyPath1(self):
        return str(self.trialRiskyPath1)

    def get_trialRiskyPath2(self):
        return str(self.trialRiskyPath2)

    def get_trialSafeProb(self):
        return str(self.trialSafeProb)

    def get_trialRiskyProb1(self):
        return str(self.trialRiskyProb1)

    def get_trialRiskyProb2(self):
        return str(self.trialRiskyProb2)

    def get_trialSafeValue(self):
        return str(self.trialSafeValue)

    def get_trialRiskyValue1(self):
        return str(self.trialRiskyValue1)

    def get_trialRiskyValue2(self):
        return str(self.trialRiskyValue2)

    def get_trialSafePathEV(self):
        return str(self.trialSafePathEV)

    def get_trialRiskyPathEV1(self):
        return str(self.trialRiskyPathEV1)

    def get_trialRiskyPathEV2(self):
        return str(self.trialRiskyPathEV2)

    def get_trialGambleEV(self):
        return str(self.trialGambleEV)

    def get_trialChoiceEV(self):
        return str(self.trialChoiceEV)

    def get_trialPlan(self):
        return str(self.trialPlan)

    def get_trialplanRT(self):
        return str(self.trialPlanRT)

    def get_trialPlanChoice(self):
        return str(self.trialPlanChoice)

    def get_trialPlanChoiceWords(self):
        return str(self.trialPlanChoiceWords)

    def get_trialPlanPathChosen(self):
        return str(self.trialPlanPathChosen)

    def get_trialPlanCor(self):
        return str(self.trialPlanCor)

    def get_trialPathProb(self):
        return str(self.trialPathProb)

    def get_trialRT(self):
        return str(self.trialRT)

    def get_trialKeypress(self):
        return str(self.trialKeypress)

    def get_trialGambleChoice(self):
        return str(self.trialGambleChoice)

    def get_trialPathProbChosen(self):
        return str(self.trialPathProbChosen)

    def get_trialPath(self):
        return str(self.trialPath)

    def get_trialPathPicWord(self):
        return str(self.trialPathPicWord)

    def get_trialPathIndx(self):
        return str(self.trialPathIndx)

    def get_trialOutcomePicWord(self):
        return str(self.trialOutcomePicWord)

    def get_trialOutcomeIndx(self):
        return str(self.trialOutcomeIndx)

    def get_trialOutcomeValence(self):
        return str(self.trialOutcomeValence)

    def get_trialOutcomeMag(self):
        return str(self.trialOutcomeMag)

    def get_trialOutcomeValue(self):
        return str(self.trialOutcomeValue)

    def get_trialOptimalChoice(self):
        return str(self.trialOptimalChoice)

    def get_trialCoins(self):
        return str(self.trialCoins)

    def errors(self):
        errors = super(TutorialData, self).errors()
        return errors
