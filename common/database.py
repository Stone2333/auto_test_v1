#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : database.py
 @Project  : rd3-test-automation
"""

import cx_Oracle
import pymysql


class OracleDB(object):
    """oracle 数据库"""

    def __init__(self, host, username, password):
        self.db = cx_Oracle.connect(
            f'{username}/{password}@{host}/ORCL', encoding="UTF-8", nencoding="UTF-8")
        self.curson = self.db.cursor()

    def select(self, sql):
        self.curson.execute(sql)
        # 取一行
        results = self.curson.fetchone()
        return results

    def select_all(self, sql):
        self.curson.execute(sql)
        # 取多行
        results = self.curson.fetchall()
        return results

    def excute(self, sql):
        try:
            self.curson.execute(sql)
            self.db.commit()
        except BaseException:
            self.db.rollback()

    def close(self):
        self.curson.close()
        self.db.close()


class MysqlDB(object):
    """mysql 数据库"""

    def __init__(self, host, username, password, port, database):
        self.db = pymysql.connect(
            host=host,
            user=username,
            password=password,
            port=port,
            db=database)
        self.cursor = self.db.cursor()

    def select(self, sql):
        self.db.ping(reconnect=True)
        self.cursor.execute(sql)
        self.db.commit()
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        try:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
        except BaseException:
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()
