#coding:utf-8
import pymysql
from sshtunnel import SSHTunnelForwarder


# 传入实例名和sql，返回查询结果
def SSHMysql(DB, SQL):
    # 配置SSH连接
    server = SSHTunnelForwarder(
        ssh_address_or_host=('188.131.132.174', 22),  # 指定ssh登录的跳转机的address
        ssh_username='root',  # 跳转机的用户
        ssh_password='L70aSp12',  # 跳转机的密码
        local_bind_address=('127.0.0.1', 1268),  # 映射到本机的地址和端口
        remote_bind_address=('172.21.16.18', 3306))  # 数据库的地址和端口
    server.start()  # 启用SSH
    # 数据库账户信息设置
    db = pymysql.connect(
        host="127.0.0.1",  # 映射地址local_bind_address IP
        port=1268,  # 映射地址local_bind_address端口
        user="huangping",
        passwd="HP@12345",
        database= DB,  # 需要连接的实例名
        charset='utf8')

    cursor = db.cursor()
    cursor.execute(SQL.encode('utf8'))  # 执行SQL
    data = cursor.fetchall()  # 获取查询结果

    # 关闭数据库连接
    cursor.close()
    return data


if __name__ == "__main__":
    SQL = "select order_id,person_id,order_time,created_at,receipt_text from orders where device_id='DB866262040107442' and order_time > '2019-06-18 00:00:00' and order_time < '2019-06-19 00:00:00';"
    SelectResult = SSHMysql('tmanv2', SQL)


