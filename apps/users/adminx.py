#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/28 14:43'


import xadmin
from xadmin import views

from django.contrib.auth import get_user_model

from users.models import VerifyCode

UserProfile = get_user_model()


class BaseSetting(object):
    # 显示主题
    enable_themes = True
    use_bootswatch = True

class XdminSettings(object):
    site_title = '生鲜网'
    site_footer = '生鲜网'
    #menu_style = 'accordion'   #可折叠的


class UserProfileAdmin(object):
    list_display = ['username','name','birthday','mobile','gender','email','last_login','is_active']
    search_list = ['username','name','birthday','mobile','gender','email','last_login','is_active']
    list_filter = ['username','name','birthday','mobile','gender','email','last_login','is_active']

class VerifyCodeAdmin(object):
    '''
        验证码
    '''
    list_display = ['code','mobile','add_time']
    search_list = ['code','mobile']
    list_filter =  ['code','mobile','add_time']



#注册到后台
xadmin.site.register(VerifyCode,VerifyCodeAdmin)
#卸载系统用户
xadmin.site.unregister(UserProfile)
#重新注册user
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)  #配置主题功能
xadmin.site.register(views.CommAdminView,XdminSettings) #配置网站title