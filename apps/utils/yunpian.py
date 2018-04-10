#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/4/9 10:59'


import requests,json
from Freshshop import settings

class YunPian(object):
    '''
        云片网发送短信
    '''
    def __init__(self,code):
        self.SMS_key = settings.SMS_APIKEY
        self.url = 'https://sms.yunpian.com/v2/sms/single_send.json'
        self.code = code

    def send_code(self,mobile):
        '''
        method:POST请求
        '''
        param = {
            "apikey":self.SMS_key,
            "mobile":mobile,
            "text":"【生鲜网】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=self.code),
        }
        response =  requests.post(url=self.url,data=param)
        result = json.loads(response.text)
        return result


if __name__ == '__main__':
    from utils.utils import VerificationCode
    code = VerificationCode()
    print(code)
    test = YunPian(code)
    result = test.send_code('18795871150')
    print(result)

