# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json
import datetime, time
import random

import sys
reload(sys)
sys.setdefaultencoding('gb18030')   

# 查询工厂设备实时简略信息
class devRTShortData(tornado.web.RequestHandler):
    def get(self, fid, did):
        revc = {
            "fid": "",
            "did": "",
            "name": "",
            "subdid": [],
            "data": [],
            "state": {"name": "运行状态", "value": ""},
            "error": "NULL"
        }
        dlist = {
            "pg0001": "1#排锯",
            "mj0001": "1#磨机",
            "bjx0001a": "1#立体补胶线A箱",
            "bjx0001b": "1#立体补胶线B箱"
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
 
# 查询工厂设备实时详细信息
class devRTMoreData(tornado.web.RequestHandler):
    def get(self, fid, did):
        revc = {
            "fid": "",
            "did": "",
            "name": "",
            "subdid": [],
            "data": [],
            "state": {"name": "运行状态", "value": ""},
            "alarms": {"name": "报警信息", "value": []},
            "error": "NULL"
        }
        dlist = {
            "pg0001": "1#排锯",
            "mj0001": "1#磨机",
            "bjx0001a": "1#立体补胶线A箱",
            "bjx0001b": "1#立体补胶线B箱"
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
        {"cid": "output", "name": "今天产量", "value": 1000.0, "unit": "㎡"},
        {"cid": "cutspeed", "name": "切割速度", "value": 1232.2, "unit": "cm/h"},
        {"cid": "cutratio", "name": "切割效率", "value": 12.2, "unit": "㎡/h"},
        {"cid": "mompower", "name": "瞬时总功率", "value": 235.9, "unit": "KW"},
        {"cid": "currentflow", "name": "瞬时总电流", "value": 612.2, "unit": "A"},
        {"cid": "totalpower", "name": "今日总用电量", "value": 9212.2, "unit": "KWh"},
        {"cid": "fwrotspeed", "name": "飞轮转速", "value": 12.2, "unit": "RPM"},
        {"cid": "fwcurrflow", "name": "飞轮电流", "value": 384.1, "unit": "A"}
    ]
    
    cdata[0]["value"] = round(random.uniform(500, 6000), 1)
    cdata[1]["value"] = round(random.uniform(1000, 2000), 1)
    cdata[2]["value"] = round(random.uniform(10, 60), 1)
    cdata[3]["value"] = round(random.uniform(100, 500), 1)
    cdata[4]["value"] = round(random.uniform(100, 1000), 1)
    cdata[5]["value"] = round(random.uniform(1000, 100000), 1)
    cdata[6]["value"] = round(random.uniform(10, 60), 1)
    cdata[7]["value"] = round(random.uniform(100, 600), 1)
    
    slist = ["停机", "运行", "报警", "通信异常"]
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
            "主电机故障", 
            "上限位报警", 
            "下限位报警", 
            "升降变频器故障", 
            "低水压报警", 
            "低油压报警", 
            "升降不同步报警", 
            "飞轮低转速报警", 
            "油箱低油位报警"
        ]
        
        if (state == 2):
            revc["alarms"]["value"] = random.sample(alarms, random.randint(1, 4))
        elif (state == 3):
            revc["alarms"]["value"] = random.sample(["排锯CPU站异常", "排锯电量表站异常"], random.randint(1, 2))

    else:  #short message
        cdata = cdata[0:4]

    revc["data"] = cdata
    
    return revc
    

def dataMJ(revc):
    cdata = [
        {"cid": "output", "name": "今天产量", "value": 1000.0, "unit": "㎡"},
        {"cid": "beltspeed", "name": "皮带速度", "value": 76.2, "unit": "cm/min"},
        {"cid": "grindratio", "name": "磨抛效率", "value": 5.6, "unit": "㎡/h"},
        {"cid": "mompower", "name": "瞬时总功率", "value": 235.9, "unit": "KW"},
        {"cid": "currentflow", "name": "瞬时总电流", "value": 312.2, "unit": "A"},
        {"cid": "totalpower", "name": "今日总用电量", "value": 9212.2, "unit": "KWh"},
        {"cid": "beamswingspeed", "name": "横梁摆动速度", "value": 29.7, "unit": "m/min"},
        {"cid": "beamposition", "name": "横梁位置", "value": 14.1, "unit": "mm"}
    ]
    
    cdata[0]["value"] = round(random.uniform(500, 6000), 1)
    cdata[1]["value"] = round(random.uniform(10, 200), 1)
    cdata[2]["value"] = round(random.uniform(1, 30), 1)
    cdata[3]["value"] = round(random.uniform(100, 500), 1)
    cdata[4]["value"] = round(random.uniform(100, 1000), 1)
    cdata[5]["value"] = round(random.uniform(1000, 100000), 1)
    cdata[6]["value"] = round(random.uniform(10, 60), 1)
    cdata[7]["value"] = round(random.uniform(1, 20), 1)
    
    slist = ["停机", "运行", "报警", "通信异常"]
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
            "1#磨头磨料报警",
            "2#磨头磨料报警",
            "3#磨头磨料报警",
            "4#磨头磨料报警",
            "5#磨头磨料报警",
            "6#磨头磨料报警",
            "7#磨头磨料报警",
            "8#磨头磨料报警",
            "9#磨头磨料报警",
            "10#磨头磨料报警",
            "11#磨头磨料报警",
            "12#磨头磨料报警",
            "13#磨头磨料报警",
            "14#磨头磨料报警",
            "15#磨头磨料报警",
            "16#磨头磨料报警",
            "横梁前极限位报警",
            "横梁后极限位报警",
            "低气压报警",
            "皮带电机故障",
            "摆动电机故障",
            "急停状态",
            "横梁清零故障"
        ]
        
        if (state == 2):
            revc["alarms"]["value"] = random.sample(alarms, random.randint(1, 4))
        elif (state == 3):
            revc["alarms"]["value"] = random.sample(["CPU站号异常", "电量表站号异常"], random.randint(1, 2))
                        
    else:  #short message
        cdata = cdata[0:4]

    revc["data"] = cdata
    
    return revc
  
  
def dataBJX(revc):
    cdata = [
        {"cid": "output", "name": "今天产量", "value": 637.1, "unit": "片"},
        {"cid": "tacttiming", "name": "生产节拍", "value": 76.2, "unit": "min/片"},
        {"cid": "totalpower", "name": "总用电量", "value": 8325.6, "unit": "KWh"},
        {"cid": "mompower", "name": "瞬时总功率", "value": 235.9, "unit": "KW"},
        {"cid": "tempe_a", "name": "A箱温度", "value": 32.2, "unit": "°C"},
        {"cid": "humidity_a", "name": "A箱湿度", "value": 56.5, "unit": "%"},
        {"cid": "momcurrent_a", "name": "A箱瞬时电流", "value": 256.5, "unit": "A"},
        {"cid": "mompower_a", "name": "A箱瞬时功率", "value": 112.2, "unit": "KW"},
        {"cid": "power_a", "name": "A箱用电量", "value": 4334.1, "unit": "KWh"},
        {"cid": "tempe_b", "name": "B箱温度", "value": 32.2, "unit": "°C"},
        {"cid": "humidity_b", "name": "B箱湿度", "value": 56.5, "unit": "%"},
        {"cid": "momcurrent_b", "name": "B箱瞬时电流", "value": 256.5, "unit": "A"},
        {"cid": "mompower_b", "name": "B箱瞬时功率", "value": 112.2, "unit": "KW"},
        {"cid": "power_b", "name": "B箱用电量", "value": 4334.1, "unit": "KWh"}
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
    
    slist = ["停机", "运行", "报警", "通信异常"]
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
            "A箱故障状态",
            "B箱故障状态",
        ]
        if (revc["did"][7] == 'a'):
            del alarms[1]
        elif (revc["did"][7] == 'b'):
            del alarms[0]
        
        if (state == 2):
            revc["alarms"]["value"] = alarms
        elif (state == 3):
            revc["alarms"]["value"] = random.sample(["CPU站号异常", "电量表站号异常"], random.randint(1, 2))
    
    else:  #short message
        cdata = cdata[0:4]

    revc["data"] = cdata
    
    return revc