# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='panelist',
            name='C',
            field=models.ImageField(default=2, upload_to=b'static/sampleapp/media/images/event'),
            preserve_default=False,
        ),
    ]
