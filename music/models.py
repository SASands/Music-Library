from datetime import date
from platform import release
from django.db import models

# Create your models here.
# Define all the models of the images in the database

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release = models.DateField(date)
    genre = models.CharField(max_length=100)
    
