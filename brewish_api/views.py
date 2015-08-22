from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from brewish_api import models
from brewish_api.serializers import *

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class UserBeerList(generics.ListAPIView):
	queryset = UserBeer.objects.all()
	serializer_class = UserBeerSerializer
	
class UserBeerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserBeer.objects.all()
	serializer_class = UserBeerSerializer
	
class BeerViewSet(viewsets.ModelViewSet):
	queryset = Beer.objects.all()
	serializer_class = BeerSerializer    
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer    
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def perform_create(self, serializer):
		serializer.save(createdBy=self.request.user)
		
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer