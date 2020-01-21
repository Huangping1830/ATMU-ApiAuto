#coding:utf-8

import json
import requests
from CommomUtil.operation_json import OperationJson
from com.qcloudapigateway.auth import signl


def get_header(Source):
    SecretId='AKID2Xmbgqi8HmtMo39y8qL1Qqm3iflMYvzzi82g'
    SecretKey='6g7yRl8lrpJfxcWk6Mho8f0ro3d4XFaug9iF5Rki'
    # SecretId = "AKIDo2lqi8zKljXqoIUs8MbwBSs6z9vAm96B5vI"
    # SecretKey = "bypi4UFa5xd8Oozj0kk0hbAfjrg3px3s22effni0"
    header = {
        'Accept-Encoding': 'Accept-Encoding: gzip, deflate',
        'Content-Type': 'application/json; charset=UTF-8',
    }
    # Source = '85272f64-da61-44c6-86fc-83a1adcbd8f3'   #92
    # Source = '60505114-6364-40b1-a530-3e6796115720'  #285
    sign, dateTime = signl.getSimpleSign(Source, SecretId, SecretKey)
    header['Authorization'] = sign
    header['Date'] = dateTime
    header['Source'] = Source
    return header

def PersonUpdate(person_id,shop_id,organization_id,label_name,label_value,header):
    data = {
        "person_id": person_id,
        "organization_id": organization_id,
        "shop_id": shop_id,
        "labels": [
            {
                "label_name": label_name,
                "label_value": label_value
            }
        ]
    }
    print(data)
    url = "https://cloud.atmuai.com/api/v3/person/update"
    json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
    r = requests.post(url, data=json_data, headers=header)
    print(r.text)


def Opjson_data():
    opjson_data = OperationJson("data.json")
    opjson_market_id = OperationJson("market_id.json")
    data=opjson_data.get_data('RECORDS')
    market = opjson_market_id.get_data('RECORDS')
    print(len(data))
    # print(market)
    for i in range(len(data)):
        person_id = data[i]['person_id']
        shop_id = data[i]['shop_id']
        organization_id = data[i]['organization_id']
        label_name = data[i]['label_name']
        label_value = data[i]['label_value']
        for j in range(len(market)):
            if organization_id == market[j]['id']:
                # secret_id =market[j]['secret_id']
                # secret_key = market[j]['secret_key']
                source = market[j]['market_id']
                header = get_header(source)
                # print(organization_id,secret_id,secret_key,source)
                break
        PersonUpdate(person_id, shop_id, organization_id, label_name, label_value, header)

def test_demo():
    test_data_285={"person_id": "35b6d89e-aebd-49c0-9b3b-731fd6ed0e30",
              "shop_id": "c37269f3-d393-4864-afa7-0d159f8c114c",
                "labels": [{"label_name": "外卖", "label_value": "外卖"}]}
    Source_285 = '60505114-6364-40b1-a530-3e6796115720'
    header = get_header(Source_285)
    url = "https://test.atmuai.com/api/v3/person/update"
    json_data = json.dumps(test_data_285, ensure_ascii=False).encode("utf-8")
    r = requests.post(url, data=json_data, headers=header)
    print(r.text)

def cloud_demo():
    # cloud_data_92 = {"person_id": "3ec40f75-ef77-475e-97ba-473fd6180d19",
    #                  "shop_id": "1fc9d22e-93f7-4704-9e58-7283f3533821",
    #                  "labels": [{"label_name": "外卖小哥", "label_value": "外卖小哥"}]}
    cloud_data_100= {"person_id": "36d69215-295c-4002-a711-5903a0402295",
                     "shop_id": "3f470adc-ce6c-42ac-9e98-f2a531375df0",
                     "labels": [{"label_name": "店员", "label_value": "店员"}]}
    # Source = '85272f64-da61-44c6-86fc-83a1adcbd8f3' #92
    Source_100 ='fc371d47-dc90-41e9-b292-6daffc6240e0'
    header = get_header( Source_100)
    url = "https://cloud.atmuai.com/api/v3/person/update"
    json_data = json.dumps(cloud_data_100, ensure_ascii=False).encode("utf-8")
    r = requests.post(url, data=json_data, headers=header)
    print(r.text)


if __name__ =='__main__':
    # cloud_demo()
    print("a")






