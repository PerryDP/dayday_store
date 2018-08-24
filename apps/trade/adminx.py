# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 13:32
# @Author  : Perry
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from trade.models import *







xadmin.site.register(ShoppingCart)
xadmin.site.register(OrderInfo)
xadmin.site.register(OrderGoods)
