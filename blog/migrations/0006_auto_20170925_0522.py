# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170924_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ematt',
            name='name',
        ),
        migrations.RemoveField(
            model_name='emsalary',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]