#coding=utf-8
from HTMLTestRunner import *
import unittest
from v7jxc_auto.case import test_login_case
from v7jxc_auto.util.server import Server
import time,os,sys,time


filePath = u'C:\\Users\\Administrator\\PycharmProjects\\untitled1\\v7jxc_auto\\report\\Report.html'  # 确定生成报告的路径

def appium_init():
    server = Server()
    server.main()

def get_suite():
    testunit = unittest.defaultTestLoader.discover("../case", pattern="test*.py")

    # try:
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description='APP功能用例测试结果')
    # 运行测试用例
    runner.run((testunit))
    fp.close()
    print("")
    print("----------All Done!-------")
    # except:
    #         print("Error!!!!!!!")

        # unittest.TextTestRunner().run(suite)

appium_init()
time.sleep(8)
get_suite()

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from v7jxc_auto.case.test_login_case import *



f=open(filePath,"rb")
mail_body=f.read()
f.close()

my_sender = '379207614@qq.com'  # 发件人邮箱账号
my_pass = 'syoqrrprjxnfbjee'  # 发件人邮箱密码
my_user = '1354091575@qq.com'  # 收件人邮箱账号，
# 我这边发送给自己
try:
    msg=MIMEText(mail_body,"html","utf-8")
    msg["subject"]=Header("精斗云app登录部分测试用例结果","utf-8")
    msg['From'] = formataddr(["JDY", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["个人测试", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except:
    print("邮件发送失败")