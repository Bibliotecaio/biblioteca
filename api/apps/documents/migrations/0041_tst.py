# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-21 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0040_auto_20180317_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.PositiveIntegerField(default=0)),
                ('b', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
