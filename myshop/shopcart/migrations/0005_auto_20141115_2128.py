# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0004_auto_20141115_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='accessory_id',
            new_name='accessory_id1',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='arrow_id',
            new_name='arrow_id1',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='bow_id',
            new_name='bow_id1',
        ),
    ]
