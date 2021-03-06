# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import norma.formulario.binary


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completado', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.IntegerField(choices=[(0, b'Binario'), (1, b'Decimal'), (2, b'Entero'), (3, b'Cadena'), (4, b'Parrafo'), (5, b'Fecha'), (6, b'Hora'), (7, b'Fecha/Hora')])),
                ('nombre', models.CharField(max_length=45)),
                ('regular', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', norma.formulario.binary.ByteAField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.Tipo')),
            ],
        ),
    ]
