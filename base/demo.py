# coding:utf-8
import requests
import json

class RunMain:
    def __init__(self):
        return

    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)

    def send_get(self,url,data):
        res = requests.get(url=url,data=data)
        #return json.dumps(res,indent=2,sort_keys=True)
        return res


    def send_post(self,url,data):
        res = requests.post(url=url,data=data)
        #return json.dumps(res,indent=2,sort_keys=True)
        return res

    def run_main(self,url,method,data=None):
        res = None
        if method == "get":
            res =self.send_get(url,data)
        elif method == "post":
            res = self.send_post(url,data)
        return res

if __name__ == "__main__":
    url ="http://web-api-test.energymost.com/api/vee/getdatastructure"
    data ={
        "UserId":312135,
        "CustomerId":347373
    }
    method = "post"
    run = RunMain()
    r = run.run_main(url,method,data)
    print r.json()
    print r.status_code







