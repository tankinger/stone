# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json

import sys
reload(sys)
sys.setdefaultencoding('gb18030')

# �ɲ�ѯ����
class listStoneFabs(tornado.web.RequestHandler):
    def get(self):
        revc = {
            "fabs": [
                {"fid": "0001", "name": "������Ҷ����"},
                {"fid": "0002", "name": "��������ʯ��"}
            ],
            "error": "NULL"
        }
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
        
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)
        

# ��ѯ������Ϣ
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
            "0001": "������Ҷ����",
            "0002": "��������ʯ��"
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
        
 
# ��ѯ�����豸
class listFabDevices(tornado.web.RequestHandler):
    def get(self, fid):
        revc = {
            "fid": "0001",
            "devices": [
                {"did": "pg0001", "name": "1#�ž�", "subdid": []},
                {"did": "mj0001", "name": "1#ĥ��", "subdid": [] },
                {"did": "bjx0001b", "name": "1#���岹����", "subdid": ["bjx0001a", "bjx0001b"]}
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
 