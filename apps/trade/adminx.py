#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/28 16:01'


import xadmin

from trade.models import ShoppingCart,OrderInfo,OrderGoods


class ShoppingCartAdmin(object):
    '''
        购物车
    '''
    list_display = ['goods','nums','add_time',]
    list_filter = ['goods','nums','add_time',]


class OrderInfoAdmin(object):
    '''
        订单详情
    '''
    list_display = ['order_sn','trade_no','pay_status','post_message','order_mount','pay_time','address','signer_name','signer_mobile','add_time',]
    list_filter = ['order_sn','trade_no','pay_status','order_mount','pay_time','signer_name','signer_mobile','add_time',]

xadmin.site.register(ShoppingCart,ShoppingCartAdmin)
xadmin.site.register(OrderInfo,OrderInfoAdmin)

