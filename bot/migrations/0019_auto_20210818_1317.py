# Generated by Django 3.2.6 on 2021-08-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_auto_20210818_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fio',
            field=models.CharField(max_length=200, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]