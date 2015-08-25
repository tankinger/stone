#!/usr/bin/python
#encoding=utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
from mysql_m import MysqlInfo

mysqlinfo = MysqlInfo()
class MysqlOperate(object):

    def __init__(self):
        pass

    def data_max(self):
        table_name = 'user'
        data_max = mysqlinfo.get_data(table_name,1)
        print data_max




if __name__ == '__main__':
    mysql_operate = MysqlOperate()
    mysql_operate.data_max()
