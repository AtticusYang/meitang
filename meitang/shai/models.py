#-*- coding:utf-8 -*-

from sqlalchemy import Column
from ..extensions import db

from datetime import datetime

class Post(db.Model):

    __table__name = 'post'
    __table__args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.String(16))
    content = db.Column(db.String(160), nullable = True)
    image_id = db.Column(db.String(64))
    small_image_id = db.Column(db.String(64))
    open_level = db.Column(db.SmallInteger, default = 0)
    favor_count = db.Column(db.SmallInteger, default = 0)
    source = db.Column(db.SmallInteger, default = 0)
    source_url = db.Column(db.String(64), nullable = True)
    pub_time = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, uid, content, image_id, small_image_id,\
            open_level, favor_count, source, source_url):
        self.uid = uid
        self.content = content
        self.image_id = image_id
        self.small_image_id = small_image_id
        self.open_level = open_level
        self.favor_count = favor_count
        self.source = source
        self.source_url = source_url

    def __repr__(self):
        return '<Post: %r %r %r %r %r %r %r %r %r>' %(self.id, self.uid, \
            self.content, self.image_id, self.small_image_id, self.open_level, \
            self.favor_count, self.source, self.source_url, self.pub_time.strftime("%Y-%m-%d"))

    @classmethod
    def add(cls, uid, content, image_id, small_image_id, open_level = 0,\
            favor_count = 0, source = 0, source_url = None):
        post = cls(uid, content, image_id, small_image_id, \
                open_level, favor_count, source, source_url)
        db.session.add(post)
        db.session.commit()


    @classmethod
    def delete(cls, id):
        post = cls.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()


    @classmethod
    def get_latest(cls, max_id, count):
        if max_id == 0:
            posts = cls.query.order_by('id desc').limit(count).all()
        else:
            posts = cls.query.filter_by(id<max_id).limit(count).all()
        return posts


    @classmethod
    def set_open_level(cls, id, open_level):
        post = cls.query.filter_by(id=id).first()
        post.open_level = open_level
        db.session.commit()

