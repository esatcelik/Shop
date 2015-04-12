# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20141115_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'B', b'Bow'), (b'A', b'Arrow'), (b'G', b'General')]),
        ),
        migrations.AlterField(
            model_name='arrows',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'A', b'Aluminium'), (b'C', b'Carbon'), (b'W', b'Wood')]),
        ),
        migrations.AlterField(
            model_name='bows',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'C', b'Compounds'), (b'R', b'Recurves'), (b'T', b'Traditional')]),
        ),
    ]
