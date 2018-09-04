# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 13:52
# @Author  : Perry
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from goods.serizlizers import GoodsSerizlizer
from user_operation.models import UserFav, UserAddress


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerizlizer()

    class Meta:
        model = UserFav
        fields = ("goods", "id",)
class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已经收藏过了'
            )
        ]


        model = UserFav
        # fields = ('user', 'goods','id')
        fields = '__all__'

class UserAddressSer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = '__all__'
