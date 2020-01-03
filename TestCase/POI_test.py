# -*- coding: utf-8 -*-

import requests
import datetime
from hashlib import sha1
import hmac
import base64
import json
from com.qcloudapigateway.auth import sign

SecretId = 'AKIDNl6mejG7p5IEA04532KGX1I8P197PuFHa8XK'
SecretKey = '9cFwI5xv97ilF4v6PtJ0L5HkzEu4C97Q65tsKET4'

#POI - 地理位置影响 - 门店周边客流来源构成
url001='http://test.tmanai.com/shop/poi/flow_parse'

#POI - 地理位置影响 - 周边门店
url002='http://test.tmanai.com/shop/poi/around_shops'

header = {
    "Content-Type": "application/json; charset=UTF-8",
    'Host': 'cloud.tmanai.com',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
}

Source = 'yousali'
sign,dateTime = sign.getSimpleSign(Source, SecretId, SecretKey)
header['Authorization'] = sign
header['Date'] = dateTime
header['Source'] = Source

print(header)


if __name__ == "__main__":
    data001={
        "organization_id": "144",
	    "shop_id": "423ae760-6eeb-0137-f47a-0a58ac100330"
    }
    data0011 = {
         "organization_id": "144",
          "shop_id": "d73a6e20-b4db-0137-dbdd-0a58ac100118"
    }
    data002 = {
	"organization_id": "1",
	"shop_id": "21c548d0-0cc8-11e8-b049-2b66ceb5c9dc"
}
    json_data = json.dumps(data002, ensure_ascii=False)
    r = requests.post(url001, data=json_data, headers=header)

    json_data2 = json.dumps(data002, ensure_ascii=False)
    r2 = requests.post(url002, data=json_data2, headers=header)
    print(r.url)
    print(r.text)
    print(r2.url)
    print(r2.text)

