#coding:utf-8
import json
import time
import os
'''
功能：调查关联率低的原因
检查未关联personid的order，在对应5分钟内是否出现过person
'''
path_root = os.path.dirname(__file__)
data_dir = os.path.join(path_root,"Face2order_data/").replace("\\","/")

class WriteExcel:
    def __init__(self,file_name=None,sheet_id=0):
        if file_name:
            self.file_name = data_dir + file_name
        else:
            self.file_name =data_dir + "Interfacedata.xls"
        self.sheet_id = sheet_id

    #写入数据
    def write_value(self,row,id,order_id=None,order_time=None,person_num=None,person_list=None):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,0,id)
        sheet_data.write(row, 1, order_id)
        sheet_data.write(row, 2, order_time)
        sheet_data.write(row, 3, person_num)
        sheet_data.write(row, 4, person_list)
        write_data.save(self.file_name)

class OperationJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path =data_dir + 'login.json'
        else:
            self.file_path = data_dir + file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        #防止文件打开后，忘记关闭，with..as 会自动关闭文件！！！
        with open(self.file_path) as fp:
            data = json.load(fp)   #加载json文件
            return data

    #根据关键字获取数据
    def get_data(self,id):
        key = str(id)
        #print self.data[key]
        return self.data[key]


if __name__ =='__main__':
    face = OperationJson('faces.json')
    order = OperationJson('orders.json')
    opers = WriteExcel('order-person.xls')
    result_face = face.get_data('RECORDS')
    result_order = order.get_data('RECORDS')
    i=0
    flag = 0
    list_per = []
    while i < len(result_order):
        j = 0
        person_id1 = result_order[i]['person_id']
        if (person_id1 == ''):
            order_id = result_order[i]['order_id']
            order_time = result_order[i]['order_time']
            order_time1 = int(time.mktime(time.strptime(order_time, '%d/%m/%Y %H:%M:%S')))
            flag += 1
            print(i)
            print('order_time=', order_time)
            list_person_id = []
            while j < len(result_face):
                # print('j=',j)
                face_time = result_face[j]['face_time']
                person_id2 = result_face[j]['person_id']
                face_time2 = int(time.mktime(time.strptime(face_time, '%d/%m/%Y %H:%M:%S')))
                if (
                        face_time2 >= order_time1 - 55 and face_time2 <= order_time1 + 1 and person_id2 not in list_person_id):
                    list_person_id.append(person_id2)
                j += 1
            if (i >= 4 and i < len(result_order) - 4 ):
                a = 0
                while a < 9:
                    person_id3 = result_order[i - 4 + a]['person_id']
                    if person_id3 in list_person_id:
                        list_person_id.remove(person_id3)
                    a += 1
            # opers.write_value(flag, id=i, order_id=order_id, order_time=order_time, person_num=len(list_person_id),
            #                   person_list=list_person_id)
            print('person_num=', len(list_person_id), list_person_id)
        # else:
        #     list_per.append(person_id1)
        i += 1











