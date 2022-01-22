# -*- coding=utf-8 -*-
import urllib.parse
import requests
import allure

from common import tool, query
from config import setting
from common import log

logger = log.FrameLog()


@allure.step('登录')
def login(
        account: str,
        password: str,
        captcha: str):
    """
    登录

    :param account: 账号
    :param password: 密码
    :param captcha: 验证码
    :return: 登录成功json和Response对象
    """
    ip = setting.DevConfig.host
    url = f'http://{ip}/login'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    encrypted_password = tool.crack_pwd(str(password))
    data = {
        "username": account,
        "password": encrypted_password,
        "captcha": captcha,
    }
    response = requests.post(headers=headers, url=url, json=data)
    response_data = response.json()
    logger.log().info(f"登录成功，登录信息:{response_data}")
    return response_data, response


if __name__ == '__main__':
    pass
