import sys
import json
from common.module import excel_module
from config import settings
from common.module import mysql_module
from common.module import request_module
# print(settings.data_path)
filename = 'test_001.xlsx'
file_name = settings.data_path+filename
method = excel_module.ReadExcel(file_name)
# print(type(method))
sheet = method.get_sheet_by_index(2)
# print(method.get_rows(sheet_obj))
print(sheet.name)
# print(method.get_rows(sheet))
data = method.get_cell_value(sheet, 1, 3)
# print(type(data))
# print(data)
# print(json.loads(data))
# print(json.dumps(data))
# conn_data = settings.MYSQL_CONFIG.get('test')
# print(conn_data)
# host = conn_data['host']
# print(host)
# conn = mysql_module.MysqlModule(host=conn_data['host'],
#                                 user=conn_data['user'],
#                                 passwd=conn_data['passwd'],
#                                 port=3306,
#                                 db=conn_data['db_test'])
# sql = 'select * from account'
# res = conn.get_all_data(sql)
# for i in res:
#     print(i)

# url = 'http://127.0.0.1:8081/test/'
# req = request_module.GetResponse(url, 'post')
# res = req.get_response(json.loads(data))
# print(res)

import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
stream = open('../report/2019-04-21-18:51:44Api_Test.html', 'wb')
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# from config.settings import EMAIL_CONFIG
# email_conf = EMAIL_CONFIG
# sender = '815885751@qq.com'
# receiver = '17801093323@163.com'
# message = MIMEText("测试python发送邮件", 'plain', 'utf-8')
# message['From'] = Header('李帅', 'utf-8')
# message['To'] = Header('测试', 'utf-8')
# subject = 'Python Email 测试'
# message['Subject'] = Header(subject, 'utf-8')
# print(email_conf['server'])
# print(email_conf['server_port'])
# try:
#     smtobj = smtplib.SMTP_SSL(email_conf['server'], email_conf['server_port'])
#     print('链接成功')
#     smtobj.login('815885751@qq.com', 'qqibnkejxunwbddi')
#     print('登录成功')
#     smtobj.sendmail(sender, [receiver], message.as_string())
#     print('邮件发送成功')
# except smtplib.SMTPException as e:
#     print("发送失败--> %s" % e)
# # finally:
# #     smtobj.quit()

# import unittest
# from test_case import test_case_commitOrder,test_case_login,test_case_shopcar
#
# test_module = [test_case_commitOrder,test_case_login,test_case_shopcar]
#
#
# def load_case(module):
#     loader = unittest.TestLoader()
#     suite = loader.loadTestsFromModule(module)
#     return suite
#
#
# def load_case_from_module(module):
#
#     suite_list = []
#
#     for tmp in module:
#         test_suite = load_case(tmp)
#         suite_list.append(test_suite)
#
# print(load_case_from_module(test_module))

# def test(**kwargs):
#     print('开始了')
#     for i in kwargs:
#         print('进来了')
#         if i == 'coo':
#             print('牛逼')
#         else:
#             print('none')
#     print('over')
# test()