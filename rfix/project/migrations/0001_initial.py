# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-26 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tasks', models.ManyToManyField(blank=True, related_name='tasks', to='task.Task')),
            ],
        ),
    ]
