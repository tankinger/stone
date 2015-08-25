# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json

import sys
reload(sys)
sys.setdefaultencoding('gb18030')

# 可查询工厂
class listStoneFabs(tornado.web.RequestHandler):
    def get(self):
        revc = {
            "fabs": [
                {"fid": "0001", "name": "福建三叶物流"},
                {"fid": "0002", "name": "福建博德石材"}
            ],
            "error": "NULL"
        }
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
        
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)
        

# 查询工厂信息
class listFabInfo(tornado.web.RequestHandler):
    def get(self, fid):     
        revc = {
            "fid": "",
            "name": "",
            "url": "",
            "db": "",
            "error": "NULL"
        }
       
        flist = {
            "0001": "福建三叶物流",
            "0002": "福建博德石材"
        }
        
        if (flist.has_key(fid)):
            revc["fid"] = fid
            revc["name"] = flist[fid]
            revc["url"] = "http://10.9.32.108:8888"
            revc["db"] = "stonefab" + fid
        else:
            revc["fid"] = fid
            revc["error"] = 'Error: fab_id ' + fid + ' database not exist!'
        
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
        
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)        
        
 
# 查询工厂设备
class listFabDevices(tornado.web.RequestHandler):
    def get(self, fid):
        revc = {
            "fid": "0001",
            "devices": [
                {"did": "pg0001", "name": "1#排锯", "subdid": []},
                {"did": "mj0001", "name": "1#磨机", "subdid": [] },
                {"did": "bjx0001b", "name": "1#立体补胶线", "subdid": ["bjx0001a", "bjx0001b"]}
            ],
            "error": "NULL"
        }
        if (fid != '0001'):
            revc["fid"] = fid
            revc["devices"] = []
            revc["error"] = 'Error: fab_id ' + fid + ' database not exist!'
            
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
        
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)
 