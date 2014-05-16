# -*- coding: utf-8 -*-

from flask import Blueprint
from .models import UserId


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/', methods=['GET'])
def index():
    return UserId.gen_user_id()
