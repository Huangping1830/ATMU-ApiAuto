#coding:utf-8

import time
import datetime

def getYesterday():
    # 先获得时间数组格式的日期
    now_time = datetime.datetime.now()
    today = datetime.date.today()
    twoDayAgo = (datetime.datetime.now() - datetime.timedelta(days=2)).date()
    # 转换为时间戳
    # timeStamp = int(time.mktime(twoDayAgo.timetuple()))
    # 转换为其他字符串格式
    esStyleTime_twoDayAgo = twoDayAgo.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    esStyleTime_yesterday = yesterday.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return esStyleTime_twoDayAgo,esStyleTime_yesterday


