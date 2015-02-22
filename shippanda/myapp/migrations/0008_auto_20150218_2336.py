# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20150218_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='image',
            field=models.ImageField(default=1, upload_to=b'/images'),
            preserve_default=False,
        ),
    ]
