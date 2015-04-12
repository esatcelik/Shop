# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0002_auto_20141115_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='accessory_id',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='arrow_id',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='bow_id',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
