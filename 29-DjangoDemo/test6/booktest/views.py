from django.shortcuts import render
from django.http import HttpResponse
from models import *
import time
import task
# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')

def fwb(request):
    return render(request, 'booktest/fwb.html')


def fwbShow(request):
    goods = GoodsInfo.objects.get(pk=1)
    context = {'goods': goods}
    return render(request, 'booktest/fwbShow.html', context)


def jiansuo(request):
    return render(request, 'booktest/jiansuo.html')


def hello(request):
    task.sayhello.delay()
    return HttpResponse('ok')
