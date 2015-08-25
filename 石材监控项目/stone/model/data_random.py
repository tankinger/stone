#!/usr/bin/python
#encoding=utf-8

import random
import sys
reload (sys)
sys.setdefaultencoding('utf-8')

class Random(object):
    def __init__(self,dev_name='排锯'):
        self.dev_name = dev_name
        
    
        
    def Day_data(self):
        import random
        day_json_list=[]
        for i in range(4):
            data_random1 = random.randint(0,1000)
            data_random2 = random.randint(0,1000)
            data_random3 = random.randint(0,1000)
            
            
            day_elements = {'element0':'一班','element1':'二班','element2':'三班','element3':'总量'}

            keyword = 'element%s'  % i
            if keyword !='element3':
                day_json = {'Item_information':day_elements.get(keyword),'Yield':data_random1,'Energy_consumption':data_random2,'Unit_energy_consumption':data_random3}
            else:
                total_Yield=total_Energy_consumption=total_Unit_energy_consumption = 0
                
                for j in range(len(day_json_list)):
                    
                    total_Yield = total_Yield+day_json_list[j].get('Yield')
                    total_Energy_consumption = total_Energy_consumption+day_json_list[j].get('Energy_consumption')
                    total_Unit_energy_consumption = total_Unit_energy_consumption+day_json_list[j].get('Unit_energy_consumption')
                day_json = {'Item_information':day_elements.get(keyword),'Yield':total_Yield,'Energy_consumption':total_Energy_consumption,'Unit_energy_consumption':total_Unit_energy_consumption}
            day_json_list.append(day_json)
        #print day_json_list
        return day_json_list


    def Month_data(self):
        import random
        month_json_list = []
        key_list = []
        value_list = []
        for k in range(31):
                key_element = 'day%s' % k
                value_element = k+1
                key_list.append(key_element)
                value_list.append(value_element)
        key_list.append('day31')
        value_list.append('总量')
        month_elements = dict(zip(key_list,value_list))
        
        
        for i in range(32):
            data_random1 = random.randint(0,1000)
            data_random2 = random.randint(0,1000)
            data_random3 = random.randint(0,1000)
            #month_elements = dict(zip(key_list,value_list))
            
            keyword = 'day%s' % i
            
            if keyword !='day31':
                month_json = {'Item_information':month_elements.get(keyword),'Yield':data_random1,'Energy_consumption':data_random2,'Unit_energy_consumption':data_random3}
            else:
                
                total_Yield=total_Energy_consumption=total_Unit_energy_consumption = 0
                for j in range(31):
                    total_Yield = total_Yield+month_json_list[j].get('Yield')
                    total_Energy_consumption = total_Energy_consumption+month_json_list[j].get('Energy_consumption')
                    total_Unit_energy_consumption = total_Unit_energy_consumption+month_json_list[j].get('Unit_energy_consumption')
                
                month_json = {'Item_information':month_elements.get(keyword),'Yield':total_Yield,'Energy_consumption':total_Energy_consumption,'Unit_energy_consumption':total_Unit_energy_consumption}

            month_json_list.append(month_json)
        #print month_json_list
        return month_json_list
        #print len(month_json_list)

        
    def Year_data(self):
        import random
        year_json_list = []
        key_list = ['month0','month1','month2','month3','month4','month5','month6','month7','month8','month9','month10','month11','month12']
        value_list = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月','总量']
        year_elements = dict(zip(key_list,value_list))
        
        for i in range(13):
            data_random1 = random.randint(0,1000)
            data_random2 = random.randint(0,1000)
            data_random3 = random.randint(0,1000)
        
            keyword = 'month%s' % i
            if keyword !='month12':
                year_json = {'Item_information':year_elements.get(keyword),'Yield':data_random1,'Energy_consumption':data_random2,'Unit_energy_consumption':data_random3}
            else:
                total_Yield=total_Energy_consumption=total_Unit_energy_consumption = 0
                for j in range(12):
                    total_Yield = total_Yield+year_json_list[j].get('Yield')
                    total_Energy_consumption = total_Energy_consumption+year_json_list[j].get('Energy_consumption')
                    total_Unit_energy_consumption = total_Unit_energy_consumption+year_json_list[j].get('Unit_energy_consumption')
                year_json = {'Item_information':year_elements.get(keyword),'Yield':total_Yield,'Energy_consumption':total_Energy_consumption,'Unit_energy_consumption':total_Unit_energy_consumption}
            year_json_list.append(year_json)
        #print year_json_list
        return year_json_list
        #print len(year_json_list)

    def monitor_data_paiju(self):
        import random
        monitor_data_list = []
        title_data = [{'Day_output':'今日产量',},{'Instant_power':'即时功率'},{'Instant_current':'即时电流'},\
                      {'speed':'切割速度'},{'Unit_energy_consumption':'单位能耗'},{'Day_power_consumption':'今日用电量'},\
                      {'Flywheel_speed':'飞轮转速'},{'efficiency':'切削效率'},{'Operating_condition':'运行状况'},{'Fault_alarm':'故障报警'}
                      ]

        key_list = ['Day_output_data','Instant_power_data','Instant_current_data','speed_data',\
                    'Unit_energy_consumption_data','Day_power_consumption_data','Flywheel_speed_data',\
                    'efficiency_data','Operating_condition_data','Fault_alarm_data'
                    ]
        j=0
        for i in title_data:
            data_random1 = random.randint(0,1000)
            data_random9 = random.randint(0,2)
            data_random10 = random.randint(1,4)
            data_random11 = random.randint(1,4)
            data_random12 = random.randint(1,4)
            data_random13 = random.randint(1,4)
            
            keyword = i.keys()[0]              ###获取键###
            value = i[keyword]                 ###获取键对应的值####
        
            if keyword == 'Fault_alarm':       ###构造不同的json数据### 
                monitor_json = {keyword:value,key_list[j]:[data_random10,data_random11,data_random12,data_random13]} 
                
            elif keyword == 'Operating_condition':
                monitor_json = {keyword:value,key_list[j]:data_random9}
                
            else:
                monitor_json = {keyword:value,key_list[j]:data_random1}
            j+=1
            monitor_data_list.append(monitor_json)                           ####构造列表####
#        print monitor_data_list
        return monitor_data_list


    def monitor_data_moji(self):
        import random
        monitor_data_list = []
        title_data = [{'Day_output':'今日产量',},{'Instant_power':'即时功率'},{'Instant_current':'即时电流'},\
                      {'speed':'抛光速度'},{'Unit_energy_consumption':'单位能耗'},{'Day_power_consumption':'今日用电量'},\
                      {'Flywheel_speed':'飞轮转速'},{'efficiency':'磨抛效率'},{'Operating_condition':'运行状况'},{'Fault_alarm':'故障报警'}
                      ]

        key_list = ['Day_output_data','Instant_power_data','Instant_current_data','speed_data',\
                    'Unit_energy_consumption_data','Day_power_consumption_data','Flywheel_speed_data',\
                    'efficiency_data','Operating_condition_data','Fault_alarm_data'
                    ]
        j=0
        for i in title_data:
            data_random1 = random.randint(0,1000)
            data_random9 = random.randint(0,2)
            data_random10 = random.randint(1,4)
            data_random11 = random.randint(1,4)
            data_random12 = random.randint(1,4)
            data_random13 = random.randint(1,4)

            keyword = i.keys()[0]              ###获取键###
            value = i[keyword]                 ###获取键对应的值####

            if keyword == 'Fault_alarm':       ###构造不同的json数据###
                monitor_json = {keyword:value,key_list[j]:[data_random10,data_random11,data_random12,data_random13]}

            elif keyword == 'Operating_condition':
                monitor_json = {keyword:value,key_list[j]:data_random9}

            else:
                monitor_json = {keyword:value,key_list[j]:data_random1}
            j+=1
            monitor_data_list.append(monitor_json)                           ####构造列表####
#        print monitor_data_list
        return monitor_data_list


    def monitor_data_bujx(self):
        import random
        monitor_data_list = []
        title_data = [{'Day_output':'今日产量',},{'Instant_power':'即时功率'},{'Instant_current':'即时电流'},\
                      {'speed':'补胶速度'},{'Unit_energy_consumption':'单位能耗'},{'Day_power_consumption':'今日用电量'},\
                      {'Temperature':'温度'},{'Humidity':'湿度'},{'efficiency':'生产效率'},\
                      {'Operating_condition':'运行状况'},{'Fault_alarm':'故障报警'}
                      ]

        key_list = ['Day_output_data','Instant_power_data','Instant_current_data','speed_data',\
                    'Unit_energy_consumption_data','Day_power_consumption_data','Temperature_data',\
                   'Humidity_data','efficiency_data','Operating_condition_data','Fault_alarm_data'
                    ]
        j=0
        for i in title_data:
            data_random1 = random.randint(0,1000)
            data_random9 = random.randint(0,2)
            data_random10 = random.randint(1,4)
            data_random11 = random.randint(1,4)
            data_random12 = random.randint(1,4)
            data_random13 = random.randint(1,4)

            keyword = i.keys()[0]              ###获取键###
            value = i[keyword]                 ###获取键对应的值####

            if keyword == 'Fault_alarm':       ###构造不同的json数据###
                monitor_json = {keyword:value,key_list[j]:[data_random10,data_random11,data_random12,data_random13]}

            elif keyword == 'Operating_condition':
                monitor_json = {keyword:value,key_list[j]:data_random9}

            else:
                monitor_json = {keyword:value,key_list[j]:data_random1}
            j+=1
            monitor_data_list.append(monitor_json)                           ####构造列表####
        #print monitor_data_list
        return monitor_data_list
        
if __name__ == '__main__':
    random = Random()
    #random.Day_data()
    #random.Month_data()
    #random.Year_data()
    random.monitor_data_moji()
