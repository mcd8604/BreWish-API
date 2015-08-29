from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Beer(models.Model):
	name = models.CharField(max_length=100, blank=False, default='')
	label = models.CharField(max_length=100, blank=True, default='')
	style = models.CharField(max_length=100, blank=True, default='')
	desc = models.TextField()
	abv = models.DecimalField(max_digits=3, decimal_places=1)
	ibu = models.PositiveSmallIntegerField()
	slug = models.SlugField(blank=True)
	isInProd = models.NullBooleanField()
	created = models.DateTimeField(auto_now_add=True)
	authRating = models.PositiveSmallIntegerField(null=True, blank=True)
	
	class Meta:
		ordering = ('name',)

class UserBeer(models.Model):
	user = models.ForeignKey('auth.User', related_name='user_beers')
	beer = models.ForeignKey(Beer, related_name='user_beers')
	isOwned = models.BooleanField(default=False)
	isWished = models.BooleanField(default=True)

class Event(models.Model):
	name = models.CharField(max_length=100, blank=False, default='')
	details = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	createdBy = models.ForeignKey('auth.User', related_name='events')
	date = models.DateField(default=timezone.now)
	time = models.TimeField(null=True, blank=True)
	location = models.CharField(max_length=100, blank=False, default='')
	isCorporate = models.BooleanField(default=False)
	guestCanInvite = models.BooleanField()
	guestCanAddBeer = models.BooleanField()		

class EventBeer(models.Model):
	event = models.ForeignKey(Event, related_name='event_beers')
	beer = models.ForeignKey(Beer, related_name='event_beers')
	#user = models.ForeignKey('auth.User', related_name='event_beers')

class EventUser(models.Model):
	event = models.ForeignKey(Event, related_name='event_users')
	user = models.ForeignKey('auth.User', related_name='event_users')
	isAttending = models.BooleanField()
