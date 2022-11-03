#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : update.py
 @Project  : rd3-test-automation
"""

from common import database
from config import setting


def db():
    """
    数据库对象

    :return:数据库对象
    """
    d = database.OracleDB(
        username=setting.DevConfig.username,
        password=setting.DevConfig.password,
        host=setting.DevConfig.dbhost)
    return d

