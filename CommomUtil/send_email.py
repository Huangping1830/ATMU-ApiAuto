#coding:utf-8
import smtplib
from email.mime.text import MIMEText
import time
'''
发送邮件 smtplib
邮件格式 

'''
class SendEmail:
    global send_user
    global email_host
    global password
    email_host = 'smtp.163.com'
    send_user = "huangping183@163.com"
    password = 'HP69852087'
    def send_mail(self,user_list,sub,content):#收件人，主题，内容
        user = "huangping" + "<"+ send_user + ">"  #发件人
        message = MIMEText(content,_subtype='plain',_charset='utf-8')  #构建邮件格式
        #连接邮箱服务器
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ';'.join(user_list)  #str.json()
        server = smtplib.SMTP()  #邮件服务器
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,url,text):
        # pass_num = float(len(pass_list))
        # fail_num = float(len(fail_list))
        # count_num = pass_num + fail_num
        # #90%
        # pass_result = "%.2f%%" %(pass_num/count_num*100)#取小数点后两位 + %
        # fail_result = "%.2f%%" %(fail_num/count_num*100)
        user_list = ['pinghuang@tman.ai']
        t = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        sub = '接口测试反馈'
        _url = url
        _text = text
        content ="运行时间："+ t + '\n'+ "出错的接口：" + _url + '\n' + "返回结果：" + _text
        self.send_mail(user_list,sub,content)

if __name__ == '__main__':
    sen = SendEmail()
    pass_list = "123"
    fail_list = "123"
    sen.send_main(pass_list,fail_list)

