from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trails/', include('trails.urls')), 
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('search/', views.search, name='search'),
]