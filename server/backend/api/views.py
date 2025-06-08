from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def api_home(request):
    return HttpResponse({
        "message":"Welcome to the text prediction API",
        "status":"success",
    })