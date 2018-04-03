from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.generic.base import View


from .serializers import GoodsSerializer,GoodsCategorySerializer
from .filters import FilterFields

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


import json

from .models import Goods,GoodsCategory


# Create your views here.


class GoodsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all goods, or create a new good.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    #filter_class = FilterFields
    filter_fields = ('category', 'name')
    search_fields = ('name','market_price')
    ordering_fields = ('name', 'market_price')


class GoodsCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''
        list category goods：商品分类列表
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer




