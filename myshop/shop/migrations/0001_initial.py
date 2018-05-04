# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='utilizadores/%Y/%m/%d')),
                ('utilizador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('imagem', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('descricao', models.TextField(max_length=300, blank=True)),
                ('preco', models.DecimalField(max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=200, null=True, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('categoria', models.ForeignKey(to='shop.Categoria')),
            ],
            options={
                'verbose_name': 'subcategoria',
                'verbose_name_plural': 'subcategorias',
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='subcategoria',
            field=models.ForeignKey(to='shop.SubCategoria'),
        ),
        migrations.AlterIndexTogether(
            name='produto',
            index_together=set([('id', 'slug')]),
        ),
    ]
