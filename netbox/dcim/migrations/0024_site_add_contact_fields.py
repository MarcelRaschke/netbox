# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0023_devicetype_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name=b'Contact E-mail'),
        ),
        migrations.AddField(
            model_name='site',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='site',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]