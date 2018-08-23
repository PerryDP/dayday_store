from django.db import models

# Create your models here.
from goods.models import Goods
from user.models import UserProfile


class UserFav(models.Model):
    '''用户收藏表'''
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING, verbose_name='收藏的商品')

    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserLeavingMessage(models.Model):
    '''用户留言表'''
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)

    msg_type = models.CharField(max_length=20, default='', verbose_name='留言类型')

    message = models.TextField(verbose_name='留言信息')

    subject= models.CharField(max_length=50,verbose_name='留言主题')
    file = models.FileField(upload_to='levingMessage/')

    class Meta:
        verbose_name = '用户留言表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):

    '''用户收获地址'''

    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    district = models.CharField(max_length=100,verbose_name='区域')

    address = models.CharField(max_length=100,verbose_name='详细地址')

    signer_name = models.CharField(max_length=10,verbose_name='联系人')

    signer_mobile = models.CharField(max_length=11,verbose_name='联系人电话')

    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name
