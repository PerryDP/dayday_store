# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 13:32
# @Author  : Perry
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from user.models import UserProfile, VerifyCode

# xadmin.site.register(UserProfile)
xadmin.site.register(VerifyCode)