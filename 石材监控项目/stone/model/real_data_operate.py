#!/usr/bin/python
#encoding=utf-8
'''
作者：tancj
时间：20150807
模块用途：
        针对石材监控系统数据的处理，具体参考各功能函数的说明
'''
import json
import ConfigParser
import sys

reload (sys)
sys.setdefaultencoding('utf-8')
from url_json_api import UrlJsonApi
from Config import Config

class RealDataOperate(object):

    ####初始化读取配置文件####
    def __init__(self,Block_Name='StoneRestful',Block_Value='rest_url'):
        config = Config()
        self.ip_address = config.Read_Config(1,Block_Name,Block_Value)
        

    ####处理监控简单页面数据####
    def Simple_Devices(self):
        simple_devices_url_list = []
        simple_devices_json_data_list = []
        

        ####获取restful简单设备目录####
        restful_json_data = UrlJsonApi()
        monitor_devices_url = "%s/v1.0/stonefab/0001/devices" % self.ip_address
        devices_json_data = restful_json_data.url_method(1,monitor_devices_url)
        devices_data = json.loads(devices_json_data)

        ####获取restful简单设备数据地址列表####
        for i in devices_data['devices']:
            simple_devices_url = "%s/v1.0/stonefab/0001/rtshort/device/%s" %(self.ip_address,i['did'])
            simple_devices_url_list.append(simple_devices_url)
            
        ####获取restful简单设备数据####
        for i in simple_devices_url_list:
            i = str(i)
            simple_devices_json_data = restful_json_data.url_method(1,i)
            simple_devices_json_data = json.loads(simple_devices_json_data)
            simple_devices_json_data_list.append(simple_devices_json_data)
        #print simple_devices_json_data_list
        return simple_devices_json_data_list
        
    #####处理监控整页面数据#####
    def Multi_Devices(self):
        multi_devices_url_list = []
        multi_devices_json_data_list = []
        
 
        ####获取restful整页面设备目录####
        restful_json_data = UrlJsonApi()
        monitor_devices_url = "%s/v1.0/stonefab/0001/hsweb/devices" % self.ip_address
        devices_json_data = restful_json_data.url_method(1,monitor_devices_url)
        devices_data = json.loads(devices_json_data)

        ####获取restful整页面设备数据地址列表####
        for i in devices_data['devices']:
            multi_devices_url = "%s/v1.0/stonefab/0001/rtmore/device/%s" %(self.ip_address,i['did'])
            multi_devices_url_list.append(multi_devices_url)

        ####获取restful简单设备数据####
        for i in multi_devices_url_list:
            i = str(i)
            multi_devices_json_data = restful_json_data.url_method(1,i)
            multi_devices_json_data = json.loads(multi_devices_json_data)
            multi_devices_json_data_list.append(multi_devices_json_data)
        print multi_devices_json_data_list

if __name__ == "__main__":
    RealDataOperate = RealDataOperate()
    #RealDataOperate.Simple_Devices()
    RealDataOperate.Multi_Devices()
