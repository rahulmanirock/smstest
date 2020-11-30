from django.conf.urls import url
from commodity.api import views

urlpatterns = [
    url(r'^$', views.commodity_list, name='commodity-list'),
]