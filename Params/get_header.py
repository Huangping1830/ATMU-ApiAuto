#coding:utf-8

from com.qcloudapigateway.auth import signl
from config.read_conf import get_conf
from CommomUtil.operation_excel import OperationExcel
from path_dir import *

class GetHeader:
    def __init__(self):
        self.secret = get_conf("SecretConfig")

    def test_header_default(self,Oper_envir):
        if Oper_envir == 'test':
            header ={
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "test.tmanai.com",
            "Accept": "text/html, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,ja;q=0.6"
            }
        elif Oper_envir == 'prod':
            header ={
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "cloud.tmanai.com",
            "Accept": "text/html, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,ja;q=0.6"
            }
        return header

    def get_default_header(self,Oper_envir):
        SecretId = self.secret["SecretId"]
        SecretKey= self.secret["SecretKey"]
        Source = self.secret["Source"]
        header= self.test_header_default(Oper_envir)
        sign1,dateTime = signl.getSimpleSign(Source, SecretId, SecretKey)
        header['Authorization'] = sign1
        header['Date'] = dateTime
        header['Source'] = Source
        return header

if __name__ =='__main__':
    a=GetHeader()
    url_address="url1"
    print(a.get_default_header('test'))



