# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0016_auto_20170209_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='physical_place',
            field=models.CharField(choices=[('ARCHIVE', 'Архив'), ('LIBRARY', 'Библиотека')], default='ARCHIVE', max_length=100, verbose_name='Место физического размещения'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='Номер документа в физическом хранилище'),
        ),
    ]
