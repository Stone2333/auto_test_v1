#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : login.py
 @Project  : rd3-test-automation
"""

import pytest
import allure

from business import public
from config import setting
from common import tool, query


@allure.feature('登录')
class TestLogin:
    data = tool.read_yaml(f'{setting.Config.data_path}\\login.yaml')

    @pytest.mark.parametrize('account, password, captcha, expect',
                             data['project'])
    @allure.title('pc登录')
    def test_qy_login(self, account, password, captcha, expect):
        response_data = public.login(account['account'], password['password'],captcha['captcha'])[0]
        assert response_data['code'] == expect['code']
        assert response_data['msg'] == expect['msg']

