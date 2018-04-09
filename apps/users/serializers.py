#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/4/9 11:39'


from rest_framework import serializers
from django.contrib.auth import get_user_model
from Freshshop.settings import MOBILE_REGX
import re
from datetime import datetime,timedelta


from .models import VerifyCode

User = get_user_model()

class VerifyUserSerializer(serializers.Serializer):
    '''
        用户手机号码验证,重载某个字段序列化
        Your validate_<field_name> methods should return the validated value or raise a serializers.ValidationError
    '''
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self,mobile):

        #验证手机是否注册
        if  User.object.filter(mobile=mobile).count():
            raise serializers.ValidationError('手机已存在')

        #验证手机是否合法
        if not re.match(MOBILE_REGX,mobile):
            raise serializers.ValidationError('手机号码非法')

        #验证，验证码是否发送过一分钟
        one_minute_ago  = datetime.now() - timedelta(days=0,hours=0,minutes=1,seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago,mobile=mobile).count():
            raise serializers.ValidationError('距离上次发送时间未过60s')

        return mobile

