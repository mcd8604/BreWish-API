from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from brewish_api.models import *

class UserSerializer(serializers.ModelSerializer):
	#ownedBeers = serializers.HyperlinkedRelatedField(many=True, view_name='userbeer-detail', read_only=True)# queryset=UserBeer.objects.all())
	#wishedBeers = serializers.HyperlinkedRelatedField(many=True, view_name='userbeer-detail', read_only=True)# queryset=UserBeer.objects.all())
	#createdEvents = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)# queryset=Event.objects.all())
	
	class Meta:
		model = User
		fields = ('id', 'username', 'email',)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer

#class UserBeerSerializer(serializers.ModelSerializer):
#	user = serializers.ReadOnlyField(source='owner.username')
#	beer = BeerSerializer(many=False, read_only=True)
	
#	class Meta:
#		model = UserBeer
#		fields = ('user', 'beer', 'isOwned', 'isWished') 

#NOTE: These serializers are great for GETS, but I will have to create
#specific ones for PUTS that don't override the 'fields'
#Either that, or override the create method somehow
class EventBeerSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='owner.username')
	beer = BeerSerializer(many=False, read_only=True)
	
	class Meta:
		model = EventBeer
		fields = ('user','beer',)
		
class EventUserSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)
	
	class Meta:
		model = EventUser
		fields = ('user','isAttending',)
	
#If users and beers are serialized, they are only for read operations
#When Event is being created, the eventUsers and eventBeers lists are ignored
class EventSerializer(serializers.ModelSerializer):
	createdBy = serializers.ReadOnlyField(source='owner.username')
	eventUsers = EventUserSerializer(many=True, read_only=True)
	eventBeers = EventBeerSerializer(many=True, read_only=True)
	
	class Meta:
		model = Event
		fields = (
		'id',
		'name',
		'details',
		'created',
		'createdBy',
		'date',
		'time',
		'location',
		'isCorporate',
		'guestCanInvite',
		'guestCanAddBeer',
		'eventUsers',
		'eventBeers',
		)