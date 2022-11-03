#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : tools.py
 @Project  : rd3-test-automation
"""

import os


class Config:

    # 项目路径
    root_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    # 测试数据路径
    data_path = os.path.join(root_path, 'casesdata')
    # 测试用例路径
    case_path = os.path.join(root_path, 'testcases')
    # 测试报告路径
    report_path = os.path.join(root_path, 'testreport')
    # 配置路径
    config_path = os.path.join(root_path, 'config')
    # 测试报告html路径
    html_path = os.path.join(root_path, 'testreport', 'html')
    # 通用方法路径
    common_path = os.path.join(root_path, 'common')
    # 日志路径
    logs_path = os.path.join(root_path, 'logs')
    # 文件下载路径
    export_path = 'D:/export'
    # 文件上传路径
    upload_path = 'D:/file_upload'
    # 台账上传路径


class DevConfig(Config):
    # 项目的host
    host = '127.0.0.1:80'
    # 数据库hots
    dbhost = '127.0.0.1:3360'
    # 数据库账号
    username = 'root'
    # 数据库密码
    password = '123456'
