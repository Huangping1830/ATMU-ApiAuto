# -*- coding: utf-8 -*-

from urllib import parse
import requests
from com.qcloudapigateway.auth import sign

SecretId = 'AKIDNl6mejG7p5IEA04532KGX1I8P197PuFHa8XK'
SecretKey = '9cFwI5xv97ilF4v6PtJ0L5HkzEu4C97Q65tsKET4'

#POI - 地理位置影响 - 门店周边客流来源构成
url001='http://cloud.tmanai.com/shop/poi/flow_parse'

#POI - 地理位置影响 - 周边门店
url002='http://cloud.tmanai.com/shop/poi/around_shops'

header = {
    "Content-Type": "application/json; charset=UTF-8",
    'Host': 'cloud.tmanai.com'
}

Source = 'yousali'
sign,dateTime = sign.getSimpleSign(Source, SecretId, SecretKey)
header['Authorization'] = sign
header['Date'] = dateTime
header['Source'] = Source

print(header)

if __name__ == "__main__":
    url="https://cloud.tmanai.com/shop/pct"
    data1= {
      "organization_id": "92",
      "shop_id":"1fc9d22e-93f7-4704-9e58-7283f3533821",
      "cycle_type": "week"
    }
    url_data111 = parse.urlencode(data1)
    url_data111=url_data111.replace('%27',"%22")
    print(type(url_data111))
    print(url_data111)

    url_data1 ='day=7&request_id=&statistical=%5B%7B%22category%22%3A900%2C%22type%22%3A902%7D%2C%7B%22category%22%3A800%2C%22type%22%3A801%7D%5D&organization_id=100'
    url_data2 ='request_id=123456&day=7&statistical=%5B%7B%22category%22%3A900%2C%22type%22%3A901%7D%5D&organization_id=100'
    # url_data = parse.urlencode(data1)
    # print(url_data)
    r1 = requests.get(url=url,params=url_data111,headers=header)
    r2 = requests.get(url=url,params=url_data2,headers=header)
    print(r1.url)
    print(r1.text)
    print(r2.url)
    print(r2.text)
