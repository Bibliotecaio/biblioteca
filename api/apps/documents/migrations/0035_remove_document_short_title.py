# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-05 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0034_auto_20170404_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='short_title',
        ),
    ]
