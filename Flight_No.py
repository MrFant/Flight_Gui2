#!/usr/bin/python
import requests
import json
def find(fn,date):
    url='http://flights.ctrip.com/Process/FlightStatus/FindByFlightNoWithJson?flightNo='+fn+'&date='+date
    headers={
        'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0', 'Host': 'flights.ctrip.com', 'Referer': 'http://flights.ctrip.com/actualtime/fno-CZ8251/t20170626', 'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT', 'Cookie': 'Session=SmartLinkCode=U155935&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=42e8ba9b-2ae9-4b2a-b9be-2bbdf7f3c51d; _bfa=1.1495783146663.38bla2.1.1498188229345.1498295641598.6.21; page_time=1495783148951%2C1495783210832%2C1495814755716%2C1495815963722%2C1495816555781%2C1495817343697%2C1498035142887%2C1498051203731%2C1498188231016%2C1498295643686%2C1498295697814%2C1498295713607%2C1498295736847%2C1498295752563%2C1498295762580%2C1498295771376%2C1498296068672; _RF1=183.255.214.172; _RSG=p_atk8GdSi0IjRtRjcI2D8; _RGUID=0b1c9d02-2ede-4ff3-8342-4a6b5bddbb52; traceExt=campaign=CHNbaidu81&adid=index; _jzqco=%7C%7C%7C%7C1498295701522%7C1.1368503224.1495783149958.1498295773597.1498296070228.1498295773597.1498296070228.undefined.0.0.17.17; __zpspc=9.8.1498296070.1498296070.1%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; FD_SearchHistorty={"type":"S","data":"S%24%u6D77%u53E3%28HAK%29%24HAK%242017-07-20%24%u73E0%u6D77%28ZUH%29%24ZUH%24%24%24"}; Union=SID=155935&AllianceID=4897&OUID=baidu97|flight|||exact; MKT_Pagesource=PC; _bfi=p1%3D101049%26p2%3D101049%26v1%3D19%26v2%3D17; FlightIntl=Search=%5B%22Shanghai%7C%E4%B8%8A%E6%B5%B7(SHA)%7C2%7CSHA%7C480%22%5D; DomesticUserHostCity=SHA%7c%c9%cf%ba%a3; _bfs=1.11; adscityen=Danzhou; ASP.NET_SessionSvc=MTAuMTUuMTI4LjI2fDkwOTB8b3V5YW5nfGRlZmF1bHR8MTQ3MDczODMxMTM2OQ', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    response=requests.get(url=url,headers=headers).content.decode('gbk')
    response=json.loads(response)
    return response['List'][0]['DCityName'],response['List'][0]['ACityName']

if __name__=="__main__":
    find('CZ8251','20170626')
