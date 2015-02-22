# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='drop_phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
    ]
