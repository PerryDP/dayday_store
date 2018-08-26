# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 12:34
# @Author  : Perry
# @File    : pagination.py
# @Software: PyCharm
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'p'
    max_page_size = 10000