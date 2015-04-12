# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_check_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='used',
        ),
    ]
