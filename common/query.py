#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : query.py
 @Project  : rd3-test-automation
"""

from common import database, log
from config import setting

logger = log.FrameLog()


def db():
    """
    数据库对象

    :return: 数据库对象
    """
    d = database.OracleDB(
        username=setting.DevConfig.username,
        password=setting.DevConfig.password,
        host=setting.DevConfig.dbhost)
    return d

