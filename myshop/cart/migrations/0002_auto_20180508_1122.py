# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='produto',
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('produto', 'carrinho')]),
        ),
    ]
