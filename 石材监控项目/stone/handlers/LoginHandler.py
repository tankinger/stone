#encoding=utf-8

## Copyright (C), 2013-2014, ****.
## File name:       setting.py
## Author:          tancj    30778121@qq.com
## Version:         0.1.7
## Date:            2014-09-10
## Description:     settings for server
## Others:          none
## History:         none 
##   1. Date:
##      Author:
##      Modification:
##   2. ...


import tornado
import os.path
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from model.data_operate import MysqlDataOperate

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        
        #### 定义工厂id ####
        self.Factory_id = '0001'
        try:
            table_name = 'User'
            self.Username = self.get_argument('inputUsername','')
            self.Passwd = self.get_argument('inputPassword','')
            print self.Username
            print self.Passwd
            mysql_data = MysqlDataOperate()
            login_info = mysql_data.login_check(self.Username,self.Passwd,table_name)
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            
            if login_info[0]==True and login_info[1]==True:
                print '登录成功...'
                Flag_info = mysql_data.Flag_name(self.Username,self.Passwd,table_name)
                self.Flag = Flag_info[0]['Flag']
                self.set_secure_cookie("Username",self.Username,expires_days=None)
                self.set_secure_cookie("Flag",self.Flag,expires_days=None)
                self.set_secure_cookie("Fid",self.Factory_id,expires_days=None)
                self.redirect('/index.html',)
            else:
                print '登录失败...'
                self.redirect('/logout.html')

        except Exception as e:
            print e
