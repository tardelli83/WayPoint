from django.contrib import admin
from django.urls import path
from waypoint import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('report/', views.report_view, name='report'),
    path('search/', views.search_view, name='search'),
]