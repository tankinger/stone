#encoding=utf-8

## Copyright (C), 2013-2014, ****.
## File name:       
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
from handlers.BaseHandler import BaseHandler
from model.data_operate import MysqlDataOperate

class UsersHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        ##### 设置安全cookie #####
        self.Username = self.get_secure_cookie("Username")
        self.Flag = self.get_secure_cookie("Flag")
        self.set_secure_cookie("Username",self.Username,expires_days=None)
        self.set_secure_cookie("Flag",self.Flag,expires_days=None)

        ###获取数据库User表的信息###
        mysql_data = MysqlDataOperate()
        userinfo_json_package = mysql_data.User_info('User')
        self.i = len(userinfo_json_package)
        #print self.i

        ####渲染传递数据####
        self.render('users.html',
                    Username = self.Username,
                    User_Flag = self.Flag,
                    i = self.i,
                    j = 0,
                    userinfo_json_package = userinfo_json_package
                    
                    )
