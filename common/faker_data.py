#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : tools.py
 @Project  : rd3-test-automation
"""

from faker import Faker

fake = Faker(locale='zh_CN')
name = fake.name()
print(name)
sfz = fake.ssn(min_age=18, max_age=90)
print(sfz)
phone = fake.phone_number()
print(phone)




