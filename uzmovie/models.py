from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/')
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.title
