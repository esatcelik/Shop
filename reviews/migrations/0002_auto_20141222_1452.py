# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user1_id',
        ),
        migrations.AddField(
            model_name='reviews',
            name='username',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
