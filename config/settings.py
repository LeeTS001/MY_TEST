
import os
import logging

Base_Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # >>D:\Git\lee\Api_Auto_Test
# data_path = os.path.join(Base_Path, 'data')   # >>D:\Git\lee\Api_Auto_Test\data
data_path = '../data/'

"""
Logging Config
"""
log_path = os.path.join(Base_Path, 'log')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s '
                           '%(filename)s '
                           '%(funcName)s '
                           '[line:%(lineno)d] '
                           '%(levelname)s '
                           ':%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_path+'/log.txt',
                    filemode='a')


"""
Mysql Config
"""
MYSQL_CONFIG = {
    "test": {
        "host": "localhost",
        "user": "lee",
        "passwd": "123456",
        "port": 3306,
        "db_test": "test",
        "db_shop": "shop"
    }
}

"Email Config"
EMAIL_CONFIG = {
    'sender': '',
    'server_port': 465,
    'receivers': [''],
    'server': 'smtp.qq.com'
    ''
}

"ENVIRONMENT"
Environment_Config = {
    'host': 'http://127.0.0.1:8081',

}