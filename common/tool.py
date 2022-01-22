# -*- coding=utf-8 -*-
import os
import time
from datetime import datetime

import chardet
import base64
import arrow
import yaml
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

from common import log
from common import sm4


logger = log.FrameLog()


def get_file_name(file_path: str):
    """
    获取路径下文件名称

    :param file_path: 文件路径
    :return: 路径列表
    """
    files = None
    for root, dirs, files in os.walk(file_path):
        # print('root_dir:', root)  # 当前目录路径
        # print('sub_dirs:', dirs)   # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件
    return files


def crack_pwd(string: str) -> str:
    """
    前端密码加密方法

    :param string: 明码密码
    :return: 加密密码
    """
    key = """-----BEGIN PUBLIC KEY-----
真实的key
-----END PUBLIC KEY-----"""
    # 注意上述key的格式
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    cipher_text = base64.b64encode(cipher.encrypt(
        string.encode(encoding="utf-8")))  # 对传递进来的用户名或密码字符串加密
    value = cipher_text.decode('utf8')  # 将加密获取到的bytes类型密文解码成str类型
    return value


def get_time_stamp() -> int:
    """
    获取当前时间戳13位

    :return: 时间戳
    """
    time_stamp = int(time.time() * 1000)
    return time_stamp


def get_last_month() -> str:
    """
    获取上一个月 年月

    :return: 上个月的年月 YYYYMM
    """
    now_time = arrow.now()
    last_month = now_time.shift(months=-1).format("YYYYMM")
    return last_month


def get_now() -> str:
    """
    获取当前年月日

    :return: 当前年月日
    """
    now_time = datetime.now().strftime('%Y-%m-%d')
    return now_time


def read_yaml(yaml_path: str) -> dict:
    """
    读取yaml文件

    :param yaml_path: yaml文件路径
    :return: json格式文件
    """

    if not os.path.isfile(yaml_path):
        raise FileNotFoundError('文件路径不存在')
    f = open(yaml_path, 'r', encoding='utf-8')
    cfg = f.read()
    dic = yaml.load(cfg, Loader=yaml.FullLoader)
    return dic

