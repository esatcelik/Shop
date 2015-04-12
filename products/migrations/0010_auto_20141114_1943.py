# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20141114_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bows',
            name='image',
            field=models.ImageField(upload_to=b'media/images/'),
        ),
        migrations.AlterField(
            model_name='bows',
            name='price',
            field=models.IntegerField(),
        ),
    ]
