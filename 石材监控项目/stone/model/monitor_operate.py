#!/usr/bin/python
#encoding=utf-8
'''
作者：tancj
时间：20150807
模块用途：
        针对石材监控系统实时数据的处理，具体参考各功能函数的说明
'''
import json
import ConfigParser
import sys
import copy

reload (sys)
sys.setdefaultencoding('utf-8')
from url_json_api import UrlJsonApi
from Config import Config

class MonitorOperate(object):

    '''初始化读取配置文件'''
    def __init__(self,dev_id='',Block_Name='StoneRestful',Block_Value='rest_url'):
        self.dev_id = dev_id
        config = Config()
        self.ip_address = config.Read_Config(1,Block_Name,Block_Value)
        


    def Multi_Devices(self):
        '''处理监控多设备页面数据'''
        multi_devices_url_list = []
        multi_devices_json_data_list = []
        

        ####获取restful多设备目录####
        restful_json_data = UrlJsonApi()
        monitor_devices_url = "%s/v1.0/stonefab/%s/devices" % (self.ip_address,self.dev_id)
        devices_json_data = restful_json_data.url_method(1,monitor_devices_url)
        devices_data = json.loads(devices_json_data)
        
        
        ####获取restful多设备数据地址列表####
        for i in devices_data['devices']:
            multi_devices_url = "%s/v1.0/stonefab/%s/rtshort/device/%s" %(self.ip_address,self.dev_id,i['did'])
            multi_devices_url_list.append(multi_devices_url)
            
        ####获取restful多设备数据####
        for i in multi_devices_url_list:
            i = str(i)
            multi_devices_json_data = restful_json_data.url_method(1,i)
            multi_devices_json_data = json.loads(multi_devices_json_data)
            multi_devices_json_data_list.append(multi_devices_json_data)

        ####设置全局变量，供其他函数调用####
        self.multi_devices_json_data_list = multi_devices_json_data_list
        self.Multi_short_devices_data = devices_data

        #print multi_devices_json_data_list
        return multi_devices_json_data_list
        
    
    def Single_Device(self):
        '''处理监控单设备数据'''
        single_device_url_list = []
        single_device_json_data_list = []
        self.device_data_list = []
 
        ####获取restful设备目录####
        restful_json_data = UrlJsonApi()
        monitor_devices_url = "%s/v1.0/stonefab/%s/hsweb/devices" % (self.ip_address,self.dev_id)
        devices_json_data = restful_json_data.url_method(1,monitor_devices_url)
        devices_data = json.loads(devices_json_data)

        ####设置全局变量，供其他函数调用####
        self.devices_data_Single = devices_data

        ####获取restful整页面设备数据地址列表####
        for i in devices_data['devices']:
            single_device_url = "%s/v1.0/stonefab/%s/rtmore/device/%s" %(self.ip_address,self.dev_id,i['did'])
            single_device_url_list.append(single_device_url)

        ####获取restful单设备数据####
        for i in single_device_url_list:
            i = str(i)
            single_device_json_data = restful_json_data.url_method(1,i)
            single_device_json_data = json.loads(single_device_json_data)
            single_device_json_data_list.append(single_device_json_data)

        ####设置全局变量，供其他函数调用####
        self.device_data_list = single_device_json_data_list

        #print single_device_json_data_list
        return single_device_json_data_list



    def Single_Device_Page(self):
        '''构造单设备网页使用的列表'''
        IdForPage_Internal_list = [] 
        IdForPage_External_list = []
        IdForPage_Total_list = []
        #### 调用Single_Device函数内的全局变量####
        device_data_list = self.device_data_list

        #### 构造列表 ####
        for k,i in enumerate(device_data_list):
            did = str(i['did'])
            IdForPage_External_list =[]
            for j in i['data']:
                cid = j['cid']
                IdForPage_name =str("%s_%s_name" %(did,cid))
                IdForPage_value = str("%s_%s_value" %(did,cid))
                IdForPage_unit = str("%s_%s_unit" %(did,cid))
                IdForPage_Internal_list = [IdForPage_name,IdForPage_value,IdForPage_unit]
                IdForPage_External_list.append(IdForPage_Internal_list)
    
            IdForPage_External_dict = {did:IdForPage_External_list}
            IdForPage_Total_list.append(IdForPage_External_dict)
        
        ####设置全局变量，供其他函数调用####
        self.IdForPage_Total_list = IdForPage_Total_list

        #print IdForPage_Total_list 
        return IdForPage_Total_list


    def Choice_Device(self,device_code=''):
        '''选择设备,并返回设备相应的数据'''

        IdForPage_list = []
        #### 调用Single_Device_Page函数内的全局变量####
        IdForPage_Total_list = self.IdForPage_Total_list

        ####判断设备，并提取相应的数据列表####
        for i in IdForPage_Total_list:
            keyword = i.keys()[0]
            try:
                if device_code == keyword:
                    IdForPage_list = i[device_code]
            except:
                print '参数有误，请检查参数传值'
        return IdForPage_list



    def Device_Name(self,device_code=''):
        '''获取一个设备的设备名字 '''

        #### 调用Multi_Devices函数内的全局变量####
        devices_info = self.devices_data_Single
        
        for i in devices_info['devices']:
            try:
                if device_code == i['did']:
                    device_name = i['name']
            except:
                print '参数有误，请检查参数传值'
        return device_name


    def Choice_Single_Device(self,device_code=''):
        '''选择设备提供设备的数据，此数据异步js使用 '''

        #### 调用Single_Device函数内的全局变量 ####
        single_device_data_list = self.device_data_list

        #### 判断设备，并提取相应的数据列表 ####
        for i in single_device_data_list:
            did = str(i['did'])
            if device_code == did:
                Single_Device_data = i['data']
        #print Single_Device_data
        return Single_Device_data



    def Choice_State_Device(self,device_code=''):
        ''' 选择设备的运行状态，此数据异步js使用 '''
        
        #### 调用Single_Device函数内的全局变量 ####
        single_device_data_list = self.device_data_list
        
        #### 判断设备，并提取相应的数据列表 ####
        for i in single_device_data_list:
            did = str(i['did'])
            if device_code == did:
                State_Device_data = i['state']
        return State_Device_data

    def Choice_Alarms_Device(self,device_code=''):
        ''' 选择设备的故障信息，此数据异步js使用 '''
        
        Alarms_str =''
        #### 调用Single_Device函数内的全局变量 ####
        single_device_data_list = self.device_data_list
        
        #### 判断设备，并提取相应的数据列表 ####
        for i in single_device_data_list:
            did = str(i['did'])
            if device_code == did:
                State_Device_data = i['alarms']

        for j in State_Device_data['value']:
            Alarms_str = Alarms_str +j+'、'

        Alarms_str = Alarms_str.rstrip('、')
        State_Device_data['value']= Alarms_str
        #print State_Device_data
        return State_Device_data


    def Multi_Device_Page(self):
        '''构造多设备网页使用的列表'''
        
        
        IdForPage_Internal_list = [] 
        IdForPage_External_list = []
        IdForMultiPage_Total_list = []
        IdForMultiJs_list = []
        #### 调用Multi_Device函数内的全局变量####
        device_data_list = self.multi_devices_json_data_list

        #### 构造列表 ####
        for k,i in enumerate(device_data_list):
            did = str(i['did'])
            dev_name = did+'_name'
            IdForPage_External_list =[]
            
            #### 构造设备标签 ####
            subdid_url_str=''
            for m in i['subdid']:
                subdid_url_str = subdid_url_str+m+'_'
            subdid_url_str = subdid_url_str.rstrip('_')
            subdid_url_str = str(subdid_url_str)
            subdid_url ='monitor.html?id=%s&subdid=%s' % (did,subdid_url_str) 
            

            #### 构造网页列表 ####
            for j in i['data']:
                cid = j['cid']
                IdForPage_name =str("%s_%s_name" %(did,cid))
                IdForPage_value = str("%s_%s_value" %(did,cid))
                IdForPage_unit = str("%s_%s_unit" %(did,cid))
                IdForPage_Internal_list = [IdForPage_name,IdForPage_value,IdForPage_unit]
                IdForPage_External_list.append(IdForPage_Internal_list)


            #### 构造一个id列表给js 使用 ####
            IdForJs_list = copy.deepcopy(IdForPage_External_list)
            IdForJs_dict = {'data':IdForJs_list,'dev_name':dev_name,'dev_id':did}
            IdForMultiJs_list.append(IdForJs_dict)
            
                        
            #### 提出output 数据 便于页面循环使用 ####
            output_data_list = IdForPage_External_list[0]
            IdForPage_External_list.remove(IdForPage_External_list[0])
            
            IdForPage_External_dict = {'data':IdForPage_External_list,'dev_id':did,'dev_name':dev_name,'subdid':subdid_url,'output':output_data_list}
            IdForMultiPage_Total_list.append(IdForPage_External_dict)
            
            

        ####设置全局变量，供其他函数调用####
        self.IdForMultiPage_Total_list = IdForMultiPage_Total_list
        self.IdForMultiJs_list = IdForMultiJs_list
        
        #print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        #print IdForMultiPage_Total_list
        return IdForMultiPage_Total_list


    def Multi_Device_Js(self):
        ''' 获取多设备的id列表 供js使用 '''

        #### 调用Multi_Device_Page函数内的全局变量####
        IdForMultiJs_list = self.IdForMultiJs_list
        #print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        #print IdForMultiJs_list
        return IdForMultiJs_list



    def Multi_Device_Data(self):
        '''多设备页面数据，供js使用 '''
        
        Multi_Device_DataForJs = [] 
        Multi_Device_StateForJs = []
        Multi_Device_NameForJs = []

        #### 调用Multi_Devices函数内的全局变量####
        Multi_device_data_list = self.multi_devices_json_data_list
        Multi_short_devices_data = self.Multi_short_devices_data

        #### 获取data state 列表 ####
        for i in Multi_device_data_list:
            Multi_Device_DataForJs.append(i['data'])
            Multi_Device_StateForJs.append(i['state'])
            
        #### 获取name 列表 ####
        for j in Multi_short_devices_data['devices']:
            Multi_Device_NameForJs.append(j['name'])
        return Multi_Device_DataForJs,Multi_Device_StateForJs,Multi_Device_NameForJs

    def Single_Subdid_Data(self,subdid=''):
        ''' 单设备页面获取下一级设备数据 用于页面生成设备切换按钮 '''
        
        subdid_list = []
        Subdid_Name_list = []
        subdev = []
        single_device_url_list = []
        single_device_json_data_list = []
        restful_json_data = UrlJsonApi()
        
        #### 判断subdid 是否是空值 ####
        if subdid == '':
            subdid_list=[]
            subdev =[]
            
        else:
            #### 构造设备列表 ####
            subdid = subdid
            subdid_list = subdid.split('_')
        
        
            #### 构造设备的api url地址 ####
            for i in subdid_list:
                single_device_url = "%s/v1.0/stonefab/%s/rtmore/device/%s" %(self.ip_address,self.dev_id,i)
                single_device_url_list.append(single_device_url)


            #### 获取设备的所有信息 ####
            for i in single_device_url_list:
                i = str(i)
                single_device_json_data = restful_json_data.url_method(1,i)
                single_device_json_data = json.loads(single_device_json_data)
                single_device_json_data_list.append(single_device_json_data)

            #### 获取设备的名称 ####
            for j in single_device_json_data_list:
                Subdid_Name_list.append(str(j['name']))
        
            #### 构造设备信息字典 ####
            for i in range(len(subdid_list)):
                subd_dict = {}
                subd_dict['id'] = subdid_list[i]                
                subd_dict['name'] = Subdid_Name_list[i]
                subdev.append(subd_dict)

        #print subdid_list
        #print Subdid_Name_list
        #print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        return subdid_list,subdev
        
        
if __name__ == "__main__":
    RealDataOperate = MonitorOperate('0001')
    #RealDataOperate.Single_Device()
    RealDataOperate.Multi_Devices()
    #RealDataOperate.Single_Device_Page()
    #RealDataOperate.Choice_Device('mj0001')
    #RealDataOperate.Device_Name('pg0001')
    #RealDataOperate.Choice_Single_Device('pg0001')
    #RealDataOperate.Choice_State_Device('pg0001')
    #RealDataOperate.Choice_Alarms_Device('pg0001')
    #RealDataOperate.Multi_Device_Page()
    #RealDataOperate.Multi_Device_Js()
    #RealDataOperate.Multi_Device_Data()
    RealDataOperate.Single_Subdid_Data('bjx0001a_bjx0001b')
