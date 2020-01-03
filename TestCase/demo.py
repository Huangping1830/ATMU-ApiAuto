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
# url = 'http://test.tmanai.com/sp/purchase_count'
url = 'http://test.tmanai.com/sp/purchase_order'
header = {
    "Content-Type": "application/json; charset=UTF-8",
    'Host': 'test.tmanai.com',
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
    data = {
        "user_id": "123456",
        "organization_id": 144,
        "shop_id": "aeee5950-3126-0137-759c-0a58ac100332",
        "cycle_type": "month",
        # "from_date": "2019-06-17",
        # "to_date": "2019-06-23"
        "from_date": "2019-06-01",
        "to_date": "2019-06-30"
    }
    json_data = json.dumps(data, ensure_ascii=False)

    r = requests.post(url, data=json_data, headers=header)
    print(r)
    print(r.text)
