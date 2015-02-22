# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20150218_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='drop_address',
            field=models.ForeignKey(to='myapp.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='drop_name',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='drop_phone',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='order',
            field=models.ForeignKey(to='myapp.Order', null=True),
            preserve_default=True,
        ),
    ]
