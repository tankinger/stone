#!/usr/bin/python
#encoding=utf-8
import MySQLdb
import MySQLdb.cursors

import sys
reload (sys)
sys.setdefaultencoding('utf-8')

class MysqlInfo(object):
    '''
    author:tancj
    date:20150610
    version:1.0
    此脚本为mysql操作模块，总共分为以下四大功能函数
    insert_data_one 数据插入
    delete_data  数据删除
    updata_data 数据更新
    get_data  数据获取
    '''
    def __init__(self,host='10.9.32.119',user='stonejk',passwd='kedastone',db='stonefab0001'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        
    

    def connect_order(self,sql):
        '传递参数 sql为标准的mysql操作命令 (类型为字符串) '

        conn = MySQLdb.connect(self.host,self.user,self.passwd,self.db,charset = 'utf8')
        cur = conn.cursor()
        new_order = cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    
    def insert_data_one(self,table_name,list_element,list_data):
        '传递参数 table_name为表名 list_element为表内元素 list_data为插入的数据(类型都为字符串)'
        '''table_name格式为"test111"  list_element格式"(name,age,sexy)"  list_data格式为"('wangzd',25,'man')" '''

        e = ''
        #sql_insert = "insert into test111(name,age,sexy) value('%s',%d,'%s')" % (name,age,sexy)
        sql_insert = "insert into %s%s value%s" % (table_name,list_element,list_data)
        print sql_insert 
    
        self.connect_order(sql_insert)
            
            
    

    def delete_data(self,table_name,id_number):
        '传递参数 table_name为表名 id_number为id号(类型都为字符串)'
        '''table_name格式为"test111"  id_number格式为"13" '''
        
        sql_delete = "delete from %s where id=%s" % (table_name,id_number)
        self.connect_order(sql_delete)
        

    def updata_data(self,table_name,updata_info,id_nubmer):
        '传递参数 table_name为表名 updata_info为需要更新的数据  id_number为id号(类型都为字符串)'
        '''table_name格式为"test111" updata_info格式为"name='tomsssss',age=40"  id_number格式为"13" '''        
        

        sql_updata = "update %s set %s where id=%s" % (table_name,updata_info,id_nubmer)
        self.connect_order(sql_updata)

    
    def get_data(self,table_name,oper,self_defined='please send your sql'):
        '传递参数 table_name为表名 oper为参数0 1 2(类型int)  self_defined为自定义查询命令(类型都为字符串)'
        ''' 
        table_name格式为"test111" oper 参数 0 为id最大值即最新数据 1 为所有数据 2 为自定义查询命令 使用0 1参数不需要传self_defined
        '''
        max_id_data = "select * from %s where id=(select max(id) from %s) LIMIT 1" % (table_name,table_name)
        all_data = "select * from %s" % (table_name)
        self_defined = self_defined 
        sql_get_dict = {0:max_id_data,1:all_data,2:self_defined}
        sql_get_data =  sql_get_dict.get(oper)
        try:
            conn = MySQLdb.connect(self.host,self.user,self.passwd,self.db,charset = 'utf8',cursorclass = MySQLdb.cursors.DictCursor)
            cur = conn.cursor()
            new_order = cur.execute(sql_get_data)
            data_info = cur.fetchmany(new_order)
            conn.commit()
            cur.close()
            conn.close()
        except:
            print 'please check your order'
        
        return data_info


if __name__ == '__main__':
    mysqlinfo = MysqlInfo()
    table_name = 'User'
    list_element = "(Username,Passwd,Phonenumber,Flag)"
    list_data = "('rr','rrr','11111','admin')"
    mysqlinfo.insert_data_one(table_name,list_element,list_data)
    #username_sql = "select Username from User where Username='tancj'"
    #print mysqlinfo.get_data(table_name,2,username_sql)



'''        
#mysqlinfo = MysqlInfo()
#sql_max = "select * from test111 where id=(select max(id) from test111)"
#sql_insert = "insert into test111(name,age,sexy) value('jiker',60,'fm')"
#mysqlinfo.connect_order(sql_insert)
#table_name = 'test111'
#updata_info = "name='tomsssss',age=40"
#id_number = '12'
#self_defined ='select * from test111 ORDER BY id ASC LIMIT 5' 
#list_element = "(name,age,sexy)"
#list_data = "('wangzd',25,'man')"
#all_data = dict(zip(list_element,list_data))
#mysqlinfo.insert_data_one(table_name,list_element,list_data) 
#mysqlinfo.delete_data(table_name,id_number)        
#mysqlinfo.updata_data(table_name,updata_info,id_number)        

#mysqlinfo.get_data(table_name,2,self_defined)        
'''
