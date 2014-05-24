# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from beansdb_client import Beansdb

cfg = {
    "localhost:7900": range(16),
}
beansdb = Beansdb(cfg, 16)
