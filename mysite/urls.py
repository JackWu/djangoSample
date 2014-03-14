from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from quickapi import views

from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determing the URL conf
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
        
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
