# solarSim

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display/(\d+)$', views.display, name='display')
]