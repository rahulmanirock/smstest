from django.conf.urls import url
from django.contrib import admin
from django.db import router
from django.urls import include
from rest_framework.routers import DefaultRouter

from elements.api import views
router = DefaultRouter()

router.register(r'^$', views.elements_list, name='list'),
urlpatterns = [
    url(r'^$', views.elements_list, name='list'),
]