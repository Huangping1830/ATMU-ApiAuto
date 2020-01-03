#coding:utf-8
import MySQLdb
import json


class OperationMysql:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(
                host = '154.8.170.133',
                port = 22,
                user = 'root',
                passwd = 'Hup!!2019',
                db = 'user',
                charset = 'utf-8',
                cursorclass = MySQLdb.cursors.DictCursor
                )
        except MySQLdb.Error as e:
            print ("Error %d:%s"%(e.args[0],e.args[1]))
        self.cur = self.conn.cursor()

    #查询数据
    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

if __name__ =="__main__":

    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from web_user where Name = 'huangping '")
    print(res)

