import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from goods.models import Goods, GoodsCategory, Banner
from goods.filters import GoodsFilters
# TODO model_to_dict可以对model 方便的序列化，但是不支持Datetime类型
from django.forms.models import model_to_dict
# TODO serializers可以将所有格式的model序列化成json字符串serializers.serialize('json',model)
from django.core import serializers

from goods.serizlizers import GoodsSerizlizer, GoodsModelSerizlizer, GoodsCategoryModelSerizlizer, BannerSerializer


def test_goods_list(request):
    goods = GoodsCategory.objects.all()[:10]

    Goods.objects.all().delete()

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
    page_size = 12
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 10000



class TestApiView4(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerizlizer
    # pagination_class = LargeResultsSetPagination


class TestApiView5(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerizlizer


class TestApiView6(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerizlizer

    def get_queryset(self):
        price_gt = self.request.query_params.get('price_gt', 0)
        return self.queryset.filter(price__gt=price_gt)


class TestApiView7(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerizlizer
    # 过滤器类型，DjangoFilterBackend 为精确过滤，
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter
                       )
    filter_class = GoodsFilters
    search_fields = ('name','shop_price')
    ordering_fields = ('shop_price','sold_num')
    # 认证
    # authentication_classes = ( JSONWebTokenAuthentication,)
    pagination_class = LargeResultsSetPagination
    # filter_fields =('name','goods_num')
    ordering = 'add_time'

class CategoryViewset(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    '''类别信息'''
    queryset = GoodsCategory.objects.filter(category_type=1)
    # print('=========',queryset)
    serializer_class = GoodsCategoryModelSerizlizer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer