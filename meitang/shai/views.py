# -*- coding: utf-8 -*-

from flask import Blueprint


shai = Blueprint('shai', __name__, url_prefix='')


@shai.route('/', methods=['GET'])
def index():
    return 'welcome to dadanshai'
