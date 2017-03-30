# coding=utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import picTest, AreaInfo
from django.core.paginator import Paginator, Page

# Create your views here.


def jingtai(request):
    return render(request, 'booktest/jingtai.html')


def index(request):
    print('=========index')
    # raise Exception('自定义异常')
    return render(request, 'booktest/index.html')


def pic1(request):
    return render(request, 'booktest/pic1.html')


def pic2(requset):
    p1 = requset.FILES['pic']
    path = settings.MEDIA_ROOT + '/booktest/' + p1.name
    # 从网络流中读取二进制数据，写入到本地
    with open(path, 'w') as pic:
        for c in p1.chunks():
            pic.write(c)
    # 保存到数据库
    pic = picTest()
    pic.pic = 'booktest/' + p1.name
    pic.save()
    return HttpResponse(path + '\n OK')


def pic3(request):
    pic = picTest.objects.get(pk=1)
    context = {'p': pic}
    return render(request, 'booktest/pic3.html', context)


def page1(request, pIndex):
    list = AreaInfo.objects.filter(aParent__isnull=True)
    p1 = Paginator(list, 5)
    if pIndex == '':
        pIndex = '1'
    page = p1.page(int(pIndex))
    context = {'paginator': p1, 'page': page}
    return render(request, 'booktest/page1.html', context)


def area1(request):
    return render(request, 'booktest/area1.html')


def sheng(request):
    list = AreaInfo.objects.filter(aParent__isnull=True)
    list2 = []
    for area in list:
        list2.append([area.id, area.atitle])
    return JsonResponse({'list': list2})


def shi(request, aParent):
    list = AreaInfo.objects.filter(aParent__id=int(aParent))
    list2 = []
    for area in list:
        list2.append([area.id, area.atitle])
    return JsonResponse({'list': list2})