# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import Response
from flask import request
from flask import render_template

from ..user import Device
from ..user import BindUser
from ..shai import Post
from ..utils import jsonify

from datetime import datetime

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/geteid', methods=['GET'])
def getuid():
    try:
        eid = Device.gen_eid()
        return jsonify(ret = 0,
                    errcode = '0100',
                    errmsg='',
                    data = {'eid' : eid} )
    except Exception, e:
        return jsonify(ret = -1,
                    errcode = '0101',
                    errmsg = 'connect mysql server failed')


@api.route('/bind', methods=['POST'])
def bind():
    eid = request.form.get('eid')
    uid = request.form.get('uid')
    name = request.form.get('name')
    avatar = request.form.get('avatar') 
    alt = request.form.get('alt')
    create_time = request.form.get('create_time')
    loc_id = request.form.get('loc_id')
    loc_name = request.form.get('loc_name')

    if not eid or not uid or not name or not avatar or not alt:
        return jsonify(ret = -1, 
                errcode = '0201',
                errmsg = 'eid, uid, name, avatar or alt is none')
    try:
        BindUser.add(eid, uid, name, avatar, alt, create_time, loc_id, loc_name)
        return jsonify(ret = 0,
                    errcode = '0200',
                    errmgs = '') 
    except Exception, e:
        return jsonify(ret = -1,
                    errcode = '0202',
                    errmsg = 'connect mysql server failed')


@api.route('/shai', methods=['POST'])
def shai():
    uid = request.form.get('uid')
    content = request.form.get('content')
    image = request.files.get('image')
    if not uid or not content or not image:
        return jsonify(ret = -1, 
                    errcode = '0301', 
                    errmsg = 'uid, content or image is null')
    
    try:
        Post.add(uid, content, '1111', '222')
        return jsonify(ret = 0,
                    errcode = '0300',
                    errmgs = '') 
    except Exception, e:
        print e
        return jsonify(ret = -1,
                    errcode = '0302',
                    errmsg = 'connect mysql server failed')


@api.route('/latest', methods=['GET'])
def latest():
    eid = int(request.args.get('eid', -1))
    max_id = int(request.args.get('max_id', 0))
    count = int(request.args.get('count', 20))
    gender = int(request.args.get('gender', 0))
    posts = Post.get_latest(max_id, count)
    data = []
    for post in posts:
        print post.uid, post.content, post.image_id, post.small_image_id
        print '1' * 60
        #user_douban = BindUser.get_by_uid(post.uid)
        #post.user_douban = user_douban
        #if user_douban:
        data.append(post)
    return jsonify(ret = 0,
                errcode = '0400',
                data = data)







