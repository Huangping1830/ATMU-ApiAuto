# -*- coding: utf-8 -*-


from CommomUtil.operation_excel import OperationExcel
from CommomUtil.operation_json import OperationJson
from CommomUtil.send_email import SendEmail
from CommomUtil.write_log import *
from Params.get_header import GetHeader
from config.read_conf import get_conf
from config.get_excel_data import GetExcelData
from path_dir import *
from urllib import parse
import requests
import json



class Request(object):
    def __init__(self,json_file,excel_file,oper_environment):
        self.json_file_path = data_dir + json_file
        self.excel_file_path = data_dir + excel_file
        self.OperJson = OperationJson(self.json_file_path)
        self.OperExcel = OperationExcel(self.excel_file_path)
        self.GetExcelData = GetExcelData(self.excel_file_path)
        self.sendmail = SendEmail()
        self.api = get_conf("apiConfig")
        self.op_en=oper_environment
        self.header = GetHeader()

    #通过获取关键字拿到data数据
    def get_data_from_json(self,row):
        id = self.GetExcelData.get_request_data(row)
        request_data = self.OperJson.get_data(id)
        return request_data

    def go_on_run(self,key):
        if self.op_en == "test":
            url = self.api['test_tmanai']+ self.GetExcelData.get_request_url(key)
            data = self.get_data_from_json(key)['test_body']
            header = self.GetExcelData.is_header(key,self.op_en)
        elif self.op_en == "prod":
            url = self.api['cloud_tmanai']+ self.GetExcelData.get_request_url(key)
            data = self.get_data_from_json(key)['pro_body']
            header = self.GetExcelData.is_header(key, self.op_en)
        else:
            log_error("Operation environment doesn't exist! Please input 'test' or 'prod'!")
        method = self.GetExcelData.get_request_method(key)
        if method == "POST":
            json_data = json.dumps(data, ensure_ascii=False)
            r = requests.post(url,data=json_data,headers=header)
        elif method == "GET":
            url_data = parse.urlencode(data)
            url_data = url_data.replace('%27', "%22")
            r = requests.get(url=url,params=url_data,headers=header)
        try:
            assert r.status_code == 200
            log_done("url="+url)
            log_done("response=" +r.text)
        except:
            log_error("url="+url + " run error!")
            self.sendmail.send_main(url=url,text=r.text)
            time.sleep(100)


    def run(self):
        CaseNum = self.GetExcelData.get_case_lines()
        key=1
        while key < CaseNum:
            self.go_on_run(key)
            key +=1


if __name__ == "__main__":
    # jsonfile = "Stat_Visitors.json"
    # excelfile = "Stat_Visitors.xls"
    # jsonfile = "Group_Portrait.json"
    # excelfile = "Group_Portrait.xls"
    # jsonfile = "Shop_Portrait.json"
    # excelfile = "Shop_Portrait.xls"
    # jsonfile = "Show_Visitors.json"
    # excelfile = "Show_Visitors.xls"
    jsonfile = "Rfm_Analysis.json"
    excelfile = "Rfm_Analysis.xls"
    a = Request(jsonfile,excelfile,"prod")
    # a.go_on_run(1)
    a.run()
