#!/usr/bin/python
#encoding=utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
from mysql_m import MysqlInfo
from data_random import Random

class MysqlDataOperate(object):

    def __init__(self,username='',passwd='',table_name='User'):     ####初始化数据####
        self.username = username
        self.passwd = passwd
        self.table_name = table_name
    
    def login_check(self,username,passwd,table_name):          ####检查数据库内的用户名和密码是否存在、匹配####

        mysqlinfo = MysqlInfo()

        ######设置查询命令#######
        username_sql = "select Username from User where Username='%s'" % username
        passwd_sql = "select Passwd from User where Username='%s'" %username
        flag_sql = "select Flag from User where Username='%s'" %username
        name_check = False
        passwd_check = False
        data_user = mysqlinfo.get_data(table_name,2,username_sql)

        ####判断用户名是否存在######
        if len(data_user)<1:
            pass
        else:
            name_check = True

        ####判断对应的密码是否正确###
            data_passwd = mysqlinfo.get_data(table_name,2,passwd_sql)
            if passwd==data_passwd[0].get('Passwd'):
                passwd_check = True

        data_flag = mysqlinfo.get_data(table_name,2,flag_sql)

        ###返回一个判断值###
        #print name_check,passwd_check,data_flag
        return name_check,passwd_check,data_flag

    def Flag_name(self,username,passwd,table_name):         ####返回一个权限判断值####

        mysqlinfo = MysqlInfo()
        flag_sql = "select Flag from User where Username='%s'" %username
        data_flag = mysqlinfo.get_data(table_name,2,flag_sql)
        #print data_flag
        return data_flag

    def UserName_check(self,username,table_name):             ##### 检查数据库内有没有同样的用户名 #####

        mysqlinfo = MysqlInfo()
        username_sql = "select Username from %s" % table_name
        data_user = mysqlinfo.get_data(table_name,2,username_sql)
        j = 0
        for i in data_user:
            
            if username == i['Username']:
                j+=1
                
        if j == 0:
            name_check = True
        else:
            name_check = False
        print name_check
        return name_check


    def Register_check(self,username,table_name):         ###检查注册是否成功####
        
        mysqlinfo = MysqlInfo()
        username_sql = "select Username from %s" % table_name
        data_user = mysqlinfo.get_data(table_name,2,username_sql)
        j = 0

        ###匹配数据库里面是否有相同的用户名###
        for i in data_user:
            if username == i['Username']:
                j+=1
        if j !=0:
            register_check = True
        else:
            register_check = False
        #print register_check
        return register_check


    def User_info(self,table_name):         ###获取数据库所有的用户信息###
        mysqlinfo = MysqlInfo()
        userinfo_sql = "select * from %s" % table_name
        data_userinfo = mysqlinfo.get_data(table_name,2,userinfo_sql)
        #print data_userinfo
        return data_userinfo


    def Monitor_data(self,choice_type):                ###修正监控数据###
        random = Random()
        choice_type_dict = {1:random.monitor_data_paiju(),2:random.monitor_data_moji(),3:random.monitor_data_bujx()}
        monitor_data_json = choice_type_dict[choice_type]

        #print monitor_data_json
        Waring_translate = {0:'暂停',1:'正常',2:'报警'}
        Fault_translate = {1:'低电压故障',2:'低油位故障',3:'发动机过热',4:'主电机故障'}
        Fault_translate_list = []
        #print '>>>>>>>>>>>>>>>>>' 


        #####把故障代码换成中文
        for i in monitor_data_json:
            #print i
            keywords = i.keys()
            if 'Operating_condition_data' in keywords:
                value = i['Operating_condition_data']
                #print value
                #print type(value)
                Waring_translate[value]
                i['Operating_condition_data'] = Waring_translate[value]

            if 'Fault_alarm_data' in keywords:
                value = i['Fault_alarm_data']
                value = list(set(value))
                for j in value:
                    #print j
                    j = Fault_translate[j]
                    Fault_translate_list.append(j)
                i['Fault_alarm_data'] = Fault_translate_list
                    
                
#        print monitor_data_json
        return monitor_data_json
if __name__ == '__main__':
    logincheck = MysqlDataOperate()
    #logincheck.login_check('tancj','tancj11','User')
    #logincheck.Flag_name('tancj','tancj11','User')
    #logincheck.UserName_check('tancj1111','User')
    #logincheck.Register_check('tancj123','User')
    #logincheck.User_info('User')
    logincheck.Monitor_data(3)
