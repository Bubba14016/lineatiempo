# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0003_auto_20170221_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='archivo',
            field=models.FileField(upload_to='static/archivos/'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='image',
            field=models.ImageField(upload_to='static/imagenes/'),
        ),
    ]
