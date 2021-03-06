"""BreWish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from brewish_api import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'eventbeers', views.EventBeerViewSet)
router.register(r'eventusers', views.EventUserViewSet)
router.register(r'beers', views.BeerViewSet)
#router.register(r'wishlist', views.WishViewSet)
#router.register(r'ownedlist', views.OwnedViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#	url(r'^events/$', views.EventList.as_view(), name='event-list'),
#	url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),        
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
