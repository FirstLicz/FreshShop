#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/29 14:24'

import sys
import os

pwd= os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.abspath(os.path.join(pwd,'..')))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Freshshop.settings')
import django
django.setup()


from db_tools.data import product_data
from goods.models import Goods,GoodsBannerImage,GoodsCategory


for product in product_data.row_data:
    goods = Goods()
    goods.name = product['name']
    goods.market_price = float(int(product['market_price'].replace('￥','').replace('元','')))
    goods.shop_price = float(int(product['sale_price'].replace('￥','').replace('元','')))
    goods.goods_detail=product['goods_desc'] if product['goods_desc'] is not None else ''
    goods.desc = product['desc'] if product['desc'] is not None else ''
    goods.image = product['images'][0] if product['images'][0] is not None else ''

    category_name = product['categorys'][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()
    for image in product['images']:
        goods_image = GoodsBannerImage()
        goods_image.goods = goods
        goods_image.image = image
        goods_image.save()



