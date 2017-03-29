# coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.
from django.http import HttpResponse

def bianliang(request):
    dict = {'title': '字典数据'}
    book = BookInfo()
    book.btitle = '对象数据'
    context = {'dict': dict, 'book': book}
    return render(request, 'booktest/bianliang.html', context)


def biaoqian(request):
    list = BookInfo.objects.all()
    context = {'list': list}
    return render(request, 'booktest/biaoqian.html', context)


def guolvqi(request):
    list = BookInfo.objects.all()
    context = {'list': list}
    return render(request, 'booktest/guolvqi.html', context)


def jicheng(request):
    list = BookInfo.objects.all()
    context = {'title': 'jicheng', 'list': list}
    return render(request, 'booktest/jicheng1.html',context)


def zhuanyi(request):
    context = {'title':'<h1>hellow world</h1>'}
    return render(request ,'booktest/zhuanyi.html', context)


def csrf1(request):
    return render(request, 'booktest/csrf1.html')

    
def csrf2(request):
    return HttpResponse('ok')