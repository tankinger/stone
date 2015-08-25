#!/usr/bin/python
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
from BaseHandler import BaseHandler

class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        try:
            UserName = self.get_secure_cookie("Username")
            Flag = self.get_secure_cookie("Flag")
            Fid = self.get_secure_cookie("Fid")
            erro_mesg = " "
            self.clear_cookie("Username")
            self.clear_cookie("Flag")
            self.clear_cookie("Fid")
            self.render('login.html')
        except Exception as e:
            print e


                                                             
