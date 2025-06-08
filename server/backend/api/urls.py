from django.urls import path,include
from django.http import HttpResponse
from api.views import api_home, PredictTextAPIView

urlpatterns = [
    path('',api_home ),
    path('predict/', PredictTextAPIView.as_view(), name='predict'),
]