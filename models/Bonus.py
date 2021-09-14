"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class Bonus(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    sectionTime         = Column(Text(length=10000))
    taskSession         = Column(Text(length=10000))
    taskSessionTry         = Column(Text(length=10000))
    taskCoins         = Column(Text(length=10000))
    taskBonus         = Column(Text(length=10000))
    structNum         = Column(Text(length=10000))
    maxCoins         = Column(Text(length=10000))

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

    def get_taskCoins(self):
        return str(self.taskCoins)

    def get_taskBonus(self):
        return str(self.taskBonus)

    def get_structNum(self):
        return str(self.structNum)

    def get_maxCoins(self):
        return str(self.maxCoins)

    def errors(self):
        errors = super(Bonus, self).errors()
        return errors
