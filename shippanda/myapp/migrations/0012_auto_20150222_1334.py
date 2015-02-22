# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_x'),
    ]

    operations = [
        migrations.AddField(
            model_name='x',
            name='order',
            field=models.ForeignKey(to='myapp.Order', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='img',
            field=models.ImageField(upload_to=b'shipment/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='x',
            name='C',
            field=models.ImageField(upload_to=b'shipment/'),
            preserve_default=True,
        ),
    ]
