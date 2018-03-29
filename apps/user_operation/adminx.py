#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/29 10:25'


import xadmin


from user_operation.models import UserFav,UserAddress,UserLeaveMessage


class UserFavAdmin(object):
    '''
        用户收藏
    '''
    list_display = ['user','goods','add_time']
    list_filter = ['user','goods','add_time']


class UserAddressAdmin(object):
    '''
        用户地址
    '''
    list_display = ['user', 'district','address','signer_name','signer_mobile', 'add_time']
    list_filter = ['user', 'district','signer_name','signer_mobile', 'add_time']


class UserLeaveMessageAdmin(object):
    '''
        用户留言
    '''
    list_display = ['user','message_type','title','content','file','add_time']
    list_filter = ['user','message_type','title','content','add_time']



xadmin.site.register(UserFav,UserFavAdmin)
xadmin.site.register(UserAddress,UserAddressAdmin)
xadmin.site.register(UserLeaveMessage,UserLeaveMessageAdmin)
