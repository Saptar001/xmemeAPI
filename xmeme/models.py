from django.db import models

# Create your models here.
class Meme(models.Model):
    name=models.CharField(max_length=100)
    meme_caption=models.CharField(max_length=200)
    meme_url=models.URLField()