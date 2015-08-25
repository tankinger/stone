#/usr/bin/python
#encoding:utf-8

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

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        return self.get_secure_cookie("Username")#,self.get_secure_cookie("Flag")
