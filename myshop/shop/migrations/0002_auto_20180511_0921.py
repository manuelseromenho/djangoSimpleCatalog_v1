# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPagamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('metodo_pagamento', models.TextField(max_length=20, blank=True)),
                ('taxa_metodo', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='endereco_envio',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='endereco_faturacao',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='nif',
            field=models.TextField(max_length=11, blank=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='metodo_pagamento',
            field=models.ForeignKey(default=1, to='shop.MetodoPagamento'),
        ),
    ]
