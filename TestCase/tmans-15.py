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
#门店画像-消费笔数图表
url = 'http://test.tmanai.com/sp/purchase_order'
#门店画像-消费人次图表
url1 = 'http://test.tmanai.com/sp/purchase_count'
#门店画像-热销榜
url2 =  'http://test.tmanai.com/sp/best_selling_list'
#门店画像-运营活动商品销售件数
url3 = 'http://test.tmanai.com/sp/activity_goods_sold'
#经营看板-消费会员
url4 ='http://test.tmanai.com/sp/members_feature'

url5 ='http://test.tmanai.com/shop/shop_sales'

url6 = ''


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
        "organization_id": "144",
        "shop_id": "aeee5950-3126-0137-759c-0a58ac100332",
        "cycle_type": "month",
        # "from_date": "2019-06-17",
        # "to_date": "2019-06-23"
        "from_date": "2019-06-01",
        "to_date": "2019-06-30"
    }
    data1 = {
        "user_id": "123456",
        "organization_id": 144,
        "shop_id": "aeee5950-3126-0137-759c-0a58ac100332",
        "cycle_type": "month",
        # "from_date": "2019-06-17",
        # "to_date": "2019-06-23"
        "from_date": "2019-06-01",
        "to_date": "2019-06-30"
    }
    data2 = {
        "user_id": "123456",
        "organization_id": 144,
        "cycle_type": "month",
        # "from_date": "2019-06-17",
        # "to_date": "2019-06-23"
        "from_date": "2019-06-01",
        "to_date": "2019-06-30"
    }
    data3 ={
        "user_id": "123456",
        "organization_id": "144",
        "shop_id":"",
        "cycle_type": "month",
        # "from_date": "2019-06-17",
        # "to_date": "2019-06-23"
        "from_date": "2019-06-01",
        "to_date": "2019-06-30"
    }
    data4 ={
        "user_id": "123456",
        "organization_id": "144",
        "shop_id": "d87a43e0-6eea-0137-f478-0a58ac100330",
        "cycle_type": "week",
        "from_date": "2019-08-06",
        "to_date": "2019-08-13"
    }
    data5={

        "organization_id": "144",
        "shop_id": "aeee5950-3126-0137-759c-0a58ac100332",
        "cycle_type": "month"
    }

    json_data = json.dumps(data5, ensure_ascii=False)
    r = requests.post(url5, data=json_data, headers=header)
    print(r)
    print(r.text)
