#!/usr/bin/python
#encoding=utf-8
'''
    author:tancj
    datetime:20150713
    version:1.0
    此脚本为URL操作，只有一个功能函数
    实现GET POST PUT DELETE 四个功能
    调用函数传值的方法：
    url_method(self,method_parameter,url_defined='please send your sql',data_json='please send your data'):
    method_parameter为四个功能的调用可以传4种值 分别为 1 2 3 4
    1 为GET 2为POST 3为PUT 4为DELETE
    
    url_defined为自定义的url

    data_json为自定义的json 数据  在调用POST PUT 时必须传相应的值

    注意 在调用GET DELETE 功能的时候 必须传method_parameter和url_defined 两个值
    在调用POST PUT 功能的时候  必须传method_parameter、url_defined 和data_json 三个值
    
'''

import pycurl
import StringIO
import simplejson
import urllib
import sys
reload (sys)
sys.setdefaultencoding('utf-8')

class UrlJsonApi(object):
    
    def __init__(self,ip='10.9.32.145',username='admin',passwd='admin'):
        self.ip = ip
        self.username = username
        self.passwd = passwd

    def url_method(self,method_parameter,url_defined='please send your sql',data_json='please send your data'):
        method_sql_dict = {1:"GET",2:"POST",3:"PUT",4:"DELETE"}
        method_sql = method_sql_dict.get(method_parameter)
        print method_sql
        
        c = pycurl.Curl()
        b = StringIO.StringIO()
        c.setopt(pycurl.URL, url_defined)
        c.setopt(pycurl.HTTPHEADER,["Content-Type: application/json","Accept-Charset:GBK,utf-8;q=0.7,*;q=0.3"])
        c.setopt(pycurl.CUSTOMREQUEST,method_sql)
        if method_sql == 'POST' or method_sql=='PUT':
            c.setopt(c.POSTFIELDS, data_json)
        c.setopt(pycurl.VERBOSE,1)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.CONNECTTIMEOUT, 60)
        c.setopt(pycurl.TIMEOUT, 300)
        c.setopt(pycurl.HTTPPROXYTUNNEL,1)
        c.setopt(pycurl.USERAGENT, "kedaIT")
        c.setopt(c.WRITEFUNCTION, b.write)
        c.perform()
        #print b.getvalue()
        return b.getvalue()



if __name__ == '__main__':
    project_create_json = '{"project":{"name":"中文","description":"我爱你们","identifier":"mjiker22333","is_public":"false","inherit_members":"true"}}'
    project_update_json = '{"project":{"name":"中文","description":"我恨你们你们","is_public":"false","inherit_members":"true"}}'
    project_delete_json = ''
    
#print urllib.urlencode(project_create_json)
    #defined="http://10.9.32.108:8881/v1.0/stonefab/0001/hsweb/devices"
    defined="http://10.9.32.108:8881/v1.0/stonefab/0001/devices"
    redminejsonapi = UrlJsonApi()
    #print redminejsonapi.get_method(1,defined)
    #redminejsonapi.post_method(1,project_create_json)
    #redminejsonapi.put_method(project_update_json,defined)
    #redminejsonapi.delete_method(defined)
    redminejsonapi.url_method(1,defined)
