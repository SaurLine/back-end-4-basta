from django.contrib import admin
from django.urls import path
from . import views

app_name = "inicio"

urlpatterns = [
    path('', views.default, name = 'index'),
]
