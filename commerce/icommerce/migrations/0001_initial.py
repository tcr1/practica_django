# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Botiga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_botiga', models.IntegerField()),
                ('nom_botiga', models.TextField(null=True, blank=True)),
                ('tipus_botiga', models.TextField(null=True, blank=True)),
                ('adress', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciutat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_ciutat', models.TextField()),
                ('moneda', models.TextField(default='euro')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codi_marca', models.IntegerField()),
                ('nom_marca', models.TextField(null=True, blank=True)),
                ('descripcio', models.TextField(null=True, blank=True)),
                ('botiga', models.ForeignKey(related_name='botigues', to='icommerce.Botiga', null=True)),
            ],
        ),
    ]
