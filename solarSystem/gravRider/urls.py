from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.form, name='form'),
    url(r'^visual/', views.visualization, name='visualization')
]