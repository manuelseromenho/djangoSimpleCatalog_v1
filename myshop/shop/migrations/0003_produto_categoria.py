# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=0, to='shop.Categoria'),
            preserve_default=False,
        ),
    ]
