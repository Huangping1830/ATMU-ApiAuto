# coding:utf-8
import xlrd
from xlutils.copy import copy
'''
功能：重构操作Excel函数
'''
class OperationExcel:
    def __init__(self,file_path=None,sheet_id=0):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path ="../data/Stat_Visitors.xls"
        self.sheet_id = sheet_id
        self.data = self.get_data()

     #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_path,encoding_override='utf-8')
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        tables = self.data
        unit = tables.cell_value(int(row),int(col))
        # print unit
        return unit

    #写入数据
    def write_value(self,row,col,value):
        '''
        写入Excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        read_data = xlrd.open_workbook(self.file_path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_path)

    #根据对应的caseid找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    #根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num +1

    #根据行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id !=None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == "__main__":
    sheet_id = 0
    opers = OperationExcel(sheet_id)
    tables =opers.get_data()
    row = tables.nrows
    col =tables.ncols
    print(opers.get_cell_value(1,2))
    print(row,col)

