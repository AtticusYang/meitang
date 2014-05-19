#-*- coding:utf-8 -*-

from sqlalchemy import Column
from ..extensions import db

class Post(db.Model):

    __table__name = 'post'

    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.Integer)
    content = db.Column(db.String(160), nullable = True)
    image_id = db.Column(db.String(64))
    small_image_id = db.Column(db.String(64))
    pub_time = db.Column(db.DateTime)
    open_level = db.Column(db.SmallInteger, default = 0)
    favor_count = db.Column(db.SmallInteger, default = 0)
    source = db.Column(db.SmallInteger, default = 0)
    source_url = db.Column(db.String(64), nullable = True)


    def __init__(self, uid, content, image_id, small_image_id,\
            pub_time, open_level, favor_count, source, source_url):
        self.uid = uid
        self.content = content
        self.image_id = image_id
        self.small_image_id = small_image_id
        self.pub_time = pub_time
        self.open_level = open_level
        self.favor_count = favor_count
        self.source = source
        self.source_url = source_url



    def __repr__(self):
        return '<Post: %r %r %r %r %r>' %(self.id, self.uid, self.content, self.image_id, self.small_image_id)


    @classmethod
    def add(cls, uid, content, image_id, small_image_id, pub_time,\
            open_level = 0, favor_count = 0, source = 0, source_url = None):
        post = cls(uid, content, image_id, small_image_id, pub_time,\
                open_level, favor_count, source, source_url)
        db.session.add(post)
        db.seesion.commit()

    @classmethod
    def delete(cls, id):
        post = cls.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()


    @classmethod
    def get_latest(cls, id, count):
        posts = cls.query.filter_by(id>id).limit(count)
        return posts


    @classmethod
    def set_open_level(cls, id, open_level):
        post = cls.query.filter_by(id=id).first()
        post.open_level = open_level
        db.sesson.commit()


