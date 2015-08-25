# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json
import datetime, time
import random

import sys
reload(sys)
sys.setdefaultencoding('gb18030')

# ����ʷ��ѯ�豸
class hsDevices(tornado.web.RequestHandler):
    def get(self, fid):
        if (fid != '0001'):
            self.write('Error: fab_id not exist (hsDevContent - get) ')
            return
        revc = {
            "fid": "0001",
            "devices": [
                {"did": "pg0001", "name": "1#�ž�"},
                {"did": "mj0001", "name": "1#ĥ��" },
                {"did": "bjx0001a", "name": "1#���岹����A��"},
                {"did": "bjx0001b", "name": "1#���岹����B��"}
            ]
        }
        #print (json.dumps(revc, ensure_ascii=False)).decode('gbk')
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)
        
# ����ʷ��ѯ�豸������        
class hsDevContent(tornado.web.RequestHandler):
    def get(self, fid, did):
        if (fid != '0001'):
            self.write('Error: fab_id not exist (hsDevContent - get) ')
            return
        revc = {}
        if (did == 'pg0001'):
            revc = {
                "fid": "0001",
                "did": "pg0001",
                "contents": [
                    {"cid": "currentflow", "name": "˲ʱ����", "unit": "A"},
                    {"cid": "mompower", "name": "˲ʱ�ܹ���", "unit": "KW"},
                    {"cid": "fwrotspeed", "name": "����ת��", "unit": "RPM"},
                    {"cid": "fwcurrflow", "name": "���ֵ���", "unit": "A"},
                    {"cid": "cutspeed", "name": "�и��ٶ�", "unit": "cm/h"},
                    {"cid": "cutratio", "name": "�и�Ч��", "unit": "m2/h"},
                    {"cid": "totalpower", "name": "���õ���", "unit": "KWh"}
                ]
            }
        elif (did == 'mj0001'):
            revc = {
                "fid": "0001",
                "did": "mj0001",
                "contents": [
                    {"cid": "currentflow", "name": "˲ʱ����", "unit": "A"},
                    {"cid": "mompower", "name": "˲ʱ�ܹ���", "unit": "KW"},
                    {"cid": "beltspeed", "name": "Ƥ���ٶ�", "unit": "cm/min"},
                    {"cid": "beamswingspeed", "name": "�����ڶ��ٶ�", "unit": "m/min"},
                    {"cid": "grindratio", "name": "ĥ��Ч��", "unit": "m2/h"},
                    {"cid": "totalpower", "name": "���õ���", "unit": "KWh"}
                ]
            }
        elif (did == 'bjx0001a'):
            revc = {
                "fid": "0001",
                "did": "bjx0001a",
                "contents": [
                    {"cid": "momcurrenta", "name": "A�����", "unit": "A"},
                    {"cid": "mompowera", "name": "A�书��", "unit": "KW"},
                    {"cid": "tempea", "name": "A���¶�", "unit": "��C"},
                    {"cid": "humiditya", "name": "A��ʪ��", "unit": "%"},
                    {"cid": "powera", "name": "A���õ���", "unit": "KWh"}
                ]
            }
        elif (did == 'bjx0001b'):
            revc = {
                "fid": "0001",
                "did": "bjx0001b",
                "contents": [
                    {"cid": "momcurrentb", "name": "B�����", "unit": "A"},
                    {"cid": "mompowerb", "name": "B�书��", "unit": "KW"},
                    {"cid": "tempeb", "name": "B���¶�", "unit": "��C"},
                    {"cid": "humidityb", "name": "B��ʪ��", "unit": "%"},
                    {"cid": "powerb", "name": "B���õ���", "unit": "KWh"},
                    {"cid": "totalpower", "name": "���õ���", "unit": "KWh"},
                    {"cid": "mompower", "name": "˲ʱ�ܹ���", "unit": "KW"},
                    {"cid": "tacttiming", "name": "��������", "unit": "min/Ƭ"}
                ]
            }
                
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevContent." % status_code)

# ��ѯ��ʷ����
class hsDevData(tornado.web.RequestHandler):
    def get(self, fid, did, cid):
        if (fid != '0001'):
            self.write('Error: fab_id not exist (hsDevData - get) ')
            return
        
        revc = {
            "fid": "0001",
            "did": "pg0001",
            "devname": "1#�ž�",
            "cid": "currentflow",
            "content": "˲ʱ����",
            "start": "2015-07-29 14:02:35",
            "end": "2015-07-30 14:02:35",
            "error": "NULL",
            "times": [],
            "data": []
        }
        
        dlist = {
            "pg0001": "1#�ž�",
            "mj0001": "1#ĥ��",
            "bjx0001a": "1#���岹����A��",
            "bjx0001b": "1#���岹����B��"    
        }
        if (dlist.has_key(did)):
            revc["did"] = did
            revc["devname"] = dlist[did]
        
        clist = {}
        if (did == 'pg0001'):
            clist = {
                "currentflow": "˲ʱ����",
                "mompower": "˲ʱ�ܹ���",
                "fwrotspeed": "����ת��",
                "fwcurrflow": "���ֵ���",
                "cutspeed": "�и��ٶ�", 
                "cutratio": "�и�Ч��",
                "totalpower": "���õ���",
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
            
            
        elif (did == 'mj0001'):
            clist = {
                "currentflow": "˲ʱ����",
                "mompower": "˲ʱ�ܹ���",
                "beltspeed": "Ƥ���ٶ�", 
                "beamswingspeed": "�����ڶ��ٶ�",
                "grindratio": "ĥ��Ч��",
                "totalpower": "���õ���",
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
                
        elif (did == 'bjx0001a'):    
            clist = {
                "momcurrenta": "A�����", 
                "mompowera": "A�书��", 
                "tempea": "A���¶�", 
                "humiditya": "A��ʪ��",
                "powera": "A���õ���", 
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
                
        elif (did == 'bjx0001b'):
            clist = {
                "momcurrentb": "B�����", 
                "mompowerb": "B�书��", 
                "tempeb": "B���¶�", 
                "humidityb": "B��ʪ��",
                "powerb": "B���õ���", 
                "totalpower": "���õ���", 
                "mompower": "˲ʱ�ܹ���", 
                "tacttiming": "��������", 
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
        
        if (revc["error"] == "NULL"):
            s = self.get_argument('start')
            e = self.get_argument('end')
            start = s[0:4] + "-" + s[4:6] + "-" + s[6:8] + " " + s[9:11] + ":" + s[11:13] + ":" + s[13:15] 
            end = e[0:4] + "-" + e[4:6] + "-" + e[6:8] + " " + e[9:11] + ":" + e[11:13] + ":" + e[13:15] 
            print start
            print end
            st = datetime.datetime.now()
            et = datetime.datetime.now()
            try:
                st =  datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
                et =  datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            except:
                self.write('Error: time format convert failed (hsDevData - get) ')
                return
                
            revc["start"] = str(st)
            revc["end"] = str(et)
            while True:
                if (st > et):
                    break
                revc["times"].append(str(st))
                revc["data"].append(round(random.uniform(500, 1000), 1))
                st = st + datetime.timedelta(minutes = 1) 
        
        print revc
        #print (json.dumps(revc, ensure_ascii=False)).decode('gbk')
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevData." % status_code)
        
    
        

