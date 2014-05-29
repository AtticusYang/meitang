#-*- coding:utf-8 -*-
from marshmallow import Serializer, fields

class DoubanUserSerializer(Serializer):
    uid = fields.String(attribute='uid')
    name = fields.String(attribute='name')
    alt = fields.String(attribute='alt')
    avatar = fields.Function(lambda obj: "http://dadanshai.com/image/"+obj.avatar)
    #avatar = fields.String(attribute='avatar')
    join_time = fields.DateTime(attribute='join_time')
    loc_id = fields.String(attribute='loc_id')
    loc_name = fields.String(attribute='loc_name')


class PostSerializer(Serializer):
    post_id = fields.String(attribute='id')
    #uid = fields.String(attribute='uid')
    content = fields.String(attribute='content')
    image = fields.Function(lambda obj: "http://dadanshai.com/image/"+obj.image_id)
    small_image = fields.Function(lambda obj: "http://dadanshai.com/image/"+obj.small_image_id)
    favor_count = fields.String(attribute='favor_count')
    pub_time = fields.DateTime(attribute='pub_time')
    user_douban = fields.Nested(DoubanUserSerializer)

