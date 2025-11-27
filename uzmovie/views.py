from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Movie
from .forms import MovieForm

def home(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'movies': movies})

def add_movie(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    
    return render(request, 'add_movie.html', {'form': form})