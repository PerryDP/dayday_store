# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 18:07
# @Author  : Perry
# @File    : serizlizers.py
# @Software: PyCharm
'''
序列化model
'''
from rest_framework import serializers

from goods.models import Goods, GoodsCategory, Banner, GoodsImage


class GoodsSerizlizer(serializers.ModelSerializer):
    '''序列化类，类似form表单的验证 这里定义的字段要和model中定义的字段一直'''
    # name = models.CharField(max_length=10, verbose_name='类别名称')
    # code = models.CharField(max_length=10, verbose_name='代码')
    # desc = models.CharField(max_length=100, verbose_name='描述信息')
    # category_type = models.IntegerField(choices=choice_cateergory_type)
    name = serializers.CharField(max_length=10)
    goods_desc = serializers.CharField(max_length=100)
    sold_num = serializers.IntegerField()

    class Meta:
        model = Goods
        fields = '__all__'

class GoodsCategoryModelSerizlizer1(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsCategoryModelSerizlizer2(serializers.ModelSerializer):
    sub_cat = GoodsCategoryModelSerizlizer1(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsCategoryModelSerizlizer(serializers.ModelSerializer):
    sub_cat = GoodsCategoryModelSerizlizer2(many=True)
    print('***************GoodsCategoryModelSerizlizer*****************')
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsImagesSerizlizer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ('image',)


class GoodsModelSerizlizer(serializers.ModelSerializer):
    category = GoodsCategoryModelSerizlizer()
    images = GoodsImagesSerizlizer(many=True)
    class Meta:
        model = Goods
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
