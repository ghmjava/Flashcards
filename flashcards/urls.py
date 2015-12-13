"""mobica URL Configuration

"""
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url('^$', views.index),

    url('^', include('django.contrib.auth.urls')),
    url(r'^logout$', views.logout_view),
    url(r'^test$', views.test),
]
