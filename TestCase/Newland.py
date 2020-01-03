# -*- coding: utf-8 -*-

import requests
import datetime
from hashlib import sha1
import hmac
import base64
import json
from com.qcloudapigateway.auth import sign

SecretId = 'AKIDO0Xmu8dljfedwA6om0g87qjf0fzibzj75wiA'
SecretKey = '1tgQkmpzh1bbbf0fj73W9tqid2tqHhl9c9b8v9f6'

#订单接口
url = 'http://test.tmanai.com/order/submit'
#g顾客标签查询接口
url1='http://test.tmanai.com/person/labels'
#顾客购物历史查询接口
url2 ='http://test.tmanai.com/member/buys'

header = {
    "Content-Type": "application/json; charset=UTF-8",
    'Host': 'test.tmanai.com',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
}

Source = 'NEWLAND'
sign,dateTime = sign.getSimpleSign(Source, SecretId, SecretKey)
header['Authorization'] = sign
header['Date'] = dateTime
header['Source'] = Source

print(header)

recept_text="欢迎光临瞳孔test0101分店 流水号:1             机号:0209  收银员:001916[00门店性质:       -----------销----售-------------  货  号  单  价  数  量  金  额 93000005    3.00       1    3.00 N碳烧咖啡360ml    360ml   ****** -------------------------------- 合计           1件        3.00元 应付                      3.00元 优惠                      0.00元 积分                           0 总积分                     0.000 会员                           -------------------------------- 现金                      3.00元 找零                      0.00元 交易时间:2019-07-31 10:00:00    谢谢惠顾!欢迎下次光临!"
device_id = "DB866262040117045"
item =[{
    "product_name": "N碳烧咖啡360ml",
    # "barcode": "1230232323",
    "price": -3.00,
    "quantity": 1.00,
    "unit": "件",
    "subtotal": -3.00,
    # "user_product_id": "93000005",
    # "first_category": "咖啡test",
    # "second_category": "咖啡test",
    # "third_category": "咖啡test",
    # "manufacturer": "咖啡test",
    # "brand": "咖啡test"
  }]
if __name__ == "__main__":
    data = {
        "user_order_id": "1200000004",
        "order_type": 0,
        "preferential": 3.00,
        "total": -3.00,
        "payment": "微信",
        "payment_id_code": "test123456",
        "order_time": 1564538400000,
        "device_id": device_id,
        "manufacturer_id": "NEWLAND",
        "member_id": "test123456",
        "id_number": "20190731",
        "phone": "123456",
        "wechat": "test123456",
        "sys_type": 0,
        "member_no": "test123456",
        "receipt_text": recept_text,
        "items": []
    }
    data1={'person_id':'9d0796aa-8014-4aa5-b013-b3dea1d9abd5'}
    data2={
        'shop_code': '123',
        'person_id': '9d0796aa-8014-4aa5-b013-b3dea1d9abd5',
        'start_time':123,
        'end_time': 123,
        'page': 1,
        'page_size': 50,
    }
    json_data = json.dumps(data, ensure_ascii=False)

    r = requests.post(url, data=json_data, headers=header)
    # r = requests.get(url1, params=json_data,headers=header)
    print(r)
    print(r.text)
