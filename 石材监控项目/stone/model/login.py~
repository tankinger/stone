#!/usr/bin/python
#encoding=utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
from mysql_m import MysqlInfo

class LoginCheck(object):
    def __init__(self,username='',passwd='',table_name=''):
        self.username = username
        self.passwd = passwd
        self.table_name = table_name
    
    def login_check(self,username,passwd,table_name):
        mysqlinfo = MysqlInfo()
        username_sql = "select Username from User where Username='%s'" % username
        passwd_sql = "select Passwd from User where Username='%s'" %username
        name_check = False
        passwd_check = False
        data_user = mysqlinfo.get_data(table_name,2,username_sql)
        if len(data_user)<1:
            pass
        else:
            name_check = True
            data_passwd = mysqlinfo.get_data(table_name,2,passwd_sql)
            if passwd==data_passwd[0].get('Passwd'):
                passwd_check = True

            
        return name_check,passwd_check


if __name__ == '__main__':
    logincheck = LoginCheck()
    logincheck.login_check('tancj111','tancj','User')
