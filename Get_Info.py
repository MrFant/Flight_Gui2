#!/usr/bin/python
#-*- coding=utf-8 -*-
import json
import requests
import sys
def Get_Info(url):
    #url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=HAK&ACity1=ZUH&DDate1='
    header = {
            'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0', 'Host': 'flights.ctrip.com', 'Cookie': 'Session=SmartLinkCode=U155935&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=42e8ba9b-2ae9-4b2a-b9be-2bbdf7f3c51d; _bfa=1.1495783146663.38bla2.1.1498295641598.1498323038753.7.28; page_time=1495783148951%2C1495783210832%2C1495814755716%2C1495815963722%2C1495816555781%2C1495817343697%2C1498035142887%2C1498051203731%2C1498188231016%2C1498295643686%2C1498295697814%2C1498295713607%2C1498295736847%2C1498295752563%2C1498295762580%2C1498295771376%2C1498296068672%2C1498296145958%2C1498323040057%2C1498323056154%2C1498323085907%2C1498323168554; _RF1=223.104.23.94; _RSG=p_atk8GdSi0IjRtRjcI2D8; _RGUID=0b1c9d02-2ede-4ff3-8342-4a6b5bddbb52; traceExt=campaign=CHNbaidu81&adid=index; _jzqco=%7C%7C%7C%7C1498295701522%7C1.1368503224.1495783149958.1498323087712.1498323170811.1498323087712.1498323170811.undefined.0.0.23.23; __zpspc=9.9.1498323041.1498323170.4%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; FD_SearchHistorty={"type":"S","data":"S%24%u6D77%u53E3%28HAK%29%24HAK%242017-07-20%24%u73E0%u6D77%28ZUH%29%24ZUH"}; Union=SID=155935&AllianceID=4897&OUID=baidu97|flight|||exact; MKT_Pagesource=PC; _bfi=p1%3D101049%26p2%3D101027%26v1%3D28%26v2%3D26; FlightIntl=Search=%5B%22Shanghai%7C%E4%B8%8A%E6%B5%B7(SHA)%7C2%7CSHA%7C480%22%5D; DomesticUserHostCity=SHA%7c%c9%cf%ba%a3; adscityen=Danzhou; ASP.NET_SessionSvc=MTAuMTUuMTI4LjI2fDkwOTB8b3V5YW5nfGRlZmF1bHR8MTQ3MDczODMxMTM2OQ; _bfs=1.6', 'Upgrade-Insecure-Requests': '1'
    }

    jscontent = requests.get(url,headers=header).content.decode('gbk')
    content = json.loads(jscontent)
    if content['lp'] == 0:
        print 'Failed!'
        sys.exit(0)
    else:
        print 'Success!'


    data = content['fis']
    return data

if __name__=="__main__":
    Get_Info(url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=HAK&ACity1=ZUH&DDate1=2017-06-26')
