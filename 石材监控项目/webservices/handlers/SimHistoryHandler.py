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
        revc = {
            "fid": "0001",
            "devices": [
                {"did": "pg0001", "name": "1#�ž�"},
                {"did": "mj0001", "name": "1#ĥ��" },
                {"did": "bjx0001a", "name": "1#���岹����A��"},
                {"did": "bjx0001b", "name": "1#���岹����B��"}
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
        
# ����ʷ��ѯ�豸������        
class hsDevContent(tornado.web.RequestHandler):
    def get(self, fid, did):       
        revc = {
            "fid": "",
            "did": "",
            "contents": [],
            "error": "NULL"
        }
        dlist = {
            "pg0001": "1#�ž�",
            "mj0001": "1#ĥ��",
            "bjx0001a": "1#���岹����A��",
            "bjx0001b": "1#���岹����B��"
        }
        err = ''
        if (fid != '0001'):
            err = 'Error: fab_id ' + fid + ' database not exist!'
        elif (not dlist.has_key(did)):
            
            err = 'Error: dev_id ' + did + ' not exist!'
        
        revc["fid"] = fid
        revc["did"] = did        
        if (err == ''):     
            revc["name"] = dlist[did]
            
            if (did[0:2] == 'pg'):
                revc["contents"] = [
                    {"cid": "currentflow", "name": "˲ʱ����", "unit": "A"},
                    {"cid": "mompower", "name": "˲ʱ�ܹ���", "unit": "KW"},
                    {"cid": "fwrotspeed", "name": "����ת��", "unit": "RPM"},
                    {"cid": "fwcurrflow", "name": "���ֵ���", "unit": "A"},
                    {"cid": "cutspeed", "name": "�и��ٶ�", "unit": "cm/h"},
                    {"cid": "cutratio", "name": "�и�Ч��", "unit": "�O/h"},
                    {"cid": "totalpower", "name": "���õ���", "unit": "KWh"}
                ]
            if (did[0:2] == 'mj'):
                revc["contents"] = [
                    {"cid": "currentflow", "name": "˲ʱ����", "unit": "A"},
                    {"cid": "mompower", "name": "˲ʱ�ܹ���", "unit": "KW"},
                    {"cid": "beltspeed", "name": "Ƥ���ٶ�", "unit": "cm/min"},
                    {"cid": "beamswingspeed", "name": "�����ڶ��ٶ�", "unit": "m/min"},
                    {"cid": "grindratio", "name": "ĥ��Ч��", "unit": "�O/h"},
                    {"cid": "totalpower", "name": "���õ���", "unit": "KWh"}
                ]
            if (did[0:3] == 'bjx'):
                if (did[7] == 'a'):
                    revc["contents"] = [
                        {"cid": "momcurrenta", "name": "A�����", "unit": "A"},
                        {"cid": "mompowera", "name": "A�书��", "unit": "KW"},
                        {"cid": "tempea", "name": "A���¶�", "unit": "��C"},
                        {"cid": "humiditya", "name": "A��ʪ��", "unit": "%"},
                        {"cid": "powera", "name": "A���õ���", "unit": "KWh"}
                    ]
                elif (did[7] == 'b'):
                    revc["contents"] = [
                        {"cid": "momcurrentb", "name": "B�����", "unit": "A"},
                        {"cid": "mompowerb", "name": "B�书��", "unit": "KW"},
                        {"cid": "tempeb", "name": "B���¶�", "unit": "��C"},
                        {"cid": "humidityb", "name": "B��ʪ��", "unit": "%"},
                        {"cid": "powerb", "name": "B���õ���", "unit": "KWh"},
                        {"cid": "totalpower", "name": "���õ���", "unit": "KWh"},
                        {"cid": "mompower", "name": "˲ʱ�ܹ���", "unit": "KW"},
                        {"cid": "tacttiming", "name": "��������", "unit": "min/Ƭ"}
                    ]
        else:
            revc["error"] = err
                       
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevContent." % status_code)

# ��ѯ��ʷ����
class hsDevData(tornado.web.RequestHandler):
    def get(self, fid, did, cid):      
        revc = {
            "fid": "",
            "did": "",
            "devname": "",
            "cid": "",
            "content": "",
            "start": "",
            "end": "",
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
        
        err = ''
        if (fid != '0001'):
            err = 'Error: fab_id ' + fid + ' database not exist!'
        elif (not dlist.has_key(did)):
            err = 'Error: dev_id ' + did + ' not exist!'

        revc["fid"] = fid
        revc["did"] = did            
        if (err == ''): 
            revc["devname"] = dlist[did]
       
            clist = {}
            if (did[0:2] == 'pg'):
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
                    revc["error"] = 'Error: url_argument ' + cid + ' not exist!'
                
                
            elif (did[0:2] == 'mj'):
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
                    revc["error"] = 'Error: url_argument ' + cid + ' not exist!'
                    
            elif (did[0:3] == 'bjx'):   
                if (did[7] == 'a'):
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
                        revc["error"] = 'Error: url_argument ' + cid + ' not exist!'
                        
                elif (did[7] == 'b'):
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
                        revc["error"] = 'Error: url_argument ' + cid + ' not exist!'
            
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
                    revc["error"] = 'Error: url_argument time format convert failed (hsDevData - get)'
                    self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
                    return
                    
                revc["start"] = str(st)
                revc["end"] = str(et)
                while True:
                    if (st > et):
                        break
                    revc["times"].append(str(st))
                    revc["data"].append(round(random.uniform(500, 1000), 1))
                    st = st + datetime.timedelta(minutes = 1) 
            
            #print revc
        else:
            revc["error"] = err
            
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevData." % status_code)
        
    
        

