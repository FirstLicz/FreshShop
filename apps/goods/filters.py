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
    name = django_filters.CharFilter(name='name',lookup_expr='iexact',help_text='模糊查找名字')

    top_category_filter = django_filters.NumberFilter(method='top_search_categroy')

    def top_search_categroy(self,queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_category_id=value)|Q(category__parent_category__category__parent_category_category_id=value))

    class Meta:
        model = Goods
        fields = ['category', 'name']





