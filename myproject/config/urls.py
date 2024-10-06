# config/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # Import the views module from the same folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Set up index page route
]
