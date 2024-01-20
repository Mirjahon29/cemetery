from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'main/main.html')
def task1(request):
    burials=burial.objects.all()
   
    return render(request,'main/z1.html',{'burials': burials,})

def task2(request):
    areas = area.objects.all()
    burials=burial.objects.filter()
   
    return render(request,'main/z2.html',{'areas': areas,'burials': burials,})
   
# def task2(request):
#     return HttpResponse('<h1>Задание №2</h1>')