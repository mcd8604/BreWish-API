from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from brewish_api.models import *
from brewish_api.serializers import *

#class UserDetail(generics.RetrieveAPIView):
#	queryset = User.objects.all()
#	serializer_class = UserSerializer
	
class WishViewSet(viewsets.ModelViewSet):
	queryset = UserBeer.objects.filter(isWished__exact=True)
	serializer_class = UserBeerSerializer
	#TODO readonly permission for friends
	def perform_create(self, serializer):
		#TODO only auth user can create
		serializer.save(user=self.request.user, isWished=True)

class OwnedViewSet(viewsets.ModelViewSet):
	queryset = UserBeer.objects.filter(isOwned__exact=True)
	serializer_class = UserBeerSerializer
	#TODO readonly permission for friends
	def perform_create(self, serializer):
		#TODO only auth user can create
		serializer.save(user=self.request.user, isOwned=True)
	
#class UserBeerDetail(generics.RetrieveUpdateDestroyAPIView):
#	queryset = UserBeer.objects.all()
#	serializer_class = UserBeerSerializer
	
class BeerViewSet(viewsets.ModelViewSet):
	queryset = Beer.objects.all()
	serializer_class = BeerSerializer    
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer    
	permission_classes = (permissions.IsAuthenticated,)
	def perform_create(self, serializer):
		serializer.save(createdBy=self.request.user)
		
#class EventDetail(generics.RetrieveUpdateDestroyAPIView):
#	queryset = Event.objects.all()
#	serializer_class = EventSerializer