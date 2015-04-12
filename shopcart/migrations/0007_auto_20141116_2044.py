# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0006_auto_20141116_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='bow_id1',
            new_name='data',
        ),
    ]
