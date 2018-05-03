# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('total', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('utilizador', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('carrinho', models.ForeignKey(null=True, to='shop.Carrinho')),
                ('item', models.ForeignKey(null=True, to='shop.Produto')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('item', 'carrinho')]),
        ),
    ]
