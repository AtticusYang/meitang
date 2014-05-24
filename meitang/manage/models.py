# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column
#from sqlalchemy import event
#from sqlalchemy import DDL
from ..extensions import db


class Online(db.Model):

    __tablename__ = 'online'
    __table__args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(db.Integer, primary_key = True)
    eid = Column(db.Integer)
    client_name = Column(db.String(32))
    client_version = Column(db.String(32))
    status = Column(db.String(32))
    uid = Column(db.String(32))
    name = Column(db.String(32))
    time = Column(db.DateTime, default = datetime.now)

    def __init__(self, eid, client_name, client_version, status, uid, name):
        self.eid = eid
        self.client_name = client_name
        self.client_version = client_version
        client.status = status
        client.uid = uid
        client.name = name


    def __repr__(self):
        return '<Online: %r %r %r %r>' %(self.eid, self.client_name, self.client_version, client.status)

    @classmethod
    def add(cls, eid, client_name, client_version, status, uid=None, name=None):
        online = cls(eid, client_name, client_version, status, uid, name)
        db.session.add(online)
        db.session.commit()


class FeedBack(db.Model):

    __tablename__ = 'feedback'
    __table__args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(db.Integer, primary_key = True)
    eid = Column(db.Integer)
    content = Column(db.String(256))
    uid = Column(db.String(32))
    name = Column(db.String(32))
    client_name = Column(db.String(32))
    client_version = Column(db.String(32))
    contact = Column(db.String(32))

    def __init__(self, eid, content, uid, name, client_name, client_version, contact):
        self.eid = eid
        self.content = content
        self.name = name
        self.client_name = client_name
        self.client_version = client_version
        self.contact = contact

    def __repr__(self):
        return '<FeedBack: %r %r>' %(self.eid, self.content)

    @classmethod
    def add(cls, eid, content, uid=None, name=None, client_name=None, client_version=None, contact=None):
        feedback = cls(eid, content, uid, name, client_name, client_version, contact)
        db.session.add(feedback)
        db.session.commit()


