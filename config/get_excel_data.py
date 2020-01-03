#coding:utf-8
'''
功能：封装从Excel文件中获取接口数据
'''

from CommomUtil.operation_excel import OperationExcel
from CommomUtil.write_log import *
from Params.get_header import GetHeader
from config import data_config


class GetExcelData:
    def __init__(self,file_path):
        self.file_path = file_path
        self.opera_excel = OperationExcel(self.file_path)
        self.header = GetHeader()

    #去获取Excel的行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None   #加个标识，显得语言高级
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #是否携带header
    def is_header(self,row,oper_envir):
        col =int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row,col)
        if header == "yes":
            return self.header.get_default_header(oper_envir)
        else:
            log_warn("接口不含header!")
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_method())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    #获取url
    def get_request_url(self,row):
        col =int(data_config.get_path())
        request_url = self.opera_excel.get_cell_value(row,col)
        return request_url

    #获取请求数据关键字
    def get_request_data(self,row):
        col = int(data_config.get_data())
        key = self.opera_excel.get_cell_value(row,col)
        if key == '':
            log_warn('no request data key!')
            return None
        return key



    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            log_warn('no expect result!')
            return None
        else:
            return expect

    def write_result(self,row,value):
        col = int(data_config.get_result())
        result = self.opera_excel.write_value(row,col,value)
        return result

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depent_key = self.opera_excel.get_cell_value(row,col)
        if depent_key == "":
            log_warn('no depent key!')
            return None
        else:
            return depent_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_field_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == '':
            log_warn('no depend case id!')
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_field_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        else:
            return data
