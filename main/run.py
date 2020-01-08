# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from CommomUtil.Request import Request
from CommomUtil.clear_log import *
from CommomUtil.write_log import *
import time
import pytest

#访客统计-接口
def StatVisitors():
    WriteLog.log_info("访客统计（Stat_Visitors）相关接口测试开始！")
    jsonfile = "Stat_Visitors.json"
    excelfile = "Stat_Visitors.xls"
    a = Request(jsonfile, excelfile,'prod')
    a.run()
    WriteLog.log_info("访客统计（Stat_Visitors）相关接口测试结束！")

#群体画像-接口
def GroupPortrait():
    WriteLog.log_info("群体画像（Group_Portrait）相关接口测试开始！")
    jsonfile = "Group_Portrait.json"
    excelfile = "Group_Portrait.xls"
    a = Request(jsonfile, excelfile,'prod')
    a.run()
    WriteLog.log_info("群体画像（Group_Portrait）相关接口测试结束！")

#门店画像-接口
def ShopPortrait():
    WriteLog.log_info("门店画像（Shop_Portrait）相关接口测试开始！")
    jsonfile = "Shop_Portrait.json"
    excelfile = "Shop_Portrait.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()
    WriteLog.log_info("门店画像（Shop_Portrait）相关接口测试结束！")

#人脸会员-接口
def ShowVisitors():
    WriteLog.log_info("人脸会员（Show_Visitors）相关接口测试开始！")
    jsonfile = "Show_Visitors.json"
    excelfile = "Show_Visitors.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()
    WriteLog.log_info("人脸会员（Show_Visitors）相关接口测试结束！")

#RFM分析-接口
def RfmAnalysis():
    WriteLog.log_info("RFM分析（Rfm_Analysis）相关接口测试开始！")
    jsonfile = "Rfm_Analysis.json"
    excelfile = "Rfm_Analysis.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()
    WriteLog.log_info("RFM分析（Rfm_Analysis）相关接口测试结束！")

#门店简报-接口
def ShopBulletin():
    WriteLog.log_info("门店简报（Shop_Bulletin）相关接口测试开始！")
    jsonfile = "Shop_Bulletin.json"
    excelfile = "Shop_Bulletin.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()
    WriteLog.log_info("门店简报（Shop_Bulletin）相关接口测试结束！")

if __name__ == "__main__":
    flog = 1
    Clear_log()
    print("自动化接口测试开始。。。")
    WriteLog.log_info("自动化接口测试开始。。。")
    while flog :
        WriteLog.log_info("第"+ str(flog) +"次循环开始。。。")
        StatVisitors()
        GroupPortrait()
        ShopPortrait()
        ShowVisitors()
        RfmAnalysis()
        ShopBulletin()
        WriteLog.log_info("第" + str(flog) + "次循环结束。。。")
        flog = flog + 1
        time.sleep(600)

