# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0002_pesa_roba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesa_roba',
            name='talla',
        ),
    ]
