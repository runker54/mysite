from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Binance(models.Model):
    coin_pairs = models.CharField(max_length=255, blank=True, null=True)
    coin_pairs_temp = models.CharField(max_length=255, blank=True, null=True)
    coin_price = models.FloatField(blank=True, null=True)
    change_1m = models.FloatField(blank=True, null=True)
    change_5m = models.FloatField(blank=True, null=True)
    change_15m = models.FloatField(blank=True, null=True)
    change_30m = models.FloatField(blank=True, null=True)

    def __str__(self):
        # 显示coin_pairs
        return self.coin_pairs


class OKX(models.Model):
    coin_pairs = models.CharField(max_length=255, blank=True, null=True)
    coin_pairs_temp = models.CharField(max_length=255, blank=True, null=True)
    coin_price = models.FloatField(blank=True, null=True)
    change_1m = models.FloatField(blank=True, null=True)
    change_5m = models.FloatField(blank=True, null=True)
    change_15m = models.FloatField(blank=True, null=True)
    change_30m = models.FloatField(blank=True, null=True)

    def __str__(self):
        # 显示coin_pairs
        return self.coin_pairs


class Huobi(models.Model):
    coin_pairs = models.CharField(max_length=255, blank=True, null=True)
    coin_pairs_temp = models.CharField(max_length=255, blank=True, null=True)
    coin_price = models.FloatField(blank=True, null=True)
    change_1m = models.FloatField(blank=True, null=True)
    change_5m = models.FloatField(blank=True, null=True)
    change_15m = models.FloatField(blank=True, null=True)
    change_30m = models.FloatField(blank=True, null=True)

    def __str__(self):
        # 显示coin_pairs
        return self.coin_pairs


class Chain(models.Model):
    coin_pairs = models.CharField(max_length=255, blank=True, null=True)
    coin_pairs_temp = models.CharField(max_length=255, blank=True, null=True)
    coin_price = models.FloatField(blank=True, null=True)
    change_1m = models.FloatField(blank=True, null=True)
    change_5m = models.FloatField(blank=True, null=True)
    change_15m = models.FloatField(blank=True, null=True)
    change_30m = models.FloatField(blank=True, null=True)

    def __str__(self):
        # 显示coin_pairs
        return self.coin_pairs


class Analysis(models.Model):
    coin_pairs = models.CharField(max_length=255, blank=True, null=True)
    binance = models.FloatField(blank=True, null=True)
    okx = models.FloatField(blank=True, null=True)
    huobi = models.FloatField(blank=True, null=True)
    chain = models.FloatField(blank=True, null=True)
    pricediff = models.FloatField(blank=True, null=True)

    def __str__(self):
        # 显示coin_pairs
        return self.coin_pairs


# 交易所公告信息
class Spider(models.Model):
    # 消息来源
    source = models.CharField(max_length=255)
    # url链接
    link = models.TextField()
    # 正文
    content = models.TextField()
    # 写入时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # 文本主要内容
        return self.content
