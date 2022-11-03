#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/11/3 10:00
 @File     : tools.py
 @Project  : rd3-test-automation
"""

import requests
import muggle_ocr


"""
使用预置模型，预置模型包含了[ModelType.OCR, ModelType.Captcha] 两种
其中 ModelType.OCR 用于识别普通印刷文本, ModelType.Captcha 用于识别4-6位简单英数验证码

"""


def get_coed_image():
    """
    获取图片地址

    """
    r = requests.get(f'图片url地址', stream=True)
    headers = r.headers
    with open(r'图片路径', 'wb') as f:
        f.write(r.content)
    return headers


def get_code_txt():
    """
    识别图片内容

    """
    with open(r"图片路径", "rb") as f:
        captcha_bytes = f.read()
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    text = sdk.predict(image_bytes=captcha_bytes)
    print(text)
    return text



"""
# 打开印刷文本图片
# with open(r"1.png", "rb") as f:
#     ocr_bytes = f.read()

# 打开验证码图片
# with open(r"1.png", "rb") as f:
#     captcha_bytes = f.read()

# 2. 初始化；model_type 可选: [ModelType.OCR, ModelType.Captcha]
# sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)

# ModelType.Captcha 可识别光学印刷文本
# for i in range(5):
#     st = time.time()
#     # 3. 调用预测函数
#     text = sdk.predict(image_bytes=ocr_bytes)
#     print(text, time.time() - st)

# ModelType.Captcha 可识别4-6位验证码


使用自定义模型
支持基于 https://github.com/kerlomz/captcha_trainer 框架训练的模型
训练完成后，进入导出编译模型的[out]路径下, 把[graph]路径下的pb模型和[model]下的yaml配置文件放到同一路径下。
将 conf_path 参数指定为 yaml配置文件 的绝对或项目相对路径即可，其他步骤一致，如下示例：

"""