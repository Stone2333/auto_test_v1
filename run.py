# -*- coding=utf-8 -*-
import pytest
from config import setting
import os
import datetime


if __name__ == '__main__':
    # pytest.main([setting.Config.case_path, '-v', '--html={}\\test.html'.format(setting.Config.report_path), '--self-contained-html'])
    # 获取当前时间
    time = datetime.datetime.now().strftime('%Y-%m-%d=%H-%M-%S')
    # 拼接路径
    path = r'{}\{}'.format(setting.Config.report_path, time)
    pytest.main(['testcases', '-v', '--alluredir={}'.format(path)])
    # os.system(d)
    html_path = setting.Config.html_path
    # 根据测试报告数据生成html
    os.popen("allure generate {} -o {} --clean".format(path, html_path))
    # 远程打开html并启动web服务
    os.popen("allure open -h 127.0.0.1 -p 8085 {}".format(html_path))