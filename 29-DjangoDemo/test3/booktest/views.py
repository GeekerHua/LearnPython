# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    return HttpResponse('hello world')


def show(request, id, title):
    return HttpResponse('%s--%s' % (id, title))


def method1(request):
    return render(request, 'booktest/method1.html')


def method2(request):
    return HttpResponse(request.method)


def method3(request):
    return HttpResponse(request.method)


def get1(request):
    return render(request, 'booktest/get1.html')


def get2(request):
    # 一键一值
    dict = request.GET
    a = dict.get('a')
    b = dict.get('b')
    c = dict['c']
    return HttpResponse('a = %s, b = %s, c = %s' % (a, b, c))


def get3(request):
    # 一键多值
    dict = request.GET
    a = dict.get('a')
    b = dict.getlist('a')
    c = dict['c']
    return HttpResponse('a = %s, a2 = %s, c = %s' % (a, b, c))


def post1(request):
    return render(request, 'booktest/post1.html')


def post2(request):
    dict = request.POST
    title = dict['title']
    gender = dict.get('gender')
    city = dict['city']
    hobby = dict.getlist('hobby')
    context = {
        'title': title,
        'gender': gender,
        'city': city,
        'hobby': hobby,
    }
    return render(request, 'booktest/post2.html', context)


def json1(request):
    return render(request, 'booktest/json1.html')


def json2(request):
    return JsonResponse({'title': 'hello', 'content': 'world'})
    # return render(request, 'booktest/json1.html');


def redirect1(request):
    # 重定向
    return HttpResponseRedirect('/')


def cookie_test(request):
    # cookie记录浏览者做了什么
    response = HttpResponse('设置cookie,查看相应报文头')
    # cookie 写入
    # response.set_cookie('title', 'hello', max_age=None)
    # cookie读取
    title = request.COOKIES['title']
    response.write(title)
    return response


def session_test(request):
    '''
    在服务器端记录敏感信息，使用session
    '''
    # request.session['name'] = 'world'
    hello = request.session.get('name')
    # 设置过期时间
    request.session.set_expiry(0)

    return HttpResponse(hello)
