# -*- coding: utf-8 -*-
import sys
import logging     #输出运行日志
from path_dir import *


class ConfigLog(object):
    @classmethod
    def setUp(cls):
        """执行用例开始时初始化,这里面应该有初始化，
        比如logger， 比如db，这样你继承它的case，
        都可以在自己的setUp里执行base的setUp
        """
        log_path = os.path.join(log_dir, '{}.log'.format(cls.__name__))
        cls.logger = cls.add_logger(log_name=cls.__name__, log_file_path=log_path,
                                    log_level=logging.INFO)
        # cls.apitool = ApiTools()
        cls.dict1 = {}

    @staticmethod
    def add_logger(log_name, log_file_path, log_level):
        # 创建一个logging
        logger = logging.getLogger(log_name)
        #log消息级别：debug、info、warning、error和critical
        logger.setLevel(log_level)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_file_path)
        fh.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        return logger

    def log_cur_name(self):
        return str(sys._getframe().f_back.f_code.co_name) #获取当前函数的函数名

    def tearDown(self):
        """执行用例结束时初始化"""
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")