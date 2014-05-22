# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import Response
from flask import jsonify
from flask import request
from flask import render_template

from ..user import Device
from ..user import BindUser
from ..shai import Post

import json


api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/geteid', methods=['GET'])
def getuid():
    eid = Device.gen_eid()
    data = {'ret' : 0,
            'errcode' : '0',
            'errmsg' : '',
            'data' : {
                'eid' : eid,
            }
        }
    return Response(json.dumps(data, ensure_ascii=False), \
            content_type='application/json; charset=utf-8')



@api.route('/bind', methods=['GET', 'POST'])
def bind():
    if request.method == 'GET':
        return render_template('api/bind.html')
    else:
        try:
            eid = request.form['eid']
            uid = request.form['uid']
            alt = request.form['alt']
            avatar = request.form['avatar']
            create_time = request.form['create_time']
            loc_id = request.form['loc_id']
            loc_name = request.form['loc_name']
        except:
            return jsonify(ret = -1,
                        errcode = '0301',
                        errmsg = 'eid, uid, alt, avatar, create_time, loc_id, loc_name should not be null'
                    )
        bind_user = BindUser(eid, uid, alt, avatar, create_time, loc_id, loc_name)
        BindUser.add(bind_user)





@api.route('/shai', methods=['GET', 'POST'])
def shai():
    if request.method == 'GET':
        return render_template('api/shai.html')
    else:
        try:
            uid = request.form['uid']
            douban_id = request.form['douban_id']
            image = request.files['image']
        except:
            return jsonify(ret = -1,
                        errcode = '0201',
                        errmsg = 'uid, douban_id or image is null'
                    )


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

    return '11111111111111111111111'






