from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.generic.base import View


from .serializers import GoodsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from .models import Goods


# Create your views here.

#原始serialize使用
# class GoodsList(View):
#     '''
#         通过django的view实现商品列表页,
#     '''
#     def get(self,request):
#         json_list = []
#         goods = Goods.objects.all()[:10]
#         # for good in goods:
#         #     json_dict={}
#         #     json_dict['name'] = good.name
#         #     json_dict['goods_sn'] = good.goods_sn
#         #     json_dict['category'] = good.category.name
#         #     json_dict['market_price'] = good.market_price
#         #     json_list.append(json_dict)
#         ###########model_to_dict 方法
#         from django.forms.models import model_to_dict
#         # for good in goods:
#         #     json_dict = model_to_dict(good)
#         #     json_list.append(json_dict)
#         from django.core.serializers import serialize
#         json_data = serialize('json',goods)
#         json_data = json.loads(json_data)
#         return JsonResponse(json_data,safe=False)




class GoodsList(APIView):
    """
    List all goods, or create a new good.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)

    def post(self,request,validated_data):
        '''
        Update and return an existing `Snippet` instance, given the validated data.
        '''
        pass
