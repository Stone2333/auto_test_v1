# * coding:utf-8 *

import os
import time
import random
from aip import AipOcr

path = r"图片路径"

yin_aip = {'APP_ID': '自己的', 'API_KEY': '自己的',
           'SECRET_KEY': '自己的'}
baidu_aip = {'APP_ID': '自己的', 'API_KEY': '自己的',
             'SECRET_KEY': '自己的'}

api_list = [yin_aip, baidu_aip]

dir_list = os.listdir(path)

filepath = path + "/{}"

class BaiduOcr():
    """百度orc"""

    def __init__(self):
        aip = random.choice(api_list)
        self.APP_ID = aip.get('APP_ID')
        self.API_KEY = aip.get('API_KEY')
        self.SECRET_KEY = aip.get('SECRET_KEY')
        self.filepath = path + "/{}"

    def get_orc_client(self):
        return AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def get_file_content(self, dir):
        with open(self.filepath.format(dir), 'rb') as fp:
            return fp.read()

    def get_parse_str(self, dir):
        str = ''
        image = self.get_file_content(dir)
        client = self.get_orc_client()
        if client is None:
            return
        json_result = client.basicGeneral(image)
        result = json_result.get('words_result')
        for item in result:
            str += item.get('words')
        return str


if __name__ == "__main__":
    spider = BaiduOcr()
    for item in dir_list:
        # file_name = filepath.format(item)
        print(item)
        result = spider.get_parse_str(item)
        print(result)
        time.sleep(5)
