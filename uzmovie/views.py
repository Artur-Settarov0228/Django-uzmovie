from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Movie
# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def add_movie(request: HttpRequest) -> HttpResponse:
    
    if request.method =='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        rating = request.POST.get('rating')
        poster = request.FILES.get('poster')
        video_url = request.POST.get('video_url')
# Ma'lumotlarni saqlash uchun kod yoziladi
        Movie.objects.create(
            title=title,
            description=description,
            release_date=release_date,
            genre=genre,
            rating=rating,
            poster=poster,
            video_url=video_url
        )
        return redirect('home')
    return render(request, 'add_movie.html')
    



