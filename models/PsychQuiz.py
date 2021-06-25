"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PsychQuiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID           = Column(Text(length=10000))
    date             = Column(Text(length=10000))
    startTime        = Column(Text(length=10000))
    sectionTime     = Column(Text(length=10000))
    qnTimeStart      = Column(Text(length=10000))
    qnTimeEnd        = Column(Text(length=10000))
    PgFinish_demo    = Column(Text(length=10000))
    PgFinish_OCIR    = Column(Text(length=10000))
    PgFinish_STAI_Y1  = Column(Text(length=10000))
    PgFinish_STAI_Y2  = Column(Text(length=10000))
    PgFinish_BIS11    = Column(Text(length=10000))
    PgFinish_SDS      = Column(Text(length=10000))
    PgRT_demo        = Column(Text(length=10000))
    PgRT_OCIR        = Column(Text(length=10000))
    PgRT_STAI_Y1     = Column(Text(length=10000))
    PgRT_STAI_Y2     = Column(Text(length=10000))
    PgRT_BIS11       = Column(Text(length=10000))
    PgRT_SDS         = Column(Text(length=10000))
    age              = Column(Text(length=10000))
    gender           = Column(Text(length=10000))
    OCIR             = Column(Text(length=10000))
    STAI_Y1          = Column(Text(length=10000))
    STAI_Y2          = Column(Text(length=10000))
    BIS11            = Column(Text(length=10000))
    SDS              = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_start_time(self):
        return str(self.startTime)

    def get_section_time(self):
        return str(self.sectionTime)

    def get_qn_start(self):
        return str(self.qnTimeStart)

    def get_qn_end(self):
        return str(self.qnTimeEnd)

    def get_pg0_finish(self):
        return str(self.PgFinish_demo)

    def get_pg1_finish(self):
        return str(self.PgFinish_OCIR)

    def get_pg2_finish(self):
        return str(self.PgFinish_STAI_Y1)

    def get_pg3_finish(self):
        return str(self.PgFinish_STAI_Y2)

    def get_pg4_finish(self):
        return str(self.PgFinish_BIS11)

    def get_pg5_finish(self):
        return str(self.PgFinish_SDS)

    def get_pg0_rt(self):
        return str(self.PgRT_demo)

    def get_pg1_rt(self):
        return str(self.PgRT_OCIR)

    def get_pg2_rt(self):
        return str(self.PgRT_STAI_Y1)

    def get_pg3_rt(self):
        return str(self.PgRT_STAI_Y2)

    def get_pg4_rt(self):
        return str(self.PgRT_BIS11)

    def get_pg5_rt(self):
        return str(self.PgRT_SDS)

    def get_age(self):
        return str(self.age)

    def get_gender(self):
        return str(self.gender)

    def get_ocir(self):
        return str(self.OCIR)

    def get_staiOne(self):
        return str(self.STAI_Y1)

    def get_staiTwo(self):
        return str(self.STAI_Y2)

    def get_bis(self):
        return str(self.BIS11)

    def get_sds(self):
        return str(self.SDS)

    def errors(self):
        errors = super(PsychQuiz, self).errors()
        return errors
