


class MailFile(object):
    def __init__(self):
        pass

    def checkfail(self,response,hope_response):
        pass


class CheckResponseHope(object):
    def __init__(self):
        pass

    def check_response_hope_key(self, response={}, hope_response={}):
        temp_data = {}
        for n1 in hope_response:
            print("n1:", n1)
            # 如果值是字典类型
            if isinstance(hope_response[n1], dict):
                print("dict")
                if not CheckResponseHope().check_response_hope_key(response=response.get(n1)
                                                                     ,hope_response=hope_response[n1]):
                    MailFile().checkfail(response=response.get(n1), hope_response=hope_response[n1])
                    return False
                raise '{},{}'.format(hope_response[n1], response[n1])

            # 如果值是列表类型
            elif isinstance(hope_response[n1], list):
                print("list")
                for hope_index, hope_listValue in enumerate(hope_response[n1]):
                    # print "hope_index:",hope_index
                    # print "hope_listValue:",hope_listValue
                    for response_index, response_listValue in enumerate(response[n1]):
                        # print "response_index:",response_index
                        # print "response_listValue:",response_listValue
                        if isinstance(hope_listValue, dict):
                            CheckResponseHope().check_response_hope_key(response=response[n1][response_index],
                            hope_response = hope_response[n1][response_index])
                            elif isinstance(hope_listValue, list):
                            if hope_response[n1][hope_index] == response[n1][hope_index]:
                                break
                            else:
                                MailFile().checkfail(response=response_listValue, hope_response=hope_listValue)
                                raise Exception("hope_response=" + str(hope_response[n1][hope_index]) + "\n" +
                                                "response=" + str(response[n1][response_index]))
                        else:
                            if hope_response[n1][hope_index] == response[n1][hope_index]:
                                break
                            else:
                                MailFile().checkfail(response=response[n1][hope_index],
                                                     hope=hope_response[n1][hope_index])
                                raise Exception(
                                    "hope_response=" + str(hope_listValue) + "\n" + "response=" + str(
                                        response_listValue))
            else:
                print("string")
                if response.has_key(n1):
                    continue
                else:
                    temp_data['error_data'] = '{}:{},{}:{}'.format(n1, hope_response[n1], n1, response[n1])
                    # 发送邮件
                    MailFile().checkfail(response=response[n1], hope=hope_response[n1])
                    raise Exception(
                        "hope_response=" + str(hope_response[n1]) + "\n" + "response=" + str(response.get(n1)))
        return True
