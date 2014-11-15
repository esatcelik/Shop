# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20141115_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='brand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessories',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessories',
            name='image',
            field=models.ImageField(default=1, upload_to=b'images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessories',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessories',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessories',
            name='type',
            field=models.CharField(default=1, max_length=1, choices=[(b'Bow', b'Bow'), (b'Arrow', b'Arrow'), (b'General', b'General')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrows',
            name='brand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrows',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrows',
            name='image',
            field=models.ImageField(default=11, upload_to=b'images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrows',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrows',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrows',
            name='type',
            field=models.CharField(default=1, max_length=1, choices=[(b'Aluminium', b'Aluminium'), (b'Carbon', b'Carbon'), (b'Wood', b'Wood')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bows',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'Compounds', b'Compounds'), (b'Recurves', b'Recurves'), (b'Traditional', b'Traditional')]),
        ),
    ]
