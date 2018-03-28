#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/28 14:34'


import xadmin

from goods.models import Goods,GoodsCategory,GoodsCategoryBrand,GoodsBannerImage,Banner


class GoodsAdmin(object):
    '''
        商品
    '''
    list_display = ['name','goods_sn','describe','goods_detail','free_shipping','market_price','shop_price',
                    'sales_volume','goods_nums','fav_nums','is_new','is_hot','add_time']
    search_list = ['goods_sn','free_shipping','market_price','shop_price', 'sales_volume','goods_nums','fav_nums','is_new','is_hot']
    list_filter = ['goods_sn','free_shipping','market_price','shop_price', 'sales_volume','goods_nums','fav_nums','is_new','is_hot','add_time']

    style_fields = {"goods_detail": 'ueditor'}

class GoodsCategoryAdmin(object):
    '''
        商品类别
    '''
    list_display = ['name','code','desc','category_type','is_table','add_time','parent_category']
    search_list = ['name','code','category_type','is_table','parent_category']
    list_filter = ['name','code','category_type','is_table','add_time','parent_category']


class GoodsCategoryBrandAdmin(object):
    '''
        商品商标
    '''
    list_display = ['name','desc','image','add_time', 'category',]
    search_list = ['name','desc','category',]
    list_filter = ['name','category','add_time']


class GoodsBannerImageAdmin(object):
    '''
        商品详情轮播图
    '''
    list_display = ['image','add_time', 'goods',]
    list_filter = ['add_time', 'goods',]


class BannerAdmin(object):
    '''
        首页商品轮播图
    '''
    list_display = ['image','index','add_time',]
    list_filter = ['index','add_time',]


xadmin.site.register(Goods,GoodsAdmin)
xadmin.site.register(GoodsCategory,GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand,GoodsCategoryBrandAdmin)
xadmin.site.register(GoodsBannerImage,GoodsBannerImageAdmin)
xadmin.site.register(Banner,BannerAdmin)
