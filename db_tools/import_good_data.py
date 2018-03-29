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



from goods.models import Goods


goods_all  = Goods.objects.all()

print(goods_all)


