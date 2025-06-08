from django.urls import path,include
from django.http import HttpResponse
from api.views import api_home

urlpatterns = [
    path('',api_home ),
]