# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_produto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
    ]
