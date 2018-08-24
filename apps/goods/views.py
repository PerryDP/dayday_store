import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Goods, GoodsCategory

# TODO model_to_dict可以对model 方便的序列化，但是不支持Datetime类型
from django.forms.models import model_to_dict
# TODO serializers可以将所有格式的model序列化成json字符串serializers.serialize('json',model)
from django.core import serializers

from goods.serizlizers import GoodsSerizlizer, GoodsModelSerizlizer


def test_goods_list(request):
    goods = GoodsCategory.objects.all()[:10]

    json_data_str = serializers.serialize('json', goods)

    json_data = json.loads(json_data_str)

    print(json_data)
    print(type(json_data))
    return JsonResponse(json_data, safe=False)


class TestApiView(APIView):

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        # goods 是一个列表所以需要配置many = True

        serializers_goods = GoodsSerizlizer(goods, many=True)

        return Response(serializers_goods.data)


class TestApiView2(APIView):
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        # goods 是一个列表所以需要配置many = True
        serializers_goods = GoodsModelSerizlizer(goods, many=True)

        return Response(serializers_goods.data)


class TestApiView3(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerizlizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'p'
    max_page_size = 10000

class TestApiView4(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerizlizer
    # pagination_class = LargeResultsSetPagination