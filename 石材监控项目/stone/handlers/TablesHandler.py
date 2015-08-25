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
from model.tables_operate import TablesOperate
from model.Sys_time import SystemTime
from handlers.BaseHandler import BaseHandler 


class TablesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        ##### 设置安全cookie 和权限标记cookie
        self.Username = self.get_secure_cookie("Username")
        self.Flag = self.get_secure_cookie("Flag")
        self.Fid = self.get_secure_cookie("Fid")
        self.set_secure_cookie("Username",self.Username,expires_days=None)
        self.set_secure_cookie("Flag",self.Flag,expires_days=None)

        
        #####初始化一个json包且为空######
        time_page='0000-00-00'
        title_name = '暂无数据'
        e=True
    
        #### 获取系统当前时间 ####
        system_time = SystemTime()
        time_page = system_time.Tables_TimeForPage()
        time_thead = system_time.Tables_TimeForThead()
        
        #### 获取初始化thead tbody total列表 ####
        try:
            thead_list = ['','','','']
            tables_operate = TablesOperate(self.Fid)     
            tables_operate.Tables_Url('pg0001','dayreport',time_thead)
            thead_list = tables_operate.Thead_List()
        except:
            e = False
            print e
            print '>>>>>>>>>>>>>>>>>>>>>>>>>'
            title_name = '数据异常'
            
        finally:

        ###渲染到页面，上传数据#####
            
            tbody_list = [['','','','']]
            total_list = ['','','','']
            self.render('tables.html',
                        Username = self.Username,
                        User_Flag = self.Flag,
                        e=e,
                        time=time_page,
                        thead=thead_list,
                        title_name=title_name,
                        tbody = tbody_list,
                        total = total_list
                        )

    @tornado.web.authenticated
    def post(self):
        
        #### 初始化数据 ####
        e = True

        ##### 设置安全cookie 和权限标记cookie####
        self.Username = self.get_secure_cookie("Username")
        self.Flag = self.get_secure_cookie("Flag")
        self.Fid = self.get_secure_cookie("Fid")
        self.set_secure_cookie("Username",self.Username,expires_days=None)
        self.set_secure_cookie("Flag",self.Flag,expires_days=None)

        
        #### 获取系统当前时间 ####
        system_time = SystemTime()
        time_page = system_time.Tables_TimeForPage()


        ####获取前端post 传输的数据#####
        self.table_type = str(self.get_argument('table_type'))
        self.time = str(self.get_argument('time'))
        self.dev_type = str(self.get_argument('dev_type'))
        self.time = self.time.replace('-','')

        
        #### 获取设备标题信息 ####
        tables_operate = TablesOperate(self.Fid)
        tables_data_dict = tables_operate.Tables_Url(self.dev_type,self.table_type,self.time)
        title_name = "%s (%s%s)" %(tables_data_dict['devname'],tables_data_dict['time'],tables_data_dict['rptitle'])
        
        ##### 调用TablesOperate模块 获取thead列表 ####
        thead_list = tables_operate.Thead_List()
        
        ##### 调用TablesOperate模块 获取tbody列表 ####
        tbody_list = tables_operate.Tbody_List()
        
        ##### 调用TablesOperate模块 获取汇总列表 ####
        total_list = tables_operate.Total_List()
                
        ###渲染到页面，上传数据#####
        self.render('tables.html',
                    Username = self.Username,
                    User_Flag = self.Flag,
                    e=e,
                    time = time_page,
                    title_name = title_name,
                    thead = thead_list,
                    tbody = tbody_list,
                    total = total_list
                    
)
