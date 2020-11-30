from django.conf.urls import url
from django.contrib import admin

from elements.api import views

urlpatterns = [
    url(r'^$', views.elements_list, name='list'),
]