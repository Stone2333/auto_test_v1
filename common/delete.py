# -*- coding=utf-8 -*-

from common import DB, log
from config import setting

logger = log.FrameLog()


def db():
    """
    数据库对象

    :return:数据库对象
    """
    d = DB.OracleDB(
        username=setting.DevConfig.username,
        password=setting.DevConfig.password,
        host=setting.DevConfig.dbhost)
    return d

