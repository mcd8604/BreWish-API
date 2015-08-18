# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brewish_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBeer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beer', models.ForeignKey(related_name='user_beers', to='brewish_api.Beer')),
                ('user', models.ForeignKey(related_name='user_beers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
