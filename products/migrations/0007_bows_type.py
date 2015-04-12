# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_bows_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bows',
            name='type',
            field=models.CharField(default='C', max_length=1, choices=[(b'C', b'Compounds'), (b'R', b'Recurves'), (b'T', b'Traditional')]),
            preserve_default=False,
        ),
    ]
