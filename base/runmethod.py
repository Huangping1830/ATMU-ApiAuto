#coding:utf-8
'''
get,post封装
'''
import requests
import json

class RunMethod:
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,params=data,headers=header)
        else:
            res = requests.get(url=url,params=data)
        #print res.status_code
        return res

    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            #print "无header"
        #print res.status_code
        return res

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header).json()
        if method == 'get':
            res = self.get_main(url,data,header).json()
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        #request_res = json.dumps(res.json())
        #return

if __name__ == '__main__':
    run = RunMethod()
    url = "http://118.89.213.148:8995/api/personal_profile/info"
    data = {
        "person_id":"79d7ba95-3ebb-11e8-b5f3-0a58ac130503",
         "shop_id":"e415cbf3-f52e-11e7-acb2-0a58ac130221"
    }
    header={
        "Content-Type": "application/json",
        "cookie":"_tman_cp_session=Vkhyd0JHNHMyd0dZZWZYSXhuNGEzNEE5ZWlqUDBrdk56Nk11RVRoY2NIZGhKQzhYVFZodGpYZkZsZnJOTHYrS2ZuaFZwMTI0b0J5dXBDUmxnU1VOSVhiWVhVTHFvc0llM3Jmd2NOSTFxK1l1bGtXOElIVFI1Y1BadkN6cXZUMlp2Sk1mRUlvMkRSYW1oKyt5MTBGdWtpVFNFZHF2L1JOL0ZyRWhxbHltdWFXQWJoZ3RFaEJKZVNvcExobmVOUTBNL2M4TW9ta1g1Q2RnY2x5T1RCTnVFQTVyRFZIeHRFQUhLanluSzZOYUdMenN5aXVsM0l1Zmlqb0l1b3o0bHBoMGdiY3RzNmx2bHd6ZGhJN3l6c0djanREdmZUMnpKWkd1bjdIa1phclZaQ3VOQm5zWjNRTEZiRXJIa3d4SldORlpreDhJdzBOVDE0aEJFZ1dPWVYzWHRBR2U5ZFFXRndYN0JUVGN0MnVPRDA4UjlEQXlKZGRESzdyOWR6cC9VeW1aNHRWTjZQeTNJd1YrTW45bzdBNXZ2a0k2SGhWaVpCZVoxakZSUVBocTFJeFZqRWpLN1BhQTB3V014blk5Y2hyZkNDQ0dDSGxwNUdQRTFJTlFDK2I2b2NkQlJvTkpBNzJobUx3VVNUc0JuZWxDMmJZSjZScmRUNlB1ZEVCN0FhcXNEMHZVT1RMMFEvNnFTZ2RVWDZ3bml0b01Gd05PcllBd2VhVXl4TzdHbWZBPS0tTDAzcTR2VnNtL1R4dS9ENXd0TjFpZz09--8a9adba9c7995f92e76a84facdee8f97fc251d23"
    }
    res = run.run_main('get',url,data,header)
    print(res)
