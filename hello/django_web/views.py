from django.shortcuts import render
from  django.http import  HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("欢迎学习 Hello World!!")

def hello2(request):
    context={}
    context['hello']='Hello World,我是李'
    return render(request,'hello.html',context)