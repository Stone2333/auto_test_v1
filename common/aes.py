# -*- coding=utf-8 -*-

import base64

from Crypto.Cipher import AES


# 密钥（key）, 密斯偏移量（iv） CBC模式加密

BLOCK_SIZE = 16  # Bytes


def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
        chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s): return s[:-ord(s[len(s) - 1:])]


vi = '7B4368CD0CFFE0B8'


def AES_Encrypt(key, data):
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf8')
    return enctext


def AES_Decrypt(key, data):
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
    enctext = AES_Encrypt(key, data)
    print(enctext)
    AES_Decrypt(key, enctext)
