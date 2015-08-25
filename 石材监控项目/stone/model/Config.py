#!/usr/bin/python
#encoding=utf-8

'''
作者：tancj
时间：20150808
读取配置文件模块
'''

import ConfigParser
import sys
import os

reload (sys)
sys.setdefaultencoding('utf-8')


class Config(object):

    ####初始化配置文件的路径####
    def __init__(self):
        #if __name__ == '__main__':
        if __name__ == '__main__' or os.path.isfile('monitor_operate.py')\
                or os.path.isfile('ChartsHandler.py') \
                or os.path.isfile('tables_operate.py'):
            self.config_path = '../config/data.conf'
        else:
            self.config_path = './config/data.conf'
    
    
    
    ####读取模块####
    def Read_Config(self,method_parameter,Block_Name,Block_Value='please send your string data'):
        
        method_sql_dict = {1:"one",2:"all"}
        method_sql = method_sql_dict.get(method_parameter)
        name = []
        value = []

        ####调用config文件####
        cf = ConfigParser.ConfigParser()
        cf.read(self.config_path)

        ####判断操作方法####
        if method_sql == "one":
            all_info = cf.get(Block_Name,Block_Value)
        if method_sql == "all":
           
            # s = cf.sections()  ##读出块数
            # o = cf.options(Block_Name)  ##读块中的值 
            v = cf.items(Block_Name)
            ###构造所有数据的字典###
            for i in v:
                name.append(i[0])
                value.append(i[1])
                all_info = dict(zip(name,value))
        #print all_info
        return all_info





if __name__ == '__main__':
    Block_Name = 'StoneRestful'
    Block_Value = 'rest_url'
    Config = Config()
    test_show = Config.Read_Config(1,Block_Name,Block_Value)
    #print test_show
