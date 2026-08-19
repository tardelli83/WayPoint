from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_list, name='trail_list'),
    path('search/', views.search_trails, name='search'),
    path('report/', views.report_view, name='report'),  
]