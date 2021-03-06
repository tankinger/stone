#encoding=utf-8
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
from BaseHandler import BaseHandler
from model.data_operate import MysqlDataOperate



class MonitorHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        ##### 设置安全cookie #####
        #self.Username = self.get_secure_cookie("Username")
        #self.Flag = self.get_secure_cookie("Flag")
        #self.set_secure_cookie("Username",self.Username,expires_days=None)
        #self.set_secure_cookie("Flag",self.Flag,expires_days=None)

        #dev_type_flag = self.get_argument(name='id',default='')

        mysql_data = MysqlDataOperate()
        monitor_info_paiju = mysql_data.Monitor_data(1)
        monitor_info_moji = mysql_data.Monitor_data(2)
        monitor_info_bujx = mysql_data.Monitor_data(3)
        dev_type_flag = 1

        if dev_type_flag == 1:
            monitor_info = monitor_info_paiju
            title_name = '排锯设备'
        if dev_type_flag == 2:
            monitor_info = monitor_info_moji
            title_name = '磨机设备'
        if dev_type_flag == 3:
            monitor_info = monitor_info_bujx
            title_name = '立体补胶线A箱'
        if dev_type_flag == 4:
            monitor_info = monitor_info_bujx
            title_name = '立体补胶线B箱'

        #print monitor_info[-3:-4:-1][0]
       # self.render('monitor.html',
       #             Username = self.Username,
       #             User_Flag = self.Flag,
       #             dev_type_flag = dev_type_flag,
       #             monitor_info = monitor_info,
       #             title_name = title_name,
       #             )

        return monitor_info


class Monitor_SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "new client opened"

    def on_close(self):
        print "client closed"

    def on_message(self, message):
        data_info = MonitorHandler(BaseHandler)
        monitor_info = data_info.get()
        print monitor_info
        #asynchronous_data = monitor_info
        #asynchronous_data = str(asynchronous_data)
        #self.write_message(asynchronous_data)


if __name__ =="__main__":

    data_show = MonitorHandler()
    data_list = data_show.get()
    print data_list
