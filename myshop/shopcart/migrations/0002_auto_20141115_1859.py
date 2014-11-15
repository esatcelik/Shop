# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SomeObject',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='data',
        ),
        migrations.AddField(
            model_name='cart',
            name='accessory_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='arrow_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='bow_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
