# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import Response
from flask import request
from flask import render_template
#from werzeug import secure_filename

from ..user import Device
from ..user import BindUser
from ..shai import Post
from ..utils import jsonify
from ..utils import allowed_file

from ..extensions import beansdb

from .serializer import PostSerializer

from datetime import datetime
import hashlib

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
    
    filename = image.filename
    if not allowed_file(filename):
        return jsonify(ret = -1, 
                    errcode = '0302', 
                    errmsg = 'not support image type')

    try:
        type = filename.split('.')[1].lower()
        image_name = "%s/%s/%s" %("image", uid, filename)
        image_id = "%s.%s" %(hashlib.md5(_image_name).hexdigest(), type)
        small_image_id = image_id
        data = {'image':image.stream.read(), 'mime':image.mimetype}
        beansdb.set(image_id, data)
        Post.add(uid, content, image_name, small_image_name)
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

    for post in posts:
        user_douban = BindUser.get_by_uid(post.uid)
        post.user_douban = user_douban

    return jsonify(ret = 0,
                errcode = '0400',
                errmsg = '',
                data = {'nextstartpos' : 4,
                    "shais": PostSerializer(posts, many=True).data,})







