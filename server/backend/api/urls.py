from django.urls import path,include
from django.http import HttpResponse
from api.views import  PredictTextAPIView

urlpatterns = [
    path('', lambda request: HttpResponse("<h1>Testing Home API</h1> ")),
    path('predict/', PredictTextAPIView.as_view(), name='predict'),
]