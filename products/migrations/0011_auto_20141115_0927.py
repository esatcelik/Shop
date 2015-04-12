# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20141114_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='bows',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bows',
            name='image',
            field=models.ImageField(upload_to=b'images'),
        ),
    ]
