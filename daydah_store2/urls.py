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
from django.views.static import serve

import xadmin
from daydah_store2.settings import MEDIA_ROOT
from goods.views import test_goods_list, TestApiView, TestApiView2, TestApiView3, TestApiView4

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('goods/', include('goods.urls')),
    path('goods/', test_goods_list),
    path('goods1/', TestApiView.as_view()),
    path('goods2/', TestApiView2.as_view()),
    path('goods3/', TestApiView3.as_view()),
    path('goods4/', TestApiView4.as_view()),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),


    # 调试api
    path('api-auth',include('rest_framework.urls')),

    # 接口文档
    path('docs/',include_docs_urls(title='天天生鲜'))
]
