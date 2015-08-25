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

import sys
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
import time
from model.data_random import Random
from model.url_json_api import UrlJsonApi
from model.Config import Config
from handlers.BaseHandler import BaseHandler 
random = Random()
urlJsonApi = UrlJsonApi()
config = Config()

class ChartsHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		####初始页面赋值####
		data = [0]
		times = [0]
		content = '查无数据'
		devname = ''
		time_data = ''
		#### 设置安全cookie 和权限标记cookie
		self.Username = self.get_secure_cookie("Username")
		self.Flag = self.get_secure_cookie("Flag")
		self.set_secure_cookie("Username",self.Username,expires_days=None)
		self.set_secure_cookie("Flag",self.Flag,expires_days=None)
			####获取本地时间
                ts = time.strftime('%Y-%m-%d',time.localtime(time.time()))

		self.render('charts.html',times=times,data=data,content=content,devname=devname,time_data=time_data,ts=ts,Username = self.Username,User_Flag = self.Flag)

	@tornado.web.authenticated	
	def post(self):
		times = []
		data = []
		##### 设置安全cookie 和权限标记cookie
		self.Username = self.get_secure_cookie("Username")
		self.Flag = self.get_secure_cookie("Flag")
		self.set_secure_cookie("Username",self.Username,expires_days=None)
		self.set_secure_cookie("Flag",self.Flag,expires_days=None)
		
                ts = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                #print ts
		####设置时间段####
		stime="000001"
		etime="010000"
		####前后台交互定义
		self.selectp = self.get_argument('selectp')
		self.selectc = self.get_argument('selectc')
		self.time = self.get_argument('time')
		
		#print self.time
		if self.selectp=='0' or self.selectc=='0' or self.time=='':
			####查询为空上传值
			times = [0]
			data = [0]
			devname = '查无数据'
			content = ''
			time_data = ''
			 ##### 设置安全cookie 和权限标记cookie
			self.Username = self.get_secure_cookie("Username")
			self.Flag = self.get_secure_cookie("Flag")
			self.set_secure_cookie("Username",self.Username,expires_days=None)
			self.set_secure_cookie("Flag",self.Flag,expires_days=None)
			ts = time.strftime('%Y-%m-%d',time.localtime(time.time()))
			self.render('charts.html',times=times,data=data,content=content,devname=devname,time_data=time_data,ts=ts,Username = self.Username,User_Flag = self.Flag)
		else:
			####提取时间信息####
			time_data = self.time
			time_s = time_data.replace('-','')
			time_url = "start=%sT%s&end=%sT%s" %(time_s,stime,time_s,etime) 
			####提取设备名称和编号####
			sp_url = self.selectp
			sc_url = self.selectc
			####提取IP变量
			Block_Name='StoneRestful'
			Block_Value='rest_url'
			config = Config()
			ip_address = config.Read_Config(1,Block_Name,Block_Value)
			defined="%s/v1.0/stonefab/0001/hsdata/device/%s/%s?%s" %(ip_address,sp_url,sc_url,time_url)
			defined_url = defined.encode("utf-8")
			####获取JSON数据
			urlJsonApi = UrlJsonApi()
			getvalue = urlJsonApi.url_method(1,defined_url)
			####提取数据####a是总数据 b是时间数据 c是列表数据
			a = json.loads(getvalue)
			b = a['times']
			c = a['data']
			####设备列表
			content = a['content']
			####设备名称
			devname = a['devname']
			####图表X轴数据
			for a1 in b:
				times.append(a1)
			print times
       		##########################
			####图表Y轴数据
			for a2 in c:
				data.append(a2)
			print data
       		####处理数据传到前台####
		
			self.render('charts.html',a1=a1,a2=a2,times=times,data=data,content=content,devname=devname,time_data=time_data,ts=ts,Username = self.Username,User_Flag = self.Flag)


