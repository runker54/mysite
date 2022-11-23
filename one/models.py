from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Binance(models.Model):
    id_number = models.AutoField(primary_key=True)
    coin_pairs = models.CharField(max_length=255, blank=True, null=True)
    coin_pairs_temp = models.CharField(max_length=255, blank=True, null=True)
    coin_price = models.FloatField(blank=True, null=True)
    change_1m = models.FloatField(blank=True, null=True)
    change_5m = models.FloatField(blank=True, null=True)
    change_15m = models.FloatField(blank=True, null=True)
    change_30m = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'binance'
    def __str__(self):
         # 显示coin_pairs
        return self.coin_pairs


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
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

        class Meta:
           # 按时间倒序排列
            db_table = 'spider'
            ordering = ('-created',)

        def __str__(self):
            # 文本主要内容
            return self.content
