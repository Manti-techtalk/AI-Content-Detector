from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Testing Home API</h1> ")