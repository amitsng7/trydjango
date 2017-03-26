from django.conf.urls import include, url
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^create$', views.post_create),
    url(r'^index$', views.post_index),
    url(r'^delete$', views.post_delete),
    url(r'^update$', views.post_update),
]