# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Botiga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_botiga', models.IntegerField()),
                ('nom_botiga', models.TextField(null=True, blank=True)),
                ('tipus_botiga', models.TextField(null=True, blank=True)),
                ('adressa', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ciutat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_ciutat', models.TextField()),
                ('moneda', models.TextField(default=b'euro')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codi_marca', models.IntegerField()),
                ('nom_marca', models.TextField(null=True, blank=True)),
                ('descripcio', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('botiga', models.ForeignKey(related_name='botigues', to='icommerce.Botiga', null=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pesa_roba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codi_pesa', models.IntegerField()),
                ('tipus', models.PositiveSmallIntegerField(verbose_name=b'CATEGORIES', choices=[(1, b'Pantalo'), (2, b'Jersei'), (3, b'Blusa'), (4, b'Camiseta'), (5, b'Jaqueta'), (6, b'Roba_interior'), (7, b'Short'), (8, b'Faldilla'), (9, b'Sabates'), (10, b'Complements'), (11, b'Vestit')])),
                ('nom', models.TextField()),
                ('colors', models.PositiveSmallIntegerField(default=1, verbose_name=b'COLORS', choices=[(1, b'Blanc'), (2, b'Negre'), (3, b'Gris'), (4, b'Marro'), (5, b'Blau'), (6, b'Verd'), (7, b'Groc'), (8, b'Roig'), (9, b'Rosa'), (10, b'Lila'), (11, b'Taronja')])),
                ('talla', models.PositiveSmallIntegerField(default=1, verbose_name=b'TALLA', choices=[(1, b'XS'), (2, b'S'), (3, b'M'), (4, b'L'), (5, b'XL'), (6, b'XXL')])),
                ('preu', models.DecimalField(null=True, verbose_name=b'Preu', max_digits=8, decimal_places=2, blank=True)),
                ('descripcio', models.TextField(null=True, blank=True)),
                ('imatge', models.ImageField(null=True, upload_to=b'icommerce', blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
