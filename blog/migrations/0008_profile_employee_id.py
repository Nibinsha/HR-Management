# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170925_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='employee_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
