# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-10 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0036_auto_20170424_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='display_on_home',
            field=models.BooleanField(default=True, verbose_name='Показывать на главной?'),
        ),
        migrations.AlterField(
            model_name='document',
            name='physical_place',
            field=models.CharField(choices=[('archive', 'Архив'), ('library', 'Библиотека')], default='ARCHIVE', max_length=100, verbose_name='Место размещения'),
        ),
    ]
