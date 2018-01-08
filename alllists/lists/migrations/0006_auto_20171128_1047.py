# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-28 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='children',
            field=models.ManyToManyField(blank=True, to='lists.List'),
        ),
        migrations.AlterField(
            model_name='list',
            name='item_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
