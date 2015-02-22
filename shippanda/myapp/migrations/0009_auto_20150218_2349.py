# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20150218_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='image',
        ),
        migrations.AddField(
            model_name='shipment',
            name='img',
            field=models.ImageField(default=1, upload_to=b'shipment/images'),
            preserve_default=False,
        ),
    ]
