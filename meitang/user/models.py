# -*- coding: utf-8 -*-

from sqlalchemy import Column 
from ..extensions import db
from ..utils import get_current_time

class UserId(db.Model):

    __tablename__ = 'user_id'

    id = Column(db.Integer, autoincrement=100000, primary_key=True)
    created_time = Column(db.DateTime)

    def __init__(self, created_time):
        self.created_time = created_time

    def __repr__(self):
        return '<UserId: %r %r>' %(self.id, self.created_time)

    @classmethod
    def gen_user_id(cls):
        current_user_id = UserId(get_current_time)
        db.session.add(current_user_id)
        db.session.commit()
        return current_user_id.id

