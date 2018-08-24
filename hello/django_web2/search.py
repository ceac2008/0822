#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
def search_form1(request):
    return render(request,'django_web2/search1.html')

def search1(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def search_form2(request):
    return render(request,'django_web2/search2.html')

def search2(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request,'django_web2/search2.html', ctx)
