#!/usr/bin/python
#encoding=utf-8
'''
作者：tancj
时间：20150814
模块用途：
       获取系统时间，并转化为可使用格式
'''
import time
import sys

reload (sys)
sys.setdefaultencoding('utf-8')

class SystemTime(object):
    def __init__(self):
        pass


    def Tables_TimeForPage(self):
        '''获取系统当前时间，并转化成生产报表页面可以使用格式 '''

        TimeForPage = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return TimeForPage

    def Tables_TimeForThead(self):
        '''获取系统当前时间，并转化成生产报表可以使用格式 '''

        TimeForThead = time.strftime('%Y%m%d',time.localtime(time.time()))
        return TimeForThead




if __name__ == "__main__":
    system_time = SystemTime()
    system_time.Tables_TimeForPage()
    
    
