# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesa_roba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipus', models.PositiveSmallIntegerField(default=1, verbose_name='Rating (stars)', choices=[(1, 'pantalo'), (2, 'jersei'), (3, 'blusa'), (4, 'camiseta'), (5, 'jaqueta'), (6, 'Roba_interior'), (7, 'short')])),
                ('colors', models.PositiveSmallIntegerField(default=1, verbose_name='Rating (stars)', choices=[(1, 'WHITE'), (2, 'PINK'), (3, 'BLACK'), (4, 'BLUE'), (5, 'BROWN')])),
                ('codi_pesa', models.IntegerField()),
                ('nom', models.TextField()),
                ('preu', models.DecimalField(null=True, verbose_name='Euro amount', max_digits=8, decimal_places=2, blank=True)),
                ('descripcio', models.TextField(null=True, blank=True)),
                ('talla', models.IntegerField()),
                ('imatge', models.ImageField(null=True, upload_to='commerce', blank=True)),
            ],
        ),
    ]
