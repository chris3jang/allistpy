# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-15 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0013_remove_list_sloop'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List',
            new_name='Item',
        ),
    ]
