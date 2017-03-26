# coding=utf-8
from django.shortcuts import render, redirect
# Create your views here.
from models import *
from datetime import date
from django.db.models import F, Q


def index(request):
    return render(request, 'booktest/index.html')


def list(request):
    # 查询集的两个特点：1.惰性执行；2.缓存
    # list = BookInfo.objects.all()
    # list = BookInfo.books.all()
    # list = BookInfo.books.filter(id__exact=1)
    # list = BookInfo.books.filter(btitle__contains='传')
    # list = BookInfo.books.filter(btitle__endswith='部')
    # list = BookInfo.books.filter(btitle__isnull=False)
    # list = BookInfo.books.filter(pk__in=[1, 3, 5])
    # list = BookInfo.books.filter(pk__gte=3)
    # list = BookInfo.books.exclude(pk__gte=3)
    # list = BookInfo.books.filter(bpub_date__year=1986)
    # list = BookInfo.books.filter(bpub_date__gt=date(1991, 1, 1))
    # list = BookInfo.books.filter(bpub_date__gt=date(1981, 1, 1), bread__gt=20)
    # 关 联查寻
    # list = BookInfo.books.filter(heroinfo__hcontent__contains='八')
    # list = HeroInfo.objects.filter(hbook__btitle='天龙八部')
    # F对象
    # list = BookInfo.books.filter(bread__gte=F('bcommet') * 0.5)
    # list = BookInfo.books.filter(bread__gt=10).filter(bread__gt=10)
    # Q对象
    # list = BookInfo.books.filter(Q(bread__gt=30) | Q(bcommet__gt=50))
    list = BookInfo.books.filter(~Q(bread__gt=30))
    count = BookInfo.books.count()
    print count
    # list = HeroInfo.objects.filter(hgender=True)
    context = {'list': list}
    return render(request, 'booktest/list.html', context)


def create(request):
    book = BookInfo.books.create_book('流星蝴蝶剑', date(2017, 3, 25), 0, 0)
    book.save()
    return redirect('/list/')


def area(request):
    city = AreaInfo.objects.get(pk=440100)
    context = {'city': city}
    return render(request, 'booktest/area.html', context)
