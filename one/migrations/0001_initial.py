# Generated by Django 4.1.3 on 2022-11-24 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_pairs', models.CharField(blank=True, max_length=255, null=True)),
                ('coin_pairs_temp', models.CharField(blank=True, max_length=255, null=True)),
                ('coin_price', models.FloatField(blank=True, null=True)),
                ('change_1m', models.FloatField(blank=True, null=True)),
                ('change_5m', models.FloatField(blank=True, null=True)),
                ('change_15m', models.FloatField(blank=True, null=True)),
                ('change_30m', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
                ('link', models.TextField()),
                ('content', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
