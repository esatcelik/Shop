# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20141121_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id1', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('Tprice', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
