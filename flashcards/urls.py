"""mobica URL Configuration

"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^$', views.index),
    #url(r'^login$', views.login),

    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout_view),

    #url(r'^login$', 'django.contrib.auth.views.login'),
]
