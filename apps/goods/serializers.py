#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/3/30 16:34'


from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=True,required=False)
    goods_sn = serializers.CharField(max_length=80,allow_blank=True,required=False)
    describe = serializers.CharField(max_length=200,default='',allow_blank=True,required=False)
    image = serializers.ImageField(required=True)

    def create(self,validated_data):
        """
        Create and return a new `Goods` instance, given the validated data.
        """
        return Goods.objects.create(**validated_data)


    def post(self,request,validated_data):
        '''
        Update and return an existing `Snippet` instance, given the validated data.
        '''
        pass