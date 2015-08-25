# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json
import datetime, time
import random

import sys
reload(sys)
sys.setdefaultencoding('gb18030')

# 可历史查询设备
class hsDevices(tornado.web.RequestHandler):
    def get(self, fid):
        if (fid != '0001'):
            self.write('Error: fab_id not exist (hsDevContent - get) ')
            return
        revc = {
            "fid": "0001",
            "devices": [
                {"did": "pg0001", "name": "1#排锯"},
                {"did": "mj0001", "name": "1#磨机" },
                {"did": "bjx0001a", "name": "1#立体补胶线A箱"},
                {"did": "bjx0001b", "name": "1#立体补胶线B箱"}
            ]
        }
        #print (json.dumps(revc, ensure_ascii=False)).decode('gbk')
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevices." % status_code)
        
# 可历史查询设备的内容        
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
                    {"cid": "currentflow", "name": "瞬时电流", "unit": "A"},
                    {"cid": "mompower", "name": "瞬时总功率", "unit": "KW"},
                    {"cid": "fwrotspeed", "name": "飞轮转速", "unit": "RPM"},
                    {"cid": "fwcurrflow", "name": "飞轮电流", "unit": "A"},
                    {"cid": "cutspeed", "name": "切割速度", "unit": "cm/h"},
                    {"cid": "cutratio", "name": "切割效率", "unit": "m2/h"},
                    {"cid": "totalpower", "name": "总用电量", "unit": "KWh"}
                ]
            }
        elif (did == 'mj0001'):
            revc = {
                "fid": "0001",
                "did": "mj0001",
                "contents": [
                    {"cid": "currentflow", "name": "瞬时电流", "unit": "A"},
                    {"cid": "mompower", "name": "瞬时总功率", "unit": "KW"},
                    {"cid": "beltspeed", "name": "皮带速度", "unit": "cm/min"},
                    {"cid": "beamswingspeed", "name": "横梁摆动速度", "unit": "m/min"},
                    {"cid": "grindratio", "name": "磨抛效率", "unit": "m2/h"},
                    {"cid": "totalpower", "name": "总用电量", "unit": "KWh"}
                ]
            }
        elif (did == 'bjx0001a'):
            revc = {
                "fid": "0001",
                "did": "bjx0001a",
                "contents": [
                    {"cid": "momcurrenta", "name": "A箱电流", "unit": "A"},
                    {"cid": "mompowera", "name": "A箱功率", "unit": "KW"},
                    {"cid": "tempea", "name": "A箱温度", "unit": "°C"},
                    {"cid": "humiditya", "name": "A箱湿度", "unit": "%"},
                    {"cid": "powera", "name": "A箱用电量", "unit": "KWh"}
                ]
            }
        elif (did == 'bjx0001b'):
            revc = {
                "fid": "0001",
                "did": "bjx0001b",
                "contents": [
                    {"cid": "momcurrentb", "name": "B箱电流", "unit": "A"},
                    {"cid": "mompowerb", "name": "B箱功率", "unit": "KW"},
                    {"cid": "tempeb", "name": "B箱温度", "unit": "°C"},
                    {"cid": "humidityb", "name": "B箱湿度", "unit": "%"},
                    {"cid": "powerb", "name": "B箱用电量", "unit": "KWh"},
                    {"cid": "totalpower", "name": "总用电量", "unit": "KWh"},
                    {"cid": "mompower", "name": "瞬时总功率", "unit": "KW"},
                    {"cid": "tacttiming", "name": "生产节拍", "unit": "min/片"}
                ]
            }
                
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in hsDevContent." % status_code)

# 查询历史数据
class hsDevData(tornado.web.RequestHandler):
    def get(self, fid, did, cid):
        if (fid != '0001'):
            self.write('Error: fab_id not exist (hsDevData - get) ')
            return
        
        revc = {
            "fid": "0001",
            "did": "pg0001",
            "devname": "1#排锯",
            "cid": "currentflow",
            "content": "瞬时电流",
            "start": "2015-07-29 14:02:35",
            "end": "2015-07-30 14:02:35",
            "error": "NULL",
            "times": [],
            "data": []
        }
        
        dlist = {
            "pg0001": "1#排锯",
            "mj0001": "1#磨机",
            "bjx0001a": "1#立体补胶线A箱",
            "bjx0001b": "1#立体补胶线B箱"    
        }
        if (dlist.has_key(did)):
            revc["did"] = did
            revc["devname"] = dlist[did]
        
        clist = {}
        if (did == 'pg0001'):
            clist = {
                "currentflow": "瞬时电流",
                "mompower": "瞬时总功率",
                "fwrotspeed": "飞轮转速",
                "fwcurrflow": "飞轮电流",
                "cutspeed": "切割速度", 
                "cutratio": "切割效率",
                "totalpower": "总用电量",
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
            
            
        elif (did == 'mj0001'):
            clist = {
                "currentflow": "瞬时电流",
                "mompower": "瞬时总功率",
                "beltspeed": "皮带速度", 
                "beamswingspeed": "横梁摆动速度",
                "grindratio": "磨抛效率",
                "totalpower": "总用电量",
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
                
        elif (did == 'bjx0001a'):    
            clist = {
                "momcurrenta": "A箱电流", 
                "mompowera": "A箱功率", 
                "tempea": "A箱温度", 
                "humiditya": "A箱湿度",
                "powera": "A箱用电量", 
            }
            if (clist.has_key(cid)):
                revc["cid"] = cid
                revc["content"] = clist[cid]
            else:
                revc["error"] = 'Error: ' + cid + ' not exist!'
                
        elif (did == 'bjx0001b'):
            clist = {
                "momcurrentb": "B箱电流", 
                "mompowerb": "B箱功率", 
                "tempeb": "B箱温度", 
                "humidityb": "B箱湿度",
                "powerb": "B箱用电量", 
                "totalpower": "总用电量", 
                "mompower": "瞬时总功率", 
                "tacttiming": "生产节拍", 
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
        
    
        

