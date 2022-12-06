import time
import pymysql
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from one.models import Binance, Spider, OKX, Huobi, Chain, Analysis
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
            return redirect("https://www.runker54.top/search")
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
def analysis_data(request):
    # 获取每个cex的coin_pairs，获得交集coin_pairs
    binance_pairs = set(Binance.objects.values_list('coin_pairs'))
    okx_pairs = set(OKX.objects.values_list('coin_pairs_temp'))
    huobi_pairs = set(Huobi.objects.values_list('coin_pairs_temp'))
    array = [_[0] for _ in list(binance_pairs & huobi_pairs & okx_pairs)]
    if request.method == 'GET':
        return render(request, 'analysis.html', {"array": array})
    if request.method == 'POST':
        # 获取Chain的coin_pairs信息
        chain_data = {_x: _y if _y else 0.00001 for _x, _y in list(Chain.objects.filter(coin_pairs__in=array).values_list('coin_pairs', 'coin_price'))}
        # 获取各个cex的交集coin_pairs信息
        binance_data = {_x: _y if _y else 0.00001 for _x, _y in list(Binance.objects.filter(coin_pairs__in=array).values_list('coin_pairs', 'coin_price'))}
        okx_data = {_x: _y if _y else 0.00001 for _x, _y in list(OKX.objects.filter(coin_pairs_temp__in=array).values_list('coin_pairs_temp', 'coin_price'))}
        huobi_data = {_x: _y if _y else 0.00001 for _x, _y in list(Huobi.objects.filter(coin_pairs_temp__in=array).values_list('coin_pairs_temp', 'coin_price'))}
        # 构建规范的字典数据
        result = {_: {"Binance": binance_data[_], "OKX": okx_data[_], "Huobi": huobi_data[_], "Chain": chain_data[_],
                      "price_diff": max([binance_data[_], okx_data[_], huobi_data[_], chain_data[_]]) - min([binance_data[_], okx_data[_], huobi_data[_], chain_data[_]]),
                      "per": (abs(binance_data[_] - chain_data[_]) / binance_data[_]) * 100} for _ in array}
        result = dict(sorted(result.items(), key=lambda item: (item[1]['per'], item[1]['price_diff']), reverse=False))
        # 将数据写入analysis
        for one_el in result:
            Analysis.objects.filter(coin_pairs=one_el).update(binance=result[one_el]['Binance'],
                                                              okx=result[one_el]['OKX'], huobi=result[one_el]['Huobi'],
                                                              chain=result[one_el]['Chain'],
                                                              pricediff=result[one_el]['price_diff'])
        ret = {'coin_list': array, 'data': result}
        return JsonResponse(ret)


@csrf_exempt
def spider_page(request):
    if request.method == 'GET':
        return render(request, 'spiderpage.html')
    if request.method == 'POST':
        # Binance Noce  top 10
        binace_noce = list(Spider.objects.all().order_by('created').values().filter(source='Binance'))[-20:]
        # OKX Noce top 10
        okx_noce = list(Spider.objects.all().order_by('created').values().filter(source='OKX'))[-20:]
        ret = {'Binance': binace_noce, 'OKX': okx_noce}
        return JsonResponse(ret)


@csrf_exempt
def navigation(request):
    return render(request, 'navigation.html')
