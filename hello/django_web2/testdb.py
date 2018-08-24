#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django_web2.models import Person


# 数据库操作
def testdb(request):
    test1 =Person(name='李四',age=19,pp=99)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
def deldb(request):
    test1 =Person.objects.get(id=2)
    test1.delete()
    return HttpResponse("<p>删除成功！</p>")
def updatedb(request):
    test1 =Person.objects.get(id=1)
    test1.name='李小'
    test1.save()
    test1.age=18
    test1.save()
    '''也可以
    # 另外一种方式
    Person.objects.filter(id=1).update(name='Google',age=99)
    
    # 修改所有的列
    # Person.objects.all().update(name='Google')
    '''
    return HttpResponse("<p>修改成功！</p>")

def finddb(request):
    # 初始化
    response = ""
    response1 = ""
    # 获取单个对象
    #response3 = Person.objects.get(id=6)
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Person.objects.all()
    for var in list:
       response1 +=var.name+" "+ str(var.age)+" "+str(var.pp)+" <br>"
    response = response1
    return HttpResponse("<p>" + response + "</p>")