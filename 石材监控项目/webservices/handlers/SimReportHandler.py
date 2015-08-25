# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json
import datetime, time
import random
import calendar

import sys
reload(sys)
sys.setdefaultencoding('gb18030')


# ��ѯ����
class reportData(tornado.web.RequestHandler):
    def get(self, fid, did, rpid):      
        revc = {
            "fid": "",
            "did": "",
            "devname": "",
            "rpid": "",
            "rptitle": "",
            "time": "",
            "error": "NULL",
            "thead": [],
            "tbody": [],
            "tend": []
        } 

        rplist = {
            "dayreport": "�ձ���",
            "monthreport": "�±���",
            "yearreport": "�걨��"
        }
        
        rphead = {
            "pg_dayreport": ["���", "����(�O)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/�O)"],
            "pg_monthreport": ["����", "����(�O)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/�O)"],
            "pg_yearreport": ["�·�", "����(�O)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/�O)"],
            "mj_dayreport": ["���", "����(�O)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/�O)"],
            "mj_monthreport": ["����", "����(�O)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/�O)"],
            "mj_yearreport": ["�·�", "����(�O)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/�O)"],
            "bjx_dayreport": ["���", "����(Ƭ)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/Ƭ)"],
            "bjx_monthreport": ["����", "����(Ƭ)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/Ƭ)"],
            "bjx_yearreport": ["�·�", "����(Ƭ)", "�ܺ�(KWh)", "��λ�ܺ�(KWh/Ƭ)"]
        }
        
        rpend = ["�ܼ�", "", "", ""]
        
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
        if (not rplist.has_key(rpid)):
            err = 'Error: report_id ' + rpid + ' not exist!'
            
        revc["fid"] = fid
        revc["did"] = did           
        revc["rpid"] = rpid 
        
        if (err == ''): 
            revc["devname"] = dlist[did]
            revc["rptitle"] = rplist[rpid]
            
            tend = rpend 
            thead = []
            if (did[0:2] == 'pg'):
                thead = rphead['pg' + '_' + rpid]
            elif (did[0:2] == 'mj'):
                thead = rphead['mj' + '_' + rpid]
            elif (did[0:3] == 'bjx'): 
                thead = rphead['bjx' + '_' + rpid]  
            
            t = self.get_argument('time')
            time = t[0:4] + "-" + t[4:6] + "-" + t[6:8]
            #print time 
                        
            if (rpid == "dayreport"):
                revc["time"] = time
            elif (rpid == "monthreport"):
                revc["time"] = time[0:7]
            elif (rpid == "yearreport"):
                revc["time"] = time[0:4]
                
            try:
                st =  datetime.datetime.strptime(time, '%Y-%m-%d')
            except:
                revc["error"] = 'Error: url_argument time format convert failed (reportData - get)'
                self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
                return
            
            tbody = self.dataReport(rpid, time, tend)
            tend = tbody.pop()
            
            revc["thead"] = thead
            revc["tbody"] = tbody
            revc["tend"] = tend
            
            
        else:
            revc["error"] = err
        
        print revc
        self.write((json.dumps(revc, ensure_ascii=False)).decode('gbk'))
    
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error in reportData." % status_code)
        
    def dataReport(self, rpid, time, rpend):
        revc = []
        num = 0
        bb = 0
        cc = 0
        if (rpid == "dayreport"):
            num = 3
            for i in range(num):
                a = str(i+1) + '��'
                b = round(random.uniform(500, 1000), 1)
                c = round(random.uniform(1500, 3000), 1)
                d = round(c/b, 1)
                revc.append([a,str(b),str(c),str(d)])
                bb = bb + b
                cc = cc + c
            dd = round(cc/bb, 1)
            revc.append([rpend[0], str(bb), str(cc), str(dd)])
 
        elif (rpid == "monthreport"):
            num = calendar.monthrange(int(time[0:4]),int(time[5:7]))[1]
            for i in range(num):
                a = str(i+1) + '��'
                b = round(random.uniform(1500, 3000), 1)
                c = round(random.uniform(4500, 9000), 1)
                d = round(c/b, 1)
                revc.append([a,str(b),str(c),str(d)])
                bb = bb + b
                cc = cc + c
            dd = round(cc/bb, 1)
            revc.append([rpend[0], str(bb), str(cc), str(dd)])
                
        elif (rpid == "yearreport"):
            num = 12
            for i in range(num):
                a = str(i+1) + '��'
                b = round(random.uniform(45000, 90000), 1)
                c = round(random.uniform(135000, 270000), 1)
                d = round(c/b, 1)
                revc.append([a,str(b),str(c),str(d)])
                bb = bb + b
                cc = cc + c
            dd = round(cc/bb, 1)
            revc.append([rpend[0], str(bb), str(cc), str(dd)])
        
        return revc
