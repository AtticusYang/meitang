# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request

from .models import Online
from .models import FeedBack

from ..utils import jsonify

manage = Blueprint('manage', __name__, url_prefix='/v1/manage')

@manage.route('/adstatus', methods=['GET'])
def adstatus():
    return jsonify(ret = 0,
                errcode = '0600',
                errmsg = '',
                data = {'adlevel1': 'off',
                    'adlevel2': 'off',
                    'adlevel3': 'off'
                })


@manage.route('/online', methods=['POST'])
def online():
    eid = request.form.get('eid')
    client_name = request.form.get('client_name')
    client_version = request.form.get('client_version')
    status = request.form.get('status')
    uid = request.form.get('uid')
    name = request.form.get('name')

    if not eid or not client_name or not client_version or not status:
        return jsonify(ret = -1,
                errcode = '0701',
                errmgs = 'eid, client_name, client_version or status is null')
    try:
        Online.add(eid, client_name, client_version, status, uid, name)
        return jsonify(ret = 0,
                    errcode = '0700',
                    errmsg = '')
    except Exception, e:
        return jsonify(ret = -1,
                    errcode = '0702',
                    errmsg = 'connect database server failed')




@manage.route('/feedback', methods=['POST'])
def feedback():
    eid = request.form.get('eid')
    content = reqeust.form.get('content')
    uid = request.form.get('uid')
    name = request.form.get('name')
    client_name = request.form.get('client_name')
    client_version = request.form.get('client_version')
    contact = request.form.get('contact')

    if not eid or not content:
        return jsonify(ret = -1,
                errcode = '0801',
                errmgs = 'eid or content is null')


    try:
        FeedBack.add(eid, content, uid, name, client_name, client_version, contact)
        return jsonify(ret = 0,
                    errcode = '0800',
                    errmsg = '')
    except Exception, e:
        return jsonify(ret = -1,
                    errcode = '0802',
                    errmsg = 'connect database server failed')

