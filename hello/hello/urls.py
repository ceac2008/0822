from django.conf.urls import url
from django.contrib import admin
from django_web2.views import index #导入views.py文件中的index函数
from django_web.views import hello
from django_web.views import hello2
from django_web2.views import base
from  django_web2.testdb import testdb
from  django_web2.testdb import deldb
from  django_web2.testdb import updatedb
from  django_web2.testdb import finddb
import django_web2.search as sr
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),  # 在url中凡是以url开头的访问都使用index函数来处理该请求
    url(r'^hello/', hello),
    url(r'^hello2/', hello2),
    url(r'base.html', base),
    url(r'^testdb$', testdb),
    url(r'^deldb$', deldb),
    url(r'^updatedb$', updatedb),
    url(r'^finddb$', finddb),
    url(r'search1.html',sr.search_form1),
    url(r'search1',sr.search1),
    url(r'search2.html', sr.search_form2),
    url(r'search2', sr.search2),
]