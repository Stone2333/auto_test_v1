#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : aes.py
 @Project  : rd3-test-automation
"""

import base64

from Crypto.Cipher import AES


# 密钥（key）, 密斯偏移量（iv） CBC模式加密

# Bytes
BLOCK_SIZE = 16

# 偏移量
vi = '7B4368CD0CFFE0B8'


def pad(s):
    """
    获取真实字符串

    :param s: 字符串
    :return:
    """
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
        chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s):
    """
    获取真实字符串,去掉最后补位的数据

    :param s: 字符串
    :return:
    """
    return s[:-ord(s[len(s) - 1:])]


def aes_encrypt(key, data):
    """
    aes加密

    :param key: 秘钥
    :param data: 数据
    :return: 加密数据
    """
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf8')
    return enctext


def aes_decrypt(key, data):
    """
    aes解密

    :param key: 秘钥
    :param data: 数据
    :return: 解密数据
    """
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    # 将加密数据转换位bytes类型数据
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    # 去补位
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted


if __name__ == '__main__':
    key = '具体的key'
    data = '123456'
    enctext = aes_encrypt(key, data)
    print(enctext)
    aes_decrypt(key, enctext)
