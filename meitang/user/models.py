# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column
from sqlalchemy import event
from sqlalchemy import DDL
from ..extensions import db


class Device(db.Model):


    __tablename__ = 'device'

    id = Column(db.Integer, primary_key=True)
    create_time = Column(db.DateTime, default=datetime.datetime.now)


    def __repr__(self):
        return '<Device: %r %r>' %(self.id, self.create_time)

    @classmethod
    def gen_eid(cls):
        current_user_id = UserId()
        db.session.add(current_user_id)
        db.session.commit()
        return str(current_user_id.id)




class BindUser(db.Model):

    __tablename__ = 'bind_user'

    id = Column(db.Integer, primary_key = True)
    uid = Column(db.Integer, nullable = False, index = True)
    name = Column(db.String(64), nullable = False)
    avatar = Column(db.String(64), nullable = False)
    alt = Column(db.String(64), nullable = True)
    create_time = (db.DateTime)
    loc_id = Column(db.Integer, nullable = True)
    loc_name = Column(db.String(64), nullable = True)
    bind_time = (db.DateTime)


    def __init__(self, uid, name, avatar, alt, create_time, loc_id, loc_name):
        self.uid = uid
        self.name = name
        self.avatar = avatar
        self.alt = alt
        self.create_time = create_time
        self.loc_id = loc_id
        self.loc_name = loc_name

    def __repr__(self):
        return '<BindUser: %r %r %r>' %(self.id, self.uid, self.name)

    @classmethod
    def add(cls, uid, name, avatar, alt, create_time, loc_id, loc_name):
        bind_user = cls(uid, name, avatar, alt, create_time, loc_id, loc_name)
        db.session.add(bind_user)
        db.session.commit()

    @classmethod
    def get_by_uid(cls, uid):
        bind_user = cls.query.filter_by(uid=uid).first()
        return bind_user

    @classmethod
    def delete(cls, id):
        bind_user = cls.query.filter_by(id=id).first()
        db.session.delete(bind_user)
        db.session.commit()


