# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from CommomUtil.Request import Request
from CommomUtil.clear_log import *
from CommomUtil.write_log import *
import time
import unittest

class AutoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.flog = 1
        Clear_log()
        print("自动化接口测试开始。。。\n")
        WriteLog.log_info("自动化接口测试开始。。。")

    @classmethod
    def tearDownClass(cls):
        print('自动化接口测试结束！\n')

    def setUp(self):
        f = os.path.split(self.jsonfile)[1]
        print(f)
        t = f[:-5]  # log名称
        print(t)
        print("setUp,相关接口测试开始！\n")
        WriteLog.log_info("访客统计（Stat_Visitors）相关接口测试开始！")




    #访客统计-接口
    def test_001_StatVisitors(self):
        print("1")
        WriteLog.log_info("访客统计（Stat_Visitors）相关接口测试开始！")
        jsonfile = "Stat_Visitors.json"
        excelfile = "Stat_Visitors.xls"
        a = Request(jsonfile, excelfile,'prod')
        a.run()
        WriteLog.log_info("访客统计（Stat_Visitors）相关接口测试结束！")

    #群体画像-接口
    def test_002_GroupPortrait(self):
        print("2")
        WriteLog.log_info("群体画像（Group_Portrait）相关接口测试开始！")
        jsonfile = "Group_Portrait.json"
        excelfile = "Group_Portrait.xls"
        a = Request(jsonfile, excelfile,'prod')
        a.run()
        WriteLog.log_info("群体画像（Group_Portrait）相关接口测试结束！")

    #门店画像-接口
    def test_003_ShopPortrait(self):
        print("3")
        WriteLog.log_info("门店画像（Shop_Portrait）相关接口测试开始！")
        jsonfile = "Shop_Portrait.json"
        excelfile = "Shop_Portrait.xls"
        a = Request(jsonfile, excelfile, 'prod')
        a.run()
        WriteLog.log_info("门店画像（Shop_Portrait）相关接口测试结束！")

    #人脸会员-接口
    def test_004_ShowVisitors(self):
        print("4")
        WriteLog.log_info("人脸会员（Show_Visitors）相关接口测试开始！")
        jsonfile = "Show_Visitors.json"
        excelfile = "Show_Visitors.xls"
        a = Request(jsonfile, excelfile, 'prod')
        a.run()
        WriteLog.log_info("人脸会员（Show_Visitors）相关接口测试结束！")

    #RFM分析-接口
    def test_005_RfmAnalysis(self):
        print("5")
        WriteLog.log_info("RFM分析（Rfm_Analysis）相关接口测试开始！")
        jsonfile = "Rfm_Analysis.json"
        excelfile = "Rfm_Analysis.xls"
        a = Request(jsonfile, excelfile, 'prod')
        a.run()
        WriteLog.log_info("RFM分析（Rfm_Analysis）相关接口测试结束！")

    #门店简报-接口
    def test_006_ShopBulletin(self):
        print("6")
        WriteLog.log_info("门店简报（Shop_Bulletin）相关接口测试开始！")
        jsonfile = "Shop_Bulletin.json"
        excelfile = "Shop_Bulletin.xls"
        a = Request(jsonfile, excelfile, 'prod')
        a.run()
        WriteLog.log_info("门店简报（Shop_Bulletin）相关接口测试结束！")

    def tearDown(self):
        print("tearDown相关接口测试结束！\n")
        WriteLog.log_info("相关接口测试结束！")



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase_01('testThird_01'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(TestCase_01('testSecond_01'))
    suite.addTest(TestCase_01('testFirst_01'))
    unittest.TextTestRunner().run(suite)
    # flog = 1
    # Clear_log()
    # print("自动化接口测试开始。。。")
    # WriteLog.log_info("自动化接口测试开始。。。")
    # while flog :
    #     WriteLog.log_info("第"+ str(flog) +"次循环开始。。。")
    #     StatVisitors()
    #     GroupPortrait()
    #     ShopPortrait()
    #     ShowVisitors()
    #     RfmAnalysis()
    #     ShopBulletin()
    #     WriteLog.log_info("第" + str(flog) + "次循环结束。。。")
    #     flog = flog + 1
    #     time.sleep(600)

