from django.contrib import admin

from .models import Binance, OKX, Huobi, Chain, Spider,CharinPairs

# Register your models here.
admin.site.register(Binance)
admin.site.register(OKX)
admin.site.register(Huobi)
admin.site.register(Chain)
admin.site.register(Spider)
admin.site.register(CharinPairs)
