# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import render_template

from ..user import UserId
from ..shai import Post


api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/getuid', methods=['GET'])
def getuid():
    new_user_id = UserId.gen_user_id()
    return jsonify(ret = 0,
                errcode = '0100',
                errmsg = '',
                data = {
                    'uid' : new_user_id
                    }
            )


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
        return  '1111111111111111111'





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
    try:
        uid = int(request.args.get('eid'))
    except:
        return jsonify(ret = -1,
                    errcode = '0301',
                    errmsg = 'uid is null'
                )

        cur_shai_id = int(request.args.get('cur_shai_id', 0))
        dobuan_id = int(request.args.get('douban_id', 0))
        count = int(request.args.get('count', 20))
        gender = int(request.args.get('gender', 0))
        posts = Post.get_latest(cur_shai_id, count)
        doubaners = DoubanUser.get_by_ids()

        return '11111111111'




