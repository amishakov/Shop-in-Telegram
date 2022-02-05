# Generated by Django 3.2.6 on 2021-08-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name="Подробное описание (разделение на отдельные сообщения ';')"),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]