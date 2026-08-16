from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_list, name='trail_list'),
]