"""daydah_store2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
import xadmin
from daydah_store2.settings import MEDIA_ROOT
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import test_goods_list, TestApiView, TestApiView2, TestApiView3, TestApiView4, TestApiView5, \
    TestApiView6, TestApiView7, CategoryViewset, BannerViewset

from rest_framework.documentation import include_docs_urls

from trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from user.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, UserAddressViewset

router = DefaultRouter()
router.register(r'goods5', TestApiView5, base_name='goods5')
router.register(r'goods6', TestApiView6, base_name='goods6')
router.register(r'goods', TestApiView7, base_name='goods')
router.register(r'categorys', CategoryViewset)
router.register(r'code', SmsCodeViewset, base_name='code')
router.register(r'users', UserViewset, base_name='users')
router.register(r'banners', BannerViewset, base_name='banners')
router.register(r'userfavs', UserFavViewset, base_name='userfav')
router.register(r'address', UserAddressViewset, base_name='address')
router.register(r'shopcarts', ShoppingCartViewset, base_name='shopcart')
router.register(r'orders', OrderViewset, base_name='orders')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('goods/', include('goods.urls')),
    # path('goods/', test_goods_list),
    path('goods1/', TestApiView.as_view()),
    path('goods2/', TestApiView2.as_view()),
    path('goods3/', TestApiView3.as_view()),
    path('goods4/', TestApiView4.as_view()),
    # path('goods5/', TestApiView5.as_view({
    #     'get':'list'
    # })),
    url(r'^', include(router.urls)),
    path('index', TemplateView.as_view(template_name="index.html"), name="index"),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 调试api
    path('api-auth', include('rest_framework.urls')),

    # 接口文档
    path('docs/', include_docs_urls(title='天天生鲜')),
    # token认证
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
]
