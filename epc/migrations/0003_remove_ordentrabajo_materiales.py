# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-20 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0002_auto_20160920_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='materiales',
        ),
    ]
