# -*- coding: utf-8 -*-
from CommomUtil.Request import Request
from CommomUtil.clear_log import *
import time

#访客统计-接口
def StatVisitors():
    jsonfile = "Stat_Visitors.json"
    excelfile = "Stat_Visitors.xls"
    a = Request(jsonfile, excelfile,'prod')
    a.run()

def GroupPortrait():
    jsonfile = "Group_Portrait.json"
    excelfile = "Group_Portrait.xls"
    a = Request(jsonfile, excelfile,'prod')
    a.run()

def ShopPortrait():
    jsonfile = "Shop_Portrait.json"
    excelfile = "Shop_Portrait.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()


def ShowVisitors():
    jsonfile = "Show_Visitors.json"
    excelfile = "Show_Visitors.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()

def RfmAnalysis():
    jsonfile = "Rfm_Analysis.json"
    excelfile = "Rfm_Analysis.xls"
    a = Request(jsonfile, excelfile, 'prod')
    a.run()

if __name__ == "__main__":
    flog = 0
    a = get_all_file()
    while flog < 1:
        StatVisitors()
        GroupPortrait()
        ShopPortrait()
        ShowVisitors()
        RfmAnalysis()
        time.sleep(900)

