# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0007_auto_20160403_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesa_roba',
            name='imatge',
            field=models.ImageField(null=True, upload_to='icommerce', blank=True),
        ),
    ]
