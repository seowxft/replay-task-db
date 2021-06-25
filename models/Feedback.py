"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class Feedback(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    feedback             = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_feedback(self):
        return str(self.feedback)


    def errors(self):
        errors = super(Feedback, self).errors()
        return errors
