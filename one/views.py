from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from one.models import Binance,Spider
import json


# redirect 重定向
# Create your views here.
# 第一个页面
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        response = request.POST
        user = response["user"]
        password = response["password"]
        if user == 'crypto' and password == 'root':
            return redirect("http://www.runker54.top/search")
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误!"})


def data_search(request):
    if request.method == 'GET':
        return render(request, "datasearch.html")


@csrf_exempt
def data_post(request):
    if request.method == 'POST':
        parms = request.POST
        coin_name = str(parms.get('coin')).upper()
        change1m = parms.get('_1m')
        change5m = parms.get('_5m')
        change15m = parms.get('_15m')
        change30m = parms.get('_30m')
        data_dict = {}
        # 默认排序方法
        sortx = 'change_1m'
        if parms:
            data_dict["coin_pairs__contains"] = coin_name
        if change1m:
            data_dict["change_1m__gte"] = float(change1m)
            sortx = 'change_1m'
        if change5m:
            data_dict["change_5m__gte"] = float(change5m)
            sortx = 'change_5m'
        if change15m:
            data_dict["change_15m__gte"] = float(change15m)
            sortx = 'change_15m'
        if change30m:
            data_dict["change_30m__gte"] = float(change30m)
            sortx = 'change_30m'
        data_list = list(Binance.objects.all().order_by(f'-{sortx}').values().filter(**data_dict))
        ret = {"data": data_list}
        return JsonResponse(ret)


@csrf_exempt
def navigation(request):
    return render(request, 'navigation.html')


@csrf_exempt
def spider_page(request):
    if request.method == 'GET':
        return render(request, 'spiderpage.html')
    if request.method == 'POST':
        # Binance Noce  top 10
        binace_noce = list(Spider.objects.all().order_by('created').values().filter(source='Binance'))[-20:]
        # OKX Noce top 10
        okx_noce = list(Spider.objects.all().order_by('created').values().filter(source='OKX'))[-20:]
        ret = {'Binance':binace_noce,'OKX':okx_noce}
        return JsonResponse(ret)
