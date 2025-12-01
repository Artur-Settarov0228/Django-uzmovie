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
    poster = models.ImageField(upload_to='posters/', verbose_name="Poster", 
                               blank=True, null=True)  # blank va null qo'shing
    video_url = models.URLField(blank=True, null=True, verbose_name="Video Havolasi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # POSTER URL UCHUN METHOD
    def get_poster_url(self):
        if self.poster and hasattr(self.poster, 'url'):
            return self.poster.url
        else:
            # Default poster rasmi
            return 'https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"

class Advertisement(models.Model):
    AD_TYPES = [
        ('sidebar', 'Yon panel'),
        ('banner', 'Banner'),
        ('inline', 'Matn ichida'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Reklama sarlavhasi")
    description = models.TextField(verbose_name="Reklama matni")
    button_text = models.CharField(max_length=50, verbose_name="Tugma matni", default="Kirish")
    button_url = models.URLField(verbose_name="Tugma havolasi")
    ad_type = models.CharField(max_length=20, choices=AD_TYPES, default='sidebar', verbose_name="Reklama turi")
    icon = models.CharField(max_length=50, verbose_name="Ikonka", 
                           default="fas fa-ad", 
                           help_text="FontAwesome ikonka nomi")
    background_color = models.CharField(max_length=20, verbose_name="Fon rangi", default="#1a1a2e")
    border_color = models.CharField(max_length=20, verbose_name="Chegara rangi", default="#00adb5")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    order = models.IntegerField(default=0, verbose_name="Tartib raqami")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Reklama"
        verbose_name_plural = "Reklamalar"
        ordering = ['order']        