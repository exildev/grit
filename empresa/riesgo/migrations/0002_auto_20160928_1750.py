# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riesgo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='consecuencia',
            field=models.IntegerField(blank=True, choices=[(1, b'Insignificacnte'), (2, b'Menor'), (3, b'Moderada'), (4, b'Mayor'), (5, b'Catastr\xc3\xb3fica')], null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='controles_administrativos',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='controles_instalacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='controles_operacionales',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='controles_talentoHumano',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgo.EvaluacionEmpresa'),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='fuente',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='medio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='metodo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='persona',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='probabilidad',
            field=models.IntegerField(blank=True, choices=[(1, b'Raro'), (2, b'Improbable'), (3, b'Posible'), (4, b'Probable'), (5, b'Casi seguro')], null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionriesgos',
            name='riesgo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgo.Riesgo'),
        ),
    ]
