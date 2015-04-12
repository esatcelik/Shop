# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rec',
            old_name='rec_data',
            new_name='rec_accessory',
        ),
        migrations.AddField(
            model_name='rec',
            name='rec_arrow',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rec',
            name='rec_bow',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
