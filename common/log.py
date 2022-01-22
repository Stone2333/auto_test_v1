import logging
import time
from config import setting

"""
logging 4个组件
1.logger 日志器 提供了应用程序的接口
2.Handler 处理器 通过logger在不同位置输出日志
3.Formator 格式器 决定日志以什么样的样式显示
4.filter 过滤器 过滤器哪些需要记录输出 哪些需要丢弃

一个日志器对应多个处理器
每个处理器有自己的格式器和过滤器

"""


class FrameLog:

    def log(self):
        # 创建一个日志
        logger = logging.getLogger('logger')
        # 设置日志输出最低等级，低于当前等级就会被忽略
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # 创建处理器
            sh = logging.StreamHandler()
            fh = logging.FileHandler(
                filename=f'{setting.Config.logs_path}\{time.strftime("%Y_%m_%d_%H_%M")}_log.log',
                encoding='utf-8')
            # 创建一个格式器
            formator = logging.Formatter(fmt="%(asctime)s %(funcName)s %(levelname)s %(message)s",
                                         datefmt="%Y-%m-%d %X")
            sh.setFormatter(formator)
            fh.setFormatter(formator)
            logger.addHandler(sh)
            logger.addHandler(fh)
            # logger.removeHandler(sh)
            # logger.removeHandler(fh)
        return logger

