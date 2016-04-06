# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0005_auto_20160403_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesa_roba',
            name='colors',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='COLORS', choices=[(1, 'Blanc'), (2, 'Negre'), (3, 'Gris'), (4, 'Marro'), (5, 'Blau'), (6, 'Verd'), (7, 'Groc'), (8, 'Roig'), (9, 'Rosa'), (10, 'Lila')]),
        ),
    ]
