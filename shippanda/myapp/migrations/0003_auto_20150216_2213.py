# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_panelist_c'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flat_no', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('tracking_no', models.AutoField(serialize=False, primary_key=True)),
                ('mapped_tracking_no', models.CharField(max_length=10)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('tracking_data', models.CharField(max_length=10)),
                ('status', models.CharField(blank=True, max_length=1, null=True, choices=[(b'P', b'pending'), (b'C', b'complete')])),
                ('cost', models.CharField(max_length=10, null=True, blank=True)),
                ('paid', models.CharField(blank=True, max_length=1, null=True, choices=[(b'Y', b'yes'), (b'N', b'no')])),
                ('cancelled', models.CharField(default=b'N', max_length=1, choices=[(b'Y', b'yes'), (b'N', b'no')])),
                ('pickup_address', models.ForeignKey(to='myapp.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('image', models.ImageField(upload_to=b'static/shipment/images')),
                ('category', models.CharField(blank=True, max_length=1, null=True, choices=[(b'P', b'premium'), (b'R', b'regular')])),
                ('drop_name', models.CharField(max_length=10)),
                ('drop_phone', models.CharField(max_length=12, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^d{10,12}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('drop_address', models.ForeignKey(to='myapp.Address')),
                ('order', models.ForeignKey(to='myapp.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('otp', models.IntegerField(null=True, blank=True)),
                ('apikey', models.CharField(max_length=100, null=True, blank=True)),
                ('referral_code', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Panelist',
        ),
    ]
