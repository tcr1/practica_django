# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0004_auto_20160403_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesa_roba',
            name='tipus',
            field=models.PositiveSmallIntegerField(verbose_name='CATEGORIES', choices=[(1, 'Pantalo'), (2, 'Jersei'), (3, 'Blusa'), (4, 'Camiseta'), (5, 'Jaqueta'), (6, 'Roba_interior'), (7, 'Short'), (8, 'Faldilla'), (9, 'Sabates'), (10, 'Complements'), (11, 'Vestit')]),
        ),
    ]
