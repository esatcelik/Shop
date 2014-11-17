# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0003_auto_20141115_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user_id',
            new_name='user_id1',
        ),
    ]
