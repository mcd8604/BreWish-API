# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('label', models.CharField(default=b'', max_length=100, blank=True)),
                ('style', models.CharField(default=b'', max_length=100, blank=True)),
                ('desc', models.TextField()),
                ('abv', models.DecimalField(max_digits=3, decimal_places=1)),
                ('ibu', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField()),
                ('isInProd', models.NullBooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('authRating', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('details', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(default=b'', max_length=100)),
                ('isCorporate', models.BooleanField()),
                ('guestCanInvite', models.BooleanField()),
                ('guestCanAddBeer', models.BooleanField()),
                ('createdBy', models.ForeignKey(related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventBeer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beer', models.ForeignKey(related_name='event_beers', to='brewish_api.Beer')),
                ('event', models.ForeignKey(related_name='event_beers', to='brewish_api.Event')),
                ('user', models.ForeignKey(related_name='event_beers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isAttending', models.BooleanField()),
                ('event', models.ForeignKey(related_name='event_users', to='brewish_api.Event')),
                ('user', models.ForeignKey(related_name='event_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
