# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('tag', models.CharField(max_length=32)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]