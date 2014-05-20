# -*- coding: utf-8 -*-

from flask import Blueprint
from .models import Device


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/', methods=['GET'])
def index():
    return Device.gen_eid()
