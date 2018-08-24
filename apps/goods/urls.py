# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 17:07
# @Author  : Perry
# @File    : urls.py
# @Software: PyCh0arm
from sys import path

from goods.views import test_goods_list

urlpatterns = {
    path('', test_goods_list),
}