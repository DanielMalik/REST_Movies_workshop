# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies_REST', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
