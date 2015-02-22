# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20150218_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='X',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('C', models.ImageField(upload_to=b'/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
