# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-21 06:56
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20170813_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ematt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('shift', models.CharField(choices=[('Night', 'Night'), ('Day', 'Day')], default='Day', max_length=6)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent', max_length=8)),
                ('reason', models.TextField(blank=True, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emsalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(blank=True, null=True)),
                ('month', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied'), ('', '')], default='', max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='joindate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number in the format: '+999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{9,11}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='resigndate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
