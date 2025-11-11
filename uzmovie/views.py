from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def add_movie(request: HttpRequest) -> HttpResponse:
    return render(request, 'add_movie.html')
