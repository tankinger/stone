#!/usr/bin/python
#encoding=utf-8
'''
作者：tancj
时间：20150814
模块用途：
        针对石材监控系统生产报表数据处理，具体参考各功能函数的说明
'''
import json
import ConfigParser
import sys

reload (sys)
sys.setdefaultencoding('utf-8')
from url_json_api import UrlJsonApi
from Config import Config


class TablesOperate(object):
    '''初始化读取配置文件'''
    def __init__(self,dev_id='',Block_Name='StoneRestful',Block_Value='rest_url'):
        self.dev_id = dev_id
        config = Config()
        self.ip_address = config.Read_Config(1,Block_Name,Block_Value)


    def Tables_Url(self,dev_name,table_type,table_time):
        '''处理动态的url，并生产相应的json数据 '''

        #### 产生一个url地址 ####
        tables_url = "%s/v1.0/stonefab/%s/report/device/%s/%s?time=%s" %(self.ip_address,self.dev_id,dev_name,table_type,table_time)

        #### 获取数据 ####
        restful_json_data = UrlJsonApi()
        table_json_data = restful_json_data.url_method(1,tables_url)
        table_data = json.loads(table_json_data)
        
        ####设置全局变量，供其他函数调用####
        self.table_data = table_data
        
        #### 返回一个字典数据####
        print table_data
        return table_data

    def Thead_List(self):
        '''处理页面的标题数据，返回一个列表'''
        
        table_data_dict = self.table_data
        Thead_List = table_data_dict['thead']
        return Thead_List

    def Tbody_List(self):
        '''处理页面的生产报表数据，返回一个列表'''

        table_data_dict = self.table_data
        Tbody_List = table_data_dict['tbody']
        return Tbody_List

    def Total_List(self):
        '''处理页面的生产报表汇总数据，返回一个列表'''
        table_data_dict = self.table_data
        Total_List = table_data_dict['tend']
        return Total_List

if __name__ =="__main__":
    tables_operate = TablesOperate()
    tables_operate.Tables_Url('pg0001','dayreport','20150729')
    #tables_operate.Thead_List()
    #tables_operate.Tbody_List()
    #tables_operate.Total_List()
