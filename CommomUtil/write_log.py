# -*- coding: utf-8 -*-

import time
from path_dir import *


class WriteLog(object):
    """记录日志工具"""

    run_path = "".join([log_dir, "Run.log"])
    error_path = "".join([log_dir, "Error.log"])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    run_file = open(os.path.abspath(run_path), "a")  #'a'表示打开一个文件追加
    """如果该文件已存在，文件指针将会放在文件的结尾。
    也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。"""
    error_file = open(os.path.abspath(error_path), "a")

    @staticmethod
    def get_now_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @staticmethod
    def _write(write_file, log_type, msg):
        """给对应的日志文件写入日志
        Args：
            write_file(str): 日志文件名称, 是runtime文件还是error文件
        """

        write_file.writelines("".join([WriteLog.get_now_time(), ": [", log_type, "]", msg, '\n']))
        write_file.flush()

    @staticmethod
    def _log(log_type, msg):
        """根据日志类别判断写入对应的日志类别文件
        Args:
            log_type(str): 日志类别，error, warn, pass, done等
            msg(str): 日志信息
        """
        if log_type == "error":
            WriteLog._write(WriteLog.error_file, log_type, msg)
        WriteLog._write(WriteLog.run_file, log_type, msg)

    @staticmethod
    def log_pass(msg):
        WriteLog._log("pass", msg)

    @staticmethod
    def log_done(msg):
        WriteLog._log("done", msg)

    @staticmethod
    def log_warn(msg):
        WriteLog._log("warn", msg)

    @staticmethod
    def log_error(msg):
        WriteLog._log("error", msg)


class TestRunError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self, value):
        return str(self.value)


def log_error(msg):
    WriteLog.log_error(msg)
    # raise TestRunError(msg)


def log_warn(msg):
    WriteLog.log_warn(msg)


def log_done(msg):
    WriteLog.log_done(msg)


def log_pass(msg):
    WriteLog.log_pass(msg)

if __name__ == "__main__":
    log_pass("成功")
    log_error("fail")
