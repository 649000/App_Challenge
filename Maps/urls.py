from django.conf.urls import url
from . import views

urlpatterns = [
    # /maps/
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.locationToCoordinates, name='geocode'),
    #   url(r'^(?P<location>.*)/$', views.locationToCoordinates, name='geocode'),
     url(r'^emails/$', views.testMails, name='ea'),
]