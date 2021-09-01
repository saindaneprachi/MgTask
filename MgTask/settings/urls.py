from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('v1/workspace', workspace),

]