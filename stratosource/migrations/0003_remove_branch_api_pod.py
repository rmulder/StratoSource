# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stratosource', '0002_auto_20160902_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='api_pod',
        ),
    ]
