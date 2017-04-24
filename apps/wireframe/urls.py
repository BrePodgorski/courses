from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^show$',views.show),
    url(r'^confirm/(?P<id>\d+)$',views.confirm),
    url(r'^clear/(?P<id>\d+)$',views.clear)
]
