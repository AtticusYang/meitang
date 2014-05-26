# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column
#from sqlalchemy import event
#from sqlalchemy import DDL
from ..extensions import db


class Device(db.Model):

    __tablename__ = 'device'
    __table__args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(db.Integer, primary_key = True)
    create_time = Column(db.DateTime, default = datetime.now)


    def __repr__(self):
        return '<Device: %r %r>' %(self.id, self.create_time)

    @classmethod
    def gen_eid(cls):
        cur_device = cls()
        db.session.add(cur_device)
        db.session.commit()
        return str(cur_device.id)


class DoubanUser(db.Model):

    __tablename__ = 'douban_user'
    __table__args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(db.Integer, primary_key = True)
    uid = Column(db.Integer, nullable = False, index = True)
    name = Column(db.String(64), nullable = False)
    avatar = Column(db.String(64), nullable = False)
    alt = Column(db.String(64), nullable = True)
    join_time = Column(db.DateTime, nullable = True)
    loc_id = Column(db.Integer, nullable = True)
    loc_name = Column(db.String(64), nullable = True)
    create_time = Column(db.DateTime, default = datetime.now)


    def __init__(self, uid, name, avatar, alt, join_time, loc_id, loc_name, create_time):
        self.uid = uid
        self.name = name
        self.avatar = avatar
        self.alt = alt
        self.join_time = join_time
        self.loc_id = loc_id
        self.loc_name = loc_name
        self.create_time = create_time

    def __repr__(self):
        return '<DoubanUser: %r %r %r %r %r>' %(\
            self.id, self.uid, self.name, self.avatar, self.alt)

    @classmethod
    def add(cls, uid, name, avatar, alt, join_time, loc_id, loc_name):
        douban_user = cls(uid, name, avatar, alt, join_time, loc_id, loc_name)
        db.session.add(douban_user)
        db.session.commit()

    @classmethod
    def get_by_uid(cls, uid):
        douban_user = cls.query.filter_by(uid=uid).first()
        return douban_user

    @classmethod
    def delete(cls, id):
        douban_user = cls.query.filter_by(id=id).first()
        db.session.delete(douban_user)
        db.session.commit()


class Bind(db.Model):
    __tablename__ = 'bind'
    __table__args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(db.Integer, primary_key = True)
    eid = Column(db.Integer, nullable = False, index= True)
    uid = Column(db.Integer, nullable = False, index = True)
    create_time = Column(db.DateTime, default = datetime.now)

    def __init__(self, eid, uid):
        self.eid = eid
        self.uid = uid

    def __repr__(self):
        return '<Bind: %r %r>' %(self.eid, self.uid)

    @classmethod
    def add(cls, eid, uid):
        bind = cls(eid, uid)
        db.session.add(bind)
        db.session.commit()
    
    @classmethod
    def get(cls, eid, uid):
        bind = cls.query.filter(and_(cls.eid == eid, cls.uid==uid)).first()
        return bind

    @classmethod
    def delete(cls, id):
        bind = cls.query.filter_by(id=id).first()
        db.session.delete(bind)
        db.session.commit()
