# Generated by Django 3.2.12 on 2022-02-05 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0025_auto_20210818_1613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File_order',
            new_name='FileOrder',
        ),
        migrations.RenameModel(
            old_name='Menu_text',
            new_name='MenuText',
        ),
        migrations.RenameModel(
            old_name='Message_text',
            new_name='MessageText',
        ),
    ]
