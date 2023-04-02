from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


LISTA_CATEGORIAS = (
    ('valorant', 'Valorant'),
    ('tarkov', 'Tarkov'),
    ('lol', 'League of Legends'),
    ('csgo', 'Cs:Go'),
    ('r6', 'Rainbow Six Siege'),
    ('desktop', 'Desktop'),

)

class Clip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    created_at = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Episode(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    clip = models.ForeignKey("Clip", related_name="episodes", on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class User(AbstractUser):
    clip_seen = models.ManyToManyField("Clip")
