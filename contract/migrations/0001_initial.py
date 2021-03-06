# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 20:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=80)),
                ('project_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='project_publish_date')),
                ('project_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=12)),
                ('project_description', models.TextField()),
                ('project_publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('project_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_publish_date', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-project_publish_date',),
            },
        ),
    ]
