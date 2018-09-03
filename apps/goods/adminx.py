# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 23:52
# @Author  : Perry
# @File    : adminx.py.py
# @Software: PyCharm
import xadmin
from goods.models import *
from xadmin import views
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "天天生鲜后台系统"
    site_footer = "dayday_shop"
    menu_style = "accordion"







class GoodsCategoryAdmin(object):
    # 显示字段
    list_display = ["name", "code", "desc", "category_type", "parent_category",
                    "is_tab", "add_time",]
    # 搜索字段
    search_fields = ['name', ]
    # 后台列表页直接修改的字段
    list_editable = ["is_tab",'desc' ]
    # 过滤器，可以按照此列表字段筛选
    list_filter = ["name", "category_type", ]






class GoodsAdmin(object):
    # 添加字段后台样式，使用ueditor
    style_fields = {"goods_desc": "ueditor"}
    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]
class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]


xadmin.site.register(Goods,GoodsAdmin)
xadmin.site.register(GoodsCategory,GoodsCategoryAdmin)
xadmin.site.register(GoodsImage)
xadmin.site.register(Banner,BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)