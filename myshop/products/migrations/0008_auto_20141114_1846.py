# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_bows_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bows',
            name='brand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bows',
            name='image',
            field=models.ImageField(default=1, upload_to=b'/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bows',
            name='quantity',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=4),
            preserve_default=False,
        ),
    ]
