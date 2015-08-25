# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json
import datetime, time
import random

import sys
reload(sys)
sys.setdefaultencoding('gb18030')   

# ��ѯ�����豸ʵʱ������Ϣ
class devRTShortData(tornado.web.RequestHandler):
    def get(self, fid, did):
        revc = {
            "fid": "",
            "did": "",
            "name": "",
            "subdid": [],
            "data": [],
            "state": {"name": "����״̬", "value": ""},
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
                revc = dataPG(revc)
            if (did[0:2] == 'mj'):
                revc = dataMJ(revc)
            if (did[0:3] == 'bjx'):
                revc = dataBJX(revc) 
        else:
            revc["error"] = err
            
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
        
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)    
 
# ��ѯ�����豸ʵʱ��ϸ��Ϣ
class devRTMoreData(tornado.web.RequestHandler):
    def get(self, fid, did):
        revc = {
            "fid": "",
            "did": "",
            "name": "",
            "subdid": [],
            "data": [],
            "state": {"name": "����״̬", "value": ""},
            "alarms": {"name": "������Ϣ", "value": []},
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
                revc = dataPG(revc)
            if (did[0:2] == 'mj'):
                revc = dataMJ(revc)
            if (did[0:3] == 'bjx'):
                revc = dataBJX(revc) 
        else:
            revc["error"] = err
            
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
        
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)
 

def dataPG(revc):
    cdata = [
        {"cid": "output", "name": "�������", "value": 1000.0, "unit": "�O"},
        {"cid": "cutspeed", "name": "�и��ٶ�", "value": 1232.2, "unit": "cm/h"},
        {"cid": "cutratio", "name": "�и�Ч��", "value": 12.2, "unit": "�O/h"},
        {"cid": "mompower", "name": "˲ʱ�ܹ���", "value": 235.9, "unit": "KW"},
        {"cid": "currentflow", "name": "˲ʱ�ܵ���", "value": 612.2, "unit": "A"},
        {"cid": "totalpower", "name": "�������õ���", "value": 9212.2, "unit": "KWh"},
        {"cid": "fwrotspeed", "name": "����ת��", "value": 12.2, "unit": "RPM"},
        {"cid": "fwcurrflow", "name": "���ֵ���", "value": 384.1, "unit": "A"}
    ]
    
    cdata[0]["value"] = round(random.uniform(500, 6000), 1)
    cdata[1]["value"] = round(random.uniform(1000, 2000), 1)
    cdata[2]["value"] = round(random.uniform(10, 60), 1)
    cdata[3]["value"] = round(random.uniform(100, 500), 1)
    cdata[4]["value"] = round(random.uniform(100, 1000), 1)
    cdata[5]["value"] = round(random.uniform(1000, 100000), 1)
    cdata[6]["value"] = round(random.uniform(10, 60), 1)
    cdata[7]["value"] = round(random.uniform(100, 600), 1)
    
    slist = ["ͣ��", "����", "����", "ͨ���쳣"]
    state = random.randint(0, 3)   
    revc["state"]["value"] = slist[state]
    
    if (state == 0):
        cdata[1]["value"] = 0.0
        cdata[2]["value"] = 0.0
        cdata[3]["value"] = 0.0
        cdata[4]["value"] = 0.0
        cdata[6]["value"] = 0.0
        cdata[7]["value"] = 0.0
    
    if (revc.has_key("alarms")):   #more message
        alarms = [
            "���������", 
            "����λ����", 
            "����λ����", 
            "������Ƶ������", 
            "��ˮѹ����", 
            "����ѹ����", 
            "������ͬ������", 
            "���ֵ�ת�ٱ���", 
            "�������λ����"
        ]
        
        if (state == 2):
            revc["alarms"]["value"] = random.sample(alarms, random.randint(1, 4))
        elif (state == 3):
            revc["alarms"]["value"] = random.sample(["�ž�CPUվ�쳣", "�ž������վ�쳣"], random.randint(1, 2))

    else:  #short message
        cdata = cdata[0:4]

    revc["data"] = cdata
    
    return revc
    

def dataMJ(revc):
    cdata = [
        {"cid": "output", "name": "�������", "value": 1000.0, "unit": "�O"},
        {"cid": "beltspeed", "name": "Ƥ���ٶ�", "value": 76.2, "unit": "cm/min"},
        {"cid": "grindratio", "name": "ĥ��Ч��", "value": 5.6, "unit": "�O/h"},
        {"cid": "mompower", "name": "˲ʱ�ܹ���", "value": 235.9, "unit": "KW"},
        {"cid": "currentflow", "name": "˲ʱ�ܵ���", "value": 312.2, "unit": "A"},
        {"cid": "totalpower", "name": "�������õ���", "value": 9212.2, "unit": "KWh"},
        {"cid": "beamswingspeed", "name": "�����ڶ��ٶ�", "value": 29.7, "unit": "m/min"},
        {"cid": "beamposition", "name": "����λ��", "value": 14.1, "unit": "mm"}
    ]
    
    cdata[0]["value"] = round(random.uniform(500, 6000), 1)
    cdata[1]["value"] = round(random.uniform(10, 200), 1)
    cdata[2]["value"] = round(random.uniform(1, 30), 1)
    cdata[3]["value"] = round(random.uniform(100, 500), 1)
    cdata[4]["value"] = round(random.uniform(100, 1000), 1)
    cdata[5]["value"] = round(random.uniform(1000, 100000), 1)
    cdata[6]["value"] = round(random.uniform(10, 60), 1)
    cdata[7]["value"] = round(random.uniform(1, 20), 1)
    
    slist = ["ͣ��", "����", "����", "ͨ���쳣"]
    state = random.randint(0, 3)   
    revc["state"]["value"] = slist[state]
    
    if (state == 0):
        cdata[1]["value"] = 0.0
        cdata[2]["value"] = 0.0
        cdata[3]["value"] = 0.0
        cdata[4]["value"] = 0.0
        cdata[6]["value"] = 0.0

    
    if (revc.has_key("alarms")):   #more message
        alarms = [
            "1#ĥͷĥ�ϱ���",
            "2#ĥͷĥ�ϱ���",
            "3#ĥͷĥ�ϱ���",
            "4#ĥͷĥ�ϱ���",
            "5#ĥͷĥ�ϱ���",
            "6#ĥͷĥ�ϱ���",
            "7#ĥͷĥ�ϱ���",
            "8#ĥͷĥ�ϱ���",
            "9#ĥͷĥ�ϱ���",
            "10#ĥͷĥ�ϱ���",
            "11#ĥͷĥ�ϱ���",
            "12#ĥͷĥ�ϱ���",
            "13#ĥͷĥ�ϱ���",
            "14#ĥͷĥ�ϱ���",
            "15#ĥͷĥ�ϱ���",
            "16#ĥͷĥ�ϱ���",
            "����ǰ����λ����",
            "��������λ����",
            "����ѹ����",
            "Ƥ���������",
            "�ڶ��������",
            "��ͣ״̬",
            "�����������"
        ]
        
        if (state == 2):
            revc["alarms"]["value"] = random.sample(alarms, random.randint(1, 4))
        elif (state == 3):
            revc["alarms"]["value"] = random.sample(["CPUվ���쳣", "������վ���쳣"], random.randint(1, 2))
                        
    else:  #short message
        cdata = cdata[0:4]

    revc["data"] = cdata
    
    return revc
  
  
def dataBJX(revc):
    cdata = [
        {"cid": "output", "name": "�������", "value": 637.1, "unit": "Ƭ"},
        {"cid": "tacttiming", "name": "��������", "value": 76.2, "unit": "min/Ƭ"},
        {"cid": "totalpower", "name": "���õ���", "value": 8325.6, "unit": "KWh"},
        {"cid": "mompower", "name": "˲ʱ�ܹ���", "value": 235.9, "unit": "KW"},
        {"cid": "tempe_a", "name": "A���¶�", "value": 32.2, "unit": "��C"},
        {"cid": "humidity_a", "name": "A��ʪ��", "value": 56.5, "unit": "%"},
        {"cid": "momcurrent_a", "name": "A��˲ʱ����", "value": 256.5, "unit": "A"},
        {"cid": "mompower_a", "name": "A��˲ʱ����", "value": 112.2, "unit": "KW"},
        {"cid": "power_a", "name": "A���õ���", "value": 4334.1, "unit": "KWh"},
        {"cid": "tempe_b", "name": "B���¶�", "value": 32.2, "unit": "��C"},
        {"cid": "humidity_b", "name": "B��ʪ��", "value": 56.5, "unit": "%"},
        {"cid": "momcurrent_b", "name": "B��˲ʱ����", "value": 256.5, "unit": "A"},
        {"cid": "mompower_b", "name": "B��˲ʱ����", "value": 112.2, "unit": "KW"},
        {"cid": "power_b", "name": "B���õ���", "value": 4334.1, "unit": "KWh"}
    ]
    
    revc["subdid"] = ["bjx0001a", "bjx0001b"]
    
    if (revc["did"][7] == 'a'):
        cdata = cdata[0:9]
    elif (revc["did"][7] == 'b'):
        del cdata[4:9]
    
    cdata[0]["value"] = round(random.uniform(500, 6000), 1)
    cdata[1]["value"] = round(random.uniform(10, 200), 1)
    cdata[2]["value"] = round(random.uniform(1000, 100000), 1)
    cdata[3]["value"] = round(random.uniform(100, 500), 1)
    cdata[4]["value"] = round(random.uniform(10, 100), 1)
    cdata[5]["value"] = round(random.uniform(10, 100), 1)
    cdata[6]["value"] = round(random.uniform(100, 600), 1)
    cdata[7]["value"] = round(random.uniform(100, 600), 1)
    cdata[8]["value"] = round(random.uniform(1000, 5000), 1)
    
    slist = ["ͣ��", "����", "����", "ͨ���쳣"]
    state = random.randint(0, 3)   
    revc["state"]["value"] = slist[state]
    
    if (state == 0):
        cdata[1]["value"] = 0.0
        cdata[3]["value"] = 0.0
        cdata[4]["value"] = 0.0
        cdata[5]["value"] = 0.0
        cdata[6]["value"] = 0.0
        cdata[7]["value"] = 0.0
    
    if (revc.has_key("alarms")):   #more message
        alarms = [
            "A�����״̬",
            "B�����״̬",
        ]
        if (revc["did"][7] == 'a'):
            del alarms[1]
        elif (revc["did"][7] == 'b'):
            del alarms[0]
        
        if (state == 2):
            revc["alarms"]["value"] = alarms
        elif (state == 3):
            revc["alarms"]["value"] = random.sample(["CPUվ���쳣", "������վ���쳣"], random.randint(1, 2))
    
    else:  #short message
        cdata = cdata[0:4]

    revc["data"] = cdata
    
    return revc