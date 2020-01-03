#coding:utf-8
import MySQLdb
import MySQLdb.cursors
import json

class MysqlSearch(object):
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host = '192.168.56.101',
                port = 3306,
                user = 'root',
                passwd = '123456',
                db = 'news',
                charset = 'utf8'
                # cursorclass = MySQLdb.cursors.DictCursor
                )
        except MySQLdb.Error as e:
            print ("Error %d:%s"%(e.args[0],e.args[1]))

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    #查询一条数据
    def search_one(self):
        #准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        #找到cursor
        cur = self.conn.cursor()
        #执行SQL
        cur.execute(sql, ('百家',))  # 向sql里传
        # print(dir(cur))
        # print(cur.description)
        #拿到结果
        result = dict(zip([k[0] for k in cur.description],cur.fetchone()))
        #处理数据
        # print(result)
        # print(result['title'])
        #关闭cursor/链接
        cur.close()
        self.close_conn()
        # result = json.dumps(result)
        return result

    #查询多条数据
    def search_more(self):
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cur = self.conn.cursor()
        # 执行SQL
        cur.execute(sql, ('推荐',))  # 向sql里传
        # print(dir(cur))
        # print(cur.description)
        # 拿到结果
        result = [dict(zip([k[0] for k in cur.description], row)) for row in cur.fetchall()]
        # 处理数据
        # print(result)
        # print(result['title'])
        # 关闭cursor/链接
        cur.close()
        self.close_conn()
        # result = json.dumps(result)
        return result

    #分页查询
    def search_more_by_page(self,page,page_size):
        offset = (page - 1) * page_size
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC LIMIT %s,%s;'
        # 找到cursor
        cur = self.conn.cursor()
        # 执行SQL
        cur.execute(sql,('推荐',offset,page_size))  # 向sql里传
        # print(dir(cur))
        # print(cur.description)
        # 拿到结果；zip：压缩的意思；dict：转化为字典类型
        result =[dict(zip([k[0] for k in cur.description], row)) for row in cur.fetchall()]
        # 处理数据
        # print(result)
        # print(result['title'])
        # 关闭cursor/链接
        cur.close()
        self.close_conn()
        # result = json.dumps(result)
        return result

    def add_one(self):
        try:
            #准备SQL
            sql=(
                "INSERT INTO `news`(`title`,`image`,`content`,`types`,`is_valid`) VALUE"
                "(%s,%s,%s,%s,%s);"
            )
            #获取链接和cursor
            cur = self.conn.cursor()
            #执行sql
            # 提交数据到数据库
            cur.execute(sql,('标题2','/static/img/news/02.png','新闻内容2','推荐',1))
            cur.execute(sql,('标题3','/static/img/news/03.png','新闻内容3','推荐',1))
            #提交事务,若不提交，则数据库不会保存数据，但是会占用id,
            self.conn.commit()
            #关闭cursor和链接
            cur.close()
            self.close_conn()
        except :
            print('error')
            self.conn.rollback()  #回滚，不提交成功

        self.close_conn()


def main():
    op_mysql = MysqlSearch()

    # rest = op_mysql.search_one()
    # print(rest['title'])

    # res = op_mysql.search_more()
    # for item in res:
    #     print(item)
    #     print('----------------')

    op_mysql.add_one()


if __name__ =="__main__":
    main()

