# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0007_auto_20161008_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='poscicion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
