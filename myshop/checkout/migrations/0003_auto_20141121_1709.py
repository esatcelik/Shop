# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_check_tprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check',
            old_name='data',
            new_name='accessory_data',
        ),
        migrations.AddField(
            model_name='check',
            name='arrow_data',
            field=models.CharField(default=1, max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check',
            name='bow_data',
            field=models.CharField(default=1, max_length=500, blank=True),
            preserve_default=False,
        ),
    ]
