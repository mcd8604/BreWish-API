from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from brewish_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	ownedBeers = serializers.HyperlinkedRelatedField(many=True, view_name='userbeer-detail', read_only=True)# queryset=UserBeer.objects.all())
	wishedBeers = serializers.HyperlinkedRelatedField(many=True, view_name='userbeer-detail', read_only=True)# queryset=UserBeer.objects.all())
	createdEvents = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)# queryset=Event.objects.all())
	
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups', 'ownedBeers', 'wishedBeers', 'createdEvents')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer
		
class UserBeerSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = UserBeer
		
class EventSerializer(serializers.ModelSerializer):
	createdBy = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Event
		
class EventBeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = EventBeer
		
class EventUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = EventUser