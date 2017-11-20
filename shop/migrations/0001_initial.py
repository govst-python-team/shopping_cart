# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
