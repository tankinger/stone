#!/usr/bin/python
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
import json
import ConfigParser
import sys
from handlers.BaseHandler import BaseHandler
from model.monitor_operate import MonitorOperate


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        
        ##### 设置安全cookie #####
        self.Username = self.get_secure_cookie("Username")
        self.Flag = self.get_secure_cookie("Flag")
        self.Fid = self.get_secure_cookie("Fid")
        self.set_secure_cookie("Username",self.Username,expires_days=None)
        self.set_secure_cookie("Flag",self.Flag,expires_days=None)
        
        
        #### 定义全局变量工厂id 给模块使用 ####
        Factory_Id = self.Fid
        global Factory_Id
        
        #### 调用MonitorOperate 模块的Multi_Device_Page 获取生产页面列表 ####
        monitor_data = MonitorOperate(Factory_Id)
        monitor_data.Multi_Devices()
        page_list = monitor_data.Multi_Device_Page()
        IdForJs_list = monitor_data.Multi_Device_Js()
        DataForJs_list = monitor_data.Multi_Device_Data()
        

        self.render('index.html',
                    Username = self.Username,
                    User_Flag = self.Flag,
                    page_list = page_list,
                    )

        

class Monitor_simple_SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "new client opened"

    def on_close(self):
        print "client closed"

    def on_message(self, message):
        monitor_data = MonitorOperate(Factory_Id)
        monitor_data.Multi_Devices()
        page_list = monitor_data.Multi_Device_Page()
        IdForJs_list = monitor_data.Multi_Device_Js()
        DataForJs_list = monitor_data.Multi_Device_Data()

        asynchronous_data = [IdForJs_list,DataForJs_list[0],DataForJs_list[1],DataForJs_list[2]]
        s = json.dumps(asynchronous_data,ensure_ascii=False)
        self.write_message(s)
