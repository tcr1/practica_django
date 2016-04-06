# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0003_remove_pesa_roba_talla'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesa_roba',
            name='talla',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='TALLA', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')]),
        ),
        migrations.AlterField(
            model_name='pesa_roba',
            name='colors',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='COLORS', choices=[(1, 'WHITE'), (2, 'PINK'), (3, 'BLACK'), (4, 'BLUE'), (5, 'BROWN')]),
        ),
        migrations.AlterField(
            model_name='pesa_roba',
            name='preu',
            field=models.DecimalField(null=True, verbose_name='Preu', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='pesa_roba',
            name='tipus',
            field=models.PositiveSmallIntegerField(verbose_name='CATEGORIES', choices=[(1, 'Pantalo'), (2, 'Jersei'), (3, 'Blusa'), (4, 'Camiseta'), (5, 'Jaqueta'), (6, 'Roba_interior'), (7, 'Short'), (8, 'Faldilla'), (9, 'Sabates'), (10, 'Complements')]),
        ),
    ]
