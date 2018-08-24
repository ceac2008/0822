from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'django_web2/index.html')

def base(request):
    return render(request,'django_web2/base.html')