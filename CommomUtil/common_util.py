#coding:utf-8

class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串当中
        判断预期结果是否正确
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        '''
        flag=None
        #print(type(str_one))
        #print type(str_two)
        #print isinstance(str_one,unicode),isinstance(str_two,unicode)
        if isinstance(str_one,str):
            #str_one =str_one.encode('unicode-escape').decode('str_escape')
            str_one = str_one.encode('utf-8')
        if isinstance(str_two,str):
            str_two = str_two.encode('utf-8')
        if str_two is not None and str_one in str_two:
            flag =True
        else:
            flag=False
        return flag

if __name__ == '__main__':
    con_str = CommonUtil()
    str_1 = "I'm huangping.How are you ?"
    str_2 = 'are'
    res = con_str.is_contain(str_2,str_1)
    print(res)
