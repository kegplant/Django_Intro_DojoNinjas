# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-15 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0003_auto_20171115_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
