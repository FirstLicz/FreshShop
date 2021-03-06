"""Freshshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url,include
import xadmin
from django.views.static import serve
from Freshshop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet,GoodsCategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
#注册router
router.register(r'goods', GoodsListViewSet,base_name='goods')

#配置category的url
router.register(r'categorys',GoodsCategoryViewSet,base_name='categorys')

goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    #配置静态文件url
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    url(r'^goods/',include('goods.urls' )),

    url(r'^', include(router.urls)),

    #配置url文档功能
    url(r'^docs/',include_docs_urls(title='')),

    url(r'^api-auth/', include('rest_framework.urls')),

    #rest_framework 认证TokenAuthentication
    url(r'^api-token-auth/', views.obtain_auth_token),

    #jwt登录认证接口
    url(r'^login/', obtain_jwt_token),
]
