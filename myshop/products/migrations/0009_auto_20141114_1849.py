# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20141114_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='bows',
            name='price',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bows',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
