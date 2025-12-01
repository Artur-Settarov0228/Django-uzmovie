from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'genre', 'rating', 'poster', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control search-box',
                'placeholder': 'Kino nomini kiriting'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control search-box',
                'placeholder': 'Kino haqida tavsif',
                'rows': 4
            }),
            'release_date': forms.DateInput(attrs={
                'class': 'form-control search-box',
                'type': 'date'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select search-box'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control search-box',
                'min': 1,
                'max': 10,
                'step': 0.1
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control search-box',
                'placeholder': 'https://example.com/video'
            }),
        }