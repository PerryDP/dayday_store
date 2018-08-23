from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class GoodsCategory(models.Model):
    '''
    商品类别
    '''
    choice_cateergory_type = (
        (1,'一级类目'),
        (2,'二级类目'),
        (3,'三级类目'),
    )

    name = models.CharField(max_length=10,verbose_name='类别名称')
    code = models.CharField(max_length=10,verbose_name='代码')
    desc = models.CharField(max_length=100,verbose_name='描述信息')
    category_type = models.IntegerField(choices=choice_cateergory_type)

    parent_catergory = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    is_tab = models.BooleanField(default=False,verbose_name='顶部显示')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '类目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
class GoodsCategoryBrand(models.Model):
    '''
    品牌
    '''
    name = models.CharField(max_length=20,verbose_name='品牌名')
    desc = models.CharField(max_length=200,verbose_name='品牌描述')
    image = models.ImageField(upload_to='brand/images/')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory,verbose_name='类别',on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=20,verbose_name='商品编码')

    name = models.CharField(max_length=20,verbose_name='商品名称')

    click_num = models.IntegerField(default=0,verbose_name='点击数')
    sold_num = models.IntegerField(default=0,verbose_name='销售数')

    fav_num = models.IntegerField(default=0,verbose_name='收藏数')

    goods_num = models.IntegerField(default=0,verbose_name='库存数量')

    market_price = models.DecimalField(default=0.0,verbose_name='原价',max_digits=11,decimal_places=2)
    price = models.DecimalField(default=0.0,verbose_name='现价',max_digits=11,decimal_places=2)
    goods_brief = models.TextField(max_length=2000,verbose_name='简描述')

    goods_desc =UEditorField(imagePath='goods/images/',filePath='goods/files/',verbose_name='商品详情')

    ship_free = models.BooleanField(default=False,verbose_name='是否免运费')

    is_new = models.BooleanField(default=False,verbose_name='是否新品')
    is_hot = models.BooleanField(default=False,verbose_name='是否热卖')

    goods_front_image = models.ImageField(upload_to='goods/fronts/',verbose_name='封面图')


    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.name
class GoodsImage(models.Model):
    '''商品轮播图'''
    category = models.ForeignKey(GoodsCategory, verbose_name='类别',null=True, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner/images/',verbose_name='图片')

    image_url = models.CharField(max_length=300,null=True,blank=True,verbose_name='图片url')

    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods,verbose_name='商品',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner',verbose_name='轮播图片')
    index = models.IntegerField(default=0,verbose_name='轮播顺序')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.goods.name