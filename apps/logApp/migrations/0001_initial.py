# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-16 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pw', models.CharField(max_length=255)),
                ('pwSalt', models.CharField(max_length=255)),
            ],
        ),
    ]
