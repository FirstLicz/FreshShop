#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/29 14:48'


import sys
import os

pwd= os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.abspath(os.path.join(pwd,'..')))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Freshshop.settings')
import django
django.setup()


from goods.models import GoodsCategory
from db_tools.data import category_data


for rank1_cate in category_data.row_data:
    goods_cate_1 = GoodsCategory()
    goods_cate_1.code = rank1_cate['code']
    goods_cate_1.name = rank1_cate['name']
    goods_cate_1.category_type = 1
    goods_cate_1.save()

    for rank2_cate in rank1_cate['sub_categorys']:
        goods_cate_2 = GoodsCategory()
        goods_cate_2.code = rank2_cate['code']
        goods_cate_2.name = rank2_cate['name']
        goods_cate_2.category_type = 2
        goods_cate_2.parent_category = goods_cate_1
        goods_cate_2.save()

        for rank3_cate in rank2_cate['sub_categorys']:
            goods_cate_3 = GoodsCategory()
            goods_cate_3.code = rank3_cate['code']
            goods_cate_3.name = rank3_cate['name']
            goods_cate_3.category_type = 3
            goods_cate_3.parent_category = goods_cate_2
            goods_cate_3.save()