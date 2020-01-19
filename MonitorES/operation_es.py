#coding:utf-8

from elasticsearch import Elasticsearch


def connect_es(body):
    # 连接es时host只写ip
    es_host_test = "140.143.193.82"
    es = Elasticsearch([{"host":es_host_test,"port":28995}])
    # print(es.cluster.state())

    # body = {"from":0,"size":10,"sort":[],"query":{"bool":{"must":[{"term":{"organization_id":{"value":"284"}}},{"term":{"person_id":{"value":"9d0796aa-8014-4aa5-b013-b3dea1d9abd5"}}}]}},"aggs":{}}
    res = es.search(index="customerLable", body=body)
    # 获取返回数据总量
    ques_count = res['hits']['total']
    # 获取返回数据
    data = res['hits']['hits'][0]
    _source = data["_source"]
    createdAt = _source["createdAt"]
    print(ques_count,data)
    print(createdAt)
    return createdAt




