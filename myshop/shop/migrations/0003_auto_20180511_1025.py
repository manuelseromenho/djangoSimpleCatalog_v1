# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180511_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nif',
            field=models.CharField(max_length=11, blank=True),
        ),
    ]
