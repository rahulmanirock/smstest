from django.conf.urls import url
from chemical_composition.api import views

urlpatterns = [
    url(r'^$', views.chemical_composition_list, name='chemical-composition-list'),
]