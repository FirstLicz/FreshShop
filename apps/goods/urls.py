#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/30 10:56'


from django.conf.urls import url

from goods.views import GoodsList


urlpatterns = [
    url(r'^list$',GoodsList.as_view(),name='goods-list'),
]


