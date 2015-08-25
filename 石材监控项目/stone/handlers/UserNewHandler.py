#encoding=utf-8



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
from model.mysql_m import MysqlInfo

class UserNewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
##### 设置登入安全cookie和权限标记cookie #####
        self.Username = self.get_secure_cookie("Username")
        self.Flag = self.get_secure_cookie("Flag")
        self.set_secure_cookie("Username",self.Username,expires_days=None)
        self.set_secure_cookie("Flag",self.Flag,expires_days=None)
####渲染传递数据####
        self.render('user-new.html',Username = self.Username,User_Flag = self.Flag,username_info=True,register_check='')

    @tornado.web.authenticated
    def post(self):
##### 设置安全cookie #####
        
        self.Username = self.get_secure_cookie("Username")
        self.Flag = self.get_secure_cookie("Flag")
        self.set_secure_cookie("Username",self.Username,expires_days=None)
        self.set_secure_cookie("Flag",self.Flag,expires_days=None)
        
####获取数据####
        
        self.New_UserName = self.get_argument('NewUserName')
        self.User_Password = self.get_argument('UserPassword')
        self.Phone_Number = self.get_argument('PhoneNumber')
        self.User_Type = self.get_argument('UserType')
        print self.New_UserName,self.User_Password ,self.Phone_Number,self.User_Type

####实例化两个模块 ,并且设定好写入数据库的参数####
        mysql_data = MysqlDataOperate()
        mysqlinfo = MysqlInfo()
        list_element = "(Username,Passwd,Phonenumber,Flag)"
        list_data = "('%s','%s','%s','%s')" % (self.New_UserName,self.User_Password,self.Phone_Number,self.User_Type)
        list_data = str(list_data)
        table_name = 'User'

####判断用户名是否可用和判断是否写入数据库成功#####
        username_info = mysql_data.UserName_check(self.New_UserName,'User')
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        if username_info == True:
            print '用户名可以注册'            
            mysqlinfo.insert_data_one(table_name,list_element,list_data)
            register_check = mysql_data.Register_check(self.New_UserName,'User')
            if register_check == True:
                print '注册成功'
                self.render('user-new.html',Username = self.Username,User_Flag = self.Flag,username_info=username_info,register_check=register_check)
            else:
                print '注册失败'
                self.render('user-new.html',Username = self.Username,User_Flag = self.Flag,register_check=register_check)
        else:
            print '用户名占用'
            self.render('user-new.html',Username = self.Username,User_Flag = self.Flag,username_info=username_info,register_check='')
        
