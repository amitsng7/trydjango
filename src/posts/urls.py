from django.conf.urls import include, url
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^create$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_index, name="index"),
    url(r'^index/$', views.post_index, name="list"),
    url(r'^(?P<id>\d+)/delete$', views.post_delete),
    url(r'^(?P<id>\d+)/edit$', views.post_update, name="update"),
]