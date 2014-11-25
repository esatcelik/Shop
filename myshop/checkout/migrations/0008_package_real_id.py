# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_check_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='real_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
