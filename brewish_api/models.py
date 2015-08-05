from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Beer(models.Model):
	name = models.CharField(max_length=100, blank=False, default='')
	label = models.CharField(max_length=100, blank=True, default='')
	style = models.CharField(max_length=100, blank=True, default='')
	desc = models.TextField()
	abv = models.DecimalField(max_digits=3, decimal_places=1)
	ibu = models.PositiveSmallIntegerField()
	slug = models.SlugField()
	isInProd = models.NullBooleanField()
	created = models.DateTimeField(auto_now_add=True)
	authRating = model.PositiveSmallIntegerField()
	
	class Meta:
		ordering = ('name',)

class User(models.Model):

class Event(models.Model):
	name = models.CharField(max_length=100, blank=False, default='')
	details = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	createdBy = models.ForeignKey(User, related_name='events')
	datetime = models.DateTimeField(auto_now_add=False)
	location = models.CharField(max_length=100, blank=False, default='')
	isCorporate = models.BooleanField()
	guestCanInvite = models.BooleanField()
	guestCanAddBeer = models.BooleanField()		
	
class EventBeer(models.Model):
	event = models.ForeignKey(Event, related_name='event_beers')
	beer = models.ForeignKey(Beer, related_name='event_beers')
	user = models.ForeignKey(User, related_name='event_beers'))
	
class EventUser(models.Model):
	event = models.ForeignKey(Event, related_name='event_users')
	user = models.ForeignKey(User, related_name='event_users')
	isAttending = models.BooleanField()
	
