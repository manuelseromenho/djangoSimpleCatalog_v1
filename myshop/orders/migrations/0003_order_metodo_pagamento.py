# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_nif'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='metodo_pagamento',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
