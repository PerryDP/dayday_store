# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 0:20
# @Author  : Perry
# @File    : signals.py
# @Software: PyCharm
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from user.models import UserProfile


@receiver(post_save, sender=UserProfile)
def create_user(sender, instance=None, created=False, **kwargs):
    '''django信号 加密用户密码存入数据库'''
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
