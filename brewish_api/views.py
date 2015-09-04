from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
	
#class WishViewSet(viewsets.ModelViewSet):
#	queryset = UserBeer.objects.filter(isWished__exact=True)
#	serializer_class = UserBeerSerializer
#	#TODO readonly permission for friends
#	def perform_create(self, serializer):
#		#TODO only auth user can create
#		serializer.save(user=self.request.user, isWished=True)

#class OwnedViewSet(viewsets.ModelViewSet):
#	queryset = UserBeer.objects.filter(isOwned__exact=True)
#	serializer_class = UserBeerSerializer
#	#TODO readonly permission for friends
#	def perform_create(self, serializer):
#		#TODO only auth user can create
#		serializer.save(user=self.request.user, isOwned=True)
	
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

class EventBeerViewSet(viewsets.ModelViewSet):
	queryset = EventBeer.objects.all()
	serializer_class = EventBeerSerializer
	
class EventUserViewSet(viewsets.ModelViewSet):
	queryset = EventUser.objects.all()
	serializer_class = EventUserSerializer
		
#@api_view(['GET', 'POST'])
#def event_beer(request):
#	if request.method == 'GET':
#		e = Event.objects.all()	
#		return Response(EventSerializer(e).data, status=status.HTTP_201_CREATED)
#		
#	elif request.method == 'POST':
#		e = Event.objects.get(id=request.data.eventId)		
#		e.eventBeers.add(request.data.beerId)
#		e.update()
#		return Response(EventSerializer(e).data, status=status.HTTP_201_CREATED)
#	return Response('Unsupported Method: ' + request.method, status=status.HTTP_400_BAD_REQUEST)
	

#class EventDetail(generics.RetrieveUpdateDestroyAPIView):
#	queryset = Event.objects.all()
#	serializer_class = EventSerializer