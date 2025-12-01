from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Movie, Advertisement
from .forms import MovieForm

def home(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.all().order_by('-created_at')[:12]
    genres = Movie.GENRE_CHOICES
    
    # Reklamalarni olish
    sidebar_ads = Advertisement.objects.filter(ad_type='sidebar', is_active=True).order_by('order')[:6]
    banner_ads = Advertisement.objects.filter(ad_type='banner', is_active=True).order_by('order')[:3]
    inline_ads = Advertisement.objects.filter(ad_type='inline', is_active=True).order_by('order')[:2]
    
    # CS 1.6 reklamasi (alohida)
    cs_ad = {
        'title': 'CS 1.6 YUKLAB OLING',
        'description': 'O\'zbek tilida, 400+ server, barcha xaritalar',
        'button_text': 'Yuklab olish',
        'icon': 'fas fa-download'
    }
    
    context = {
        'movies': movies,
        'genres': genres,
        'sidebar_ads': sidebar_ads,
        'banner_ads': banner_ads,
        'inline_ads': inline_ads,
        'cs_ad': cs_ad,
    }
    return render(request, 'home.html', context)

def add_movie(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    
    context = {
        'form': form,
    }
    return render(request, 'add_movie.html', context)