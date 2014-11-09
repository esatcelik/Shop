# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('features', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
