#coding:utf-8
import json
from path_dir import *
'''
重构json工具类
'''
class OperationJson:
    def __init__(self,json_file_path):
        self.json_file_path = json_file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        #防止文件打开后，忘记关闭，with..as 会自动关闭文件！！！
        with open(self.json_file_path) as fp:
            data = json.load(fp)   #加载json文件
            return data

    #根据关键字获取数据
    def get_data(self,id):
        key = str(id)
        return self.data[key]

if __name__ =='__main__':
    file = data_dir + "Stat_Visitors.json"
    opjson = OperationJson(file)
    print("read_data",opjson.read_data())
    print(opjson.get_data('getdata_number'))




