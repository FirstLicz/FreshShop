#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/4/2 14:39'


import django_filters
from django.db.models import Q
from .models import Goods

class FilterFields(django_filters.rest_framework.FilterSet):
    '''
        过滤设置类
    '''
    pricemin = django_filters.NumberFilter(name='shop_price', help_text="最低价格", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')

    top_category = django_filters.NumberFilter(method='top_search_categroy')

    def top_search_categroy(self,queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_category_id=value)|Q(category__parent_category__category__parent_category_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax',]





