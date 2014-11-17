# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0005_auto_20141115_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='accessory_id1',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='arrow_id1',
        ),
        migrations.AlterField(
            model_name='cart',
            name='bow_id1',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
