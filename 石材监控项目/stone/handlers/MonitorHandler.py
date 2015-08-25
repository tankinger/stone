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
import json
from handlers.BaseHandler import BaseHandler
from model.data_operate import MysqlDataOperate
from model.monitor_operate import MonitorOperate

class MonitorHandler(BaseHandler):
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
        
        #### 获取下一级设备的id 和 name ####
        dev_subdid =  self.get_argument(name='subdid',default='')
        dev_subdid = str(dev_subdid)
        monitor_data = MonitorOperate(Factory_Id)
        subdev_list = monitor_data.Single_Subdid_Data(dev_subdid)
        #print subdev_list[1]['id']
        #print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

        #### 获取设备代码 ####
        dev_type_flag = self.get_argument(name='id',default='')
        dev_type_flag = str(dev_type_flag)
        global dev_type_flag
        

        #### 调用功能模块 返回一个网页使用的idname列表####
        monitor_data = MonitorOperate(Factory_Id)
        monitor_data.Single_Device()
        monitor_data.Single_Device_Page()
        IdForPage_list = monitor_data.Choice_Device(dev_type_flag)

        #### 调用功能模块 返回一个字符串类型设备名###
        device_name = monitor_data.Device_Name(dev_type_flag)

                

        self.render('monitor.html',
                    Username = self.Username,
                    User_Flag = self.Flag,
                    dev_type_flag = dev_type_flag,
                    IdForPage_list = IdForPage_list,
                    device_name = device_name,
                    subdev = subdev_list,
                    dev_subdid = dev_subdid,
                    )


class Monitor_SocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print "new client opened"

    def on_close(self):
        print "client closed"

    def on_message(self, message):

        #### 调用功能模块 返回一个网页使用的idname列表####
        monitor_data = MonitorOperate(Factory_Id)
        monitor_data.Single_Device()
        monitor_data.Single_Device_Page()
        IdForPage_list = monitor_data.Choice_Device(dev_type_flag)
        
        #### 调用功能模块 返回一个网页使用的设备数据列表 ####
        Choice_Device_data = monitor_data.Choice_Single_Device(dev_type_flag)
        
        #### 调用功能模块 返回一个网页使用的设备运行状态列表 ####
        State_Device_data = monitor_data.Choice_State_Device(dev_type_flag)

        #### 调用功能模块 返回一个网页使用的设备故障信息字典 ####
        Alarms_Device_data = monitor_data.Choice_Alarms_Device(dev_type_flag)


        #### 构造一个数据列表 ####
        asynchronous_data = [IdForPage_list,Choice_Device_data,State_Device_data,Alarms_Device_data]
        #print asynchronous_data
        s = json.dumps(asynchronous_data,ensure_ascii=False)
        
        self.write_message(s)
