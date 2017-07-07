#!/usr/bin/python
# -*- coding: utf-8 -*-
import Get_Info
import time
from Airport import Airport
'''
#如果出现最低价不在列出的航班中的情况，代表该最低价是中转航班
#有时候会出现与出发地和目的地不同的城市，这是携程网的航班路线推荐
'''
class Flight():
    def __init__(self,Dc,Ac):
        self.Url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1='+Dc+'&ACity1='+Ac+'&DDate1='
    def Search(self,date):
        self.Url+=date
        self.Info=Get_Info.Get_Info(self.Url)
def Get_Citycode(name):
    return Airport[name]




if __name__=="__main__":
    #Dc_name=raw_input("Please input the departure city:\n")
    #Ac_name=raw_input("Please input the arrival city:\n")
    Dc_name='海口'
    Ac_name='成都'
    Dc=Get_Citycode(Dc_name)
    Ac=Get_Citycode(Ac_name)
    s=Flight(Dc,Ac)
    Or_lp = 0
    while(True):
        s.Search()

        if s.Lp != Or_lp:
            Email_script.Post_Email(s.Info)
        else:
            time.sleep(3*3600)

        Or_lp=s.Lp





