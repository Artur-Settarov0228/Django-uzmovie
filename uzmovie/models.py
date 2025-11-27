from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Drama', 'Drama'),
        ('Komediya', 'Komediya'),
        ('Fantastika', 'Fantastika'),
        ('Sarguzasht', 'Sarguzasht'),
        ('Romantika', 'Romantika'),
        ('Jangari', 'Jangari'),
        ('Tarixiy', 'Tarixiy'),
        ('Detektiv', 'Detektiv'),
        ('Qo\'rqinchli', 'Qo\'rqinchli'),
        ('Multfilm', 'Multfilm'),
        ('Biografik', 'Biografik'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Kino Nomi")
    description = models.TextField(verbose_name="Tavsif")
    release_date = models.DateField(verbose_name="Chiqgan Sana")
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name="Janr")
    rating = models.FloatField(verbose_name="Reyting")
    poster = models.ImageField(upload_to='posters/', verbose_name="Poster")
    video_url = models.URLField(blank=True, null=True, verbose_name="Video Havolasi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"