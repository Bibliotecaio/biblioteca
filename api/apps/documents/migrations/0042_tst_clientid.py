# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-21 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0041_tst'),
    ]

    operations = [
        migrations.AddField(
            model_name='tst',
            name='clientid',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]