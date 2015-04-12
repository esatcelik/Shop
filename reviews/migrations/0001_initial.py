# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_id', models.IntegerField()),
                ('review', models.TextField()),
                ('user1_id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mod', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
