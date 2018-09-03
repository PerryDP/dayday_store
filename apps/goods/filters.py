# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 15:43
# @Author  : Perry
# @File    : filters.py
# @Software: PyCharm
import django_filters
from django.db.models import Q
from django_filters import rest_framework

from goods.models import Goods


class GoodsFilters(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(field_name='shop_price',lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price',lookup_expr='lte')

    top_category = django_filters.NumberFilter(method='top_category_filter',)

    def top_category_filter(self,queryset,name,value):
        print('=========value========',value)
        queryset = queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
        print('=========queryset========',queryset)
        # return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

        return  queryset

    class Meta:
        model = Goods
        # fields = ['min_price','max_price']
        fields = ['name','pricemin','pricemax','is_hot','is_new']

