#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : conftest.py
 @Project  : rd3-test-automation
"""

import pytest

from common import query, delete
from business import public


def setup_function():
    print('setup_function：每个用例开始前都会执行')


def teardown_function():
    print('teardown_function:每个用例结束后都会执行')


def setup_module():
    print('setup_module整个.py模块开始前只执行一次')


def teardown_module():
    print('teardown_module整个.py模块结束后只执行一次')

