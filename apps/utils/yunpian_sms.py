# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 22:00
# @Author  : Perry
# @File    : yunpian_sms.py
# @Software: PyCharm
import json

import requests


class YunPian(object):
    '''
       云片网发送短信验证码接口 单例模式
       文档 https://www.yunpian.com/doc/zh_CN/domestic/single_send.html
       '''
    __instance = None
    __first_init = False

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self):
        if not self.__first_init:
            self.api_key = 'be519953e2208dcc0870863b65454207'
            self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'
            YunPian.__first_init = True

    @classmethod
    def send_sms(self,code,mobile):
        instance = YunPian()
        params = {
            'apikey':instance.api_key,
            'mobile':mobile,
            'text':'【天天商店】您的验证码是{}。如非本人操作，请忽略本短信'.format(code)
        }
        response = requests.post(instance.single_send_url,data=params)
        re_data = json.loads(response.text)

        return re_data

if __name__ == '__main__':
    resp = YunPian.send_sms('3321','18028772416')
    print(resp)