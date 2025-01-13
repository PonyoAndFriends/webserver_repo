from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('testing', views.redshift_testing)
]