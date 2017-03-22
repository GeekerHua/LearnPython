# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import BookInfo, HeroInfo

# Create your views here.


def index(request):
    # 最基础的方法，使用loader加载template模板。
    #     t1 = loader.get_template('booktest/index.html')
    #     return HttpResponse(t1.render(request=request))
    #     return HttpResponse('hello world')
    # 对于常用的loader加载方法，django进行了封装，使用render进行加载即可。
    context = {'title': '我是首页', 'list': range(10)}
    return render(request, 'booktest/index.html', context)


def book(request):
    #  查询所有图书信息
    list = BookInfo.objects.all()
    context = {'book': list}
    #  调用模板并返回
    return render(request, 'booktest/book.html', context)


def hero(request, id):

    b1 = BookInfo.objects.get(id=int(id))
    heros = b1.heroinfo_set.all()
    context = {'heros': heros}

    return render(request, 'booktest/hero.html', context)
