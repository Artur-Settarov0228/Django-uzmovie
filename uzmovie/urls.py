from django.urls import path
from . views import home, add_movie

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_movie, name='add_movie'),

]

