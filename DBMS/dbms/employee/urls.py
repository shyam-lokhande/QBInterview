from django.contrib import admin
from django.urls import include, path
from .views import *

app_name="employee"

urlpatterns = [
    path('upload/',uploadFile,name='uploadFile'),
]