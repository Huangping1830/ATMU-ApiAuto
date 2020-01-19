#coding:utf-8

import json
import requests
from CommomUtil.operation_json import OperationJson
from com.qcloudapigateway.auth import signl


def get_header():
    SecretId='AKID2Xmbgqi8HmtMo39y8qL1Qqm3iflMYvzzi82g'
    SecretKey='6g7yRl8lrpJfxcWk6Mho8f0ro3d4XFaug9iF5Rki'
    # SecretId = "AKIDo2lqi8zKljXqoIUs8MbwBSs6z9vAm96B5vI"
    # SecretKey = "bypi4UFa5xd8Oozj0kk0hbAfjrg3px3s22effni0"
    header = {
        'Accept-Encoding': 'Accept-Encoding: gzip, deflate',
        'Content-Type': 'application/json; charset=UTF-8',
    }
    Source = '85272f64-da61-44c6-86fc-83a1adcbd8f3'
    sign, dateTime = signl.getSimpleSign(Source, SecretId, SecretKey)
    header['Authorization'] = sign
    header['Date'] = dateTime
    header['Source'] = Source
    return header

def pull2es(data):
    url = "https://cloud.atmuai.com/api/v3/person/update"
    json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
    r = requests.post(url, data=json_data, headers=get_header())
    print(r.text)


if __name__ =='__main__':
    opjson = OperationJson("data.json")
    data=opjson.get_data('RECORDS')
    print(len(data))
    for i in range(len(data)):
        print(data[i])
        pull2es(data[i])


