#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : tools.py
 @Project  : rd3-test-automation
"""

import pytest
from config import setting
import os
import datetime


if __name__ == '__main__':
    # pytest.main([setting.Config.case_path, '-v', '--html={}\\test.html'.format(setting.Config.report_path), '--self-contained-html'])
    # 获取当前时间
    time = datetime.datetime.now().strftime('%Y-%m-%d=%H-%M-%S')
    # 拼接路径
    path = rf"{setting.Config.report_path}\{time}"
    pytest.main(["testcases", "-v", f"--alluredir={path}"])
    # os.system(d)
    html_path = setting.Config.html_path
    # 根据测试报告数据生成html
    os.popen(f"allure generate {path} -o {html_path} --clean")
    # 远程打开html并启动web服务
    os.popen(f"allure open -h 127.0.0.1 -p 8085 {html_path}")