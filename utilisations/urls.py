"""mobica URL Configuration

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^groups$', views.all_groups),
    url(r'^group/(?P<group_id>\d+)/$', views.group),
]
