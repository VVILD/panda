# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150216_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b"Phone number must be entered in the format: '999999999'. Up to 12 digits allowed.")]),
            preserve_default=True,
        ),
    ]
