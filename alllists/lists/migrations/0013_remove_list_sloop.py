# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-13 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0012_list_sloop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='sloop',
        ),
    ]
