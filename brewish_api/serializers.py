from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from brewish_api.models import Beer, Event, EventBeer, EventUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer
		
class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		
class EventBeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = EventBeer
		
class EventUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = EventUser