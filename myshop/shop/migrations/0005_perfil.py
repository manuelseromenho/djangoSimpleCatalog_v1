# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_remove_produto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='utilizadores/%Y/%m/%d')),
                ('utilizador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
