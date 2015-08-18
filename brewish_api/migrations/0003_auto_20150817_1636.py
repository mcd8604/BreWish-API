# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewish_api', '0002_userbeer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='authRating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
