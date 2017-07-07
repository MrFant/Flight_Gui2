#!/usr/bin/python
import sys
import Flight_No
import Flight_Price
import time
import Email_script
price1=0
price2=0
while(True):
    a,b=Flight_No.find(sys.argv[1],sys.argv[2])
    a=Flight_Price.Get_Citycode(a.encode('utf-8'))
    b=Flight_Price.Get_Citycode(b.encode('utf-8'))
    s=Flight_Price.Flight(a,b)
    date=sys.argv[2]
    date=date[:4]+'-'+date[4:]
    date=date[:7]+'-'+date[7:]
    s.Search(date)
    for i in s.Info:
        if i['fn']==sys.argv[1]:
            price2=i['lp']
    if price2==0:
        sys.exit(0)

    if price1==price2:
        time.sleep(60*10)
    else:
        content="Price change!\nLast time:"+str(price1)+"\nNow:"+str(price2)
        Email_script.Post_Email(content,sys.argv[3])
        price1=price2

