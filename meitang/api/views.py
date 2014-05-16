# -*- coding: utf-8 -*-

from flask import Blueprint


api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/getuid', methods=['GET'])
def getuid():
    return 'api, get uid'
