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

class OwnedBeer(models.Model):
	user = models.ForeignKey('auth.User')
	beer = models.ForeignKey(Beer)
	
class WishedBeer(models.Model):
	user = models.ForeignKey('auth.User')
	beer = models.ForeignKey(Beer)

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
	#eventUsers = models.ManyToManyField(User, through='EventUser', through_fields=('event', 'user'))
	#eventBeers = models.ManyToManyField(Beer, through='EventBeer')

class EventBeer(models.Model):
	event = models.ForeignKey(Event, related_name='eventBeers')
	user = models.ForeignKey('auth.User', related_name='+')
	beer = models.ForeignKey(Beer)

class EventUser(models.Model):
	event = models.ForeignKey(Event, related_name='eventUsers')
	user = models.ForeignKey(User, null=False)
	#inviter = models.ForeignKey(User, related_name="event_invites")
	isAttending = models.BooleanField(default=False)
