from django.db import models
# TODO 继承自django的权限用户model
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    choice_gender = (
        ('man','男'),
        ('nv','女'),
        ('weizhi','未知'),
    )
    name = models.CharField(max_length=10,null=True,blank=True,verbose_name='姓名')
    birthday = models.DateField(null=True,blank=True,verbose_name='生日')
    gender = models.CharField(max_length=10,choices=choice_gender,default='weizhi',verbose_name='性别')
    mobile = models.CharField(null=True,blank=True,max_length=11,verbose_name='手机号')

    register_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):

    code = models.CharField(max_length=10,verbose_name='验证码')
    mobile = models.CharField(max_length=11,verbose_name='手机号码')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mobile
