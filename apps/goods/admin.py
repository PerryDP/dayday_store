from django.contrib import admin

# Register your models here.
from goods.models import *

admin.site.register(GoodsCategory)
admin.site.register(Goods)
admin.site.register(GoodsCategoryBrand)
admin.site.register(GoodsImage)
admin.site.register(Banner)