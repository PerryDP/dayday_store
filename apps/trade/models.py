from django.db import models

# Create your models here.
from goods.models import Goods
from user.models import UserProfile
# TODO 通过方法获取系统的user_model
# =============获取user开始=============
from django.contrib.auth import get_user_model

user = get_user_model()


# ==============获取user结束============

class ShoppingCart(models.Model):
    '''购物车'''
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name='商品')
    nums = models.IntegerField(default=1, verbose_name='商品数量')

    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}-{}-{}'.format(self.user.name, self.goods.name, self.goods_nums)


class OrderInfo(models.Model):
    choice_pay_status = (
        ('sucess', '成功'),
        ('cancel', '取消'),
        ('daizhifu', '待支付')
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='用户')
    order_sn = models.CharField(max_length=50,null=True,blank=True, unique=True, verbose_name='订单号')
    trade_no = models.CharField(max_length=50, null=True,blank=True,verbose_name='第三方流水号')
    pay_status = models.CharField(choices=choice_pay_status, default='daizhifu', verbose_name='支付状态',max_length=50,null=True)
    post_script = models.CharField(max_length=200, verbose_name='支付留言',null=True,blank=True)

    order_mount = models.FloatField(verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True,blank=True)

    address = models.CharField(max_length=100, default='', verbose_name='地址')
    signer_name = models.CharField(max_length=100, default='', verbose_name='签收人')
    singer_mobile = models.CharField(max_length=11, default='', verbose_name='签收人电话')

    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.trade_no


class OrderGoods(models.Model):
    '''订单商品详情'''
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name='订单',related_name='goods')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
    goods_num = models.IntegerField(default=0, verbose_name='商品数量')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
